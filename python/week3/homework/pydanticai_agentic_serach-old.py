"""

In previous lessons, we implemented agents with bare OpenAI API calls and ToyAIKit. ToyAIKit is great for prototyping, learning, and debugging. For production, I recommend using a dedicated agentic framework.

Pydantic AI is my favorite agentic framework. Most agentic frameworks are similar, so if you learn one, moving to another isn't difficult.

https://aishippinglabs.com/courses/ai-buildcamp/agents/agent-frameworks/pydantic-ai?cohort=4
https://github.com/alexeygrigorev/ai-engineering-buildcamp-code/blob/1fcdb6a02f477e2a071df5058d0cd2856db062e2/03-agents/03-agent-frameworks/pydantic-ai.ipynb
https://pydantic.dev/docs/ai/overview/

"""

import os
from functools import wraps

import httpx2
from openai import AsyncAzureOpenAI
from dotenv import load_dotenv

from pydantic_ai import Agent, ModelHTTPError, UsageLimitExceeded, UsageLimits, capture_run_messages
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.azure import AzureProvider
from GetPageTool import GetPageTool
from SearchWikipediaTool import SearchWikipediaTool

load_dotenv()


#The key is designing instructions that guide the agent through a multi-step process:
instructions = """
You're a Wikipedia assistant. Answer only from English Wikipedia, using these tools:

- search_wikipedia(query, limit=10, cap=50): use this when you need to find pages.
  Pass a search query, not an exact page title. It returns total and hits.
  Each hit has title, pageid, wordcount, timestamp, and snippet.
- get_page(title): use this when you already know the exact page title.
  Pass a title such as "Capybara", not a search query. The tool reads the
  article itself and returns only {"title", "characters"}. You never receive
  the article text.

Choose the tool before you call it:

- The user names an exact article, or a previous search already gave you the
  title: call get_page with that title. Do not search first.
- The user asks a question, names a topic, or the title is uncertain: call
  search_wikipedia. Read the titles and snippets, then call get_page only for
  the page you will use in the answer.
- Do not call get_page with a search query. Do not call search_wikipedia when
  the exact title is already known.

Before the one tool call you are allowed to make at this step, write 2 to 3
sentences. Say which tool you are about to call, the exact argument, and why.
Write that in the message text.

Stop rules:
- If the user message is a page title, call get_page once with that exact
  text. Do not search. Do not call get_page again.
- After get_page returns, the next message is the final answer. Do not call
  another tool.
- If the user asks a question, call search_wikipedia once. Then call get_page
  once for the single best title. Then answer. Do not search again.

The final answer reports the character count from get_page. If the page is
missing, characters is 0. If search finds no useful title, say so.
"""


def log_calls(fn):
    # Print each Wikipedia call as it happens. The returned value is what
    # the next model request receives, so it must stay small.
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print(f"TOOL START {fn.__name__} args={args} kwargs={kwargs}", flush=True)
        result = fn(*args, **kwargs)
        if isinstance(result, dict) and "characters" in result:
            detail = f"characters={result['characters']}"
        elif isinstance(result, dict):
            detail = f"total={result.get('total')} hits={len(result.get('hits', []))}"
        else:
            detail = type(result).__name__
        print(f"TOOL END {fn.__name__} {detail}", flush=True)
        return result

    return wrapper


#Prints the messages in a human readable format
def printMessages(messages):
    """
    traditional way to print the messages
    """
    for m in messages:
        print(m.kind)
        for p in m.parts:
            part_kind = p.part_kind
            if part_kind == 'user-prompt':
                print('USER:', p.content)
            if part_kind == 'tool-call':
                print('TOOL CALL:', p.tool_name, p.args)
            if part_kind == 'tool-return':
                print('TOOL RETURN:', p.tool_name)
            if part_kind == 'text':
                print(p.content)
        print()


def is_page_title(query):
    # A title is a name or short phrase. A question has "?" or starts with
    # a question word, so those still go through search first.
    text = query.strip()
    if not text or "?" in text:
        return False
    first = text.split()[0].lower()
    question_words = {
        "who", "what", "when", "where", "why", "how",
        "which", "explain", "describe", "tell",
    }
    return first not in question_words


if __name__ == "__main__":

    # Create one instance of each tool, then pass the bound methods.
    # The modules themselves are not callable, and the class still expects
    # self. A bound method hides self, so the model only sees the arguments.
    search_tool = SearchWikipediaTool()
    page_tool = GetPageTool()
    search = log_calls(search_tool.search_wikipedia)

    def get_page(title: str) -> dict:
        """Read one Wikipedia page and return only its size.

        The article text is counted in this function and is not returned.
        The model receives the title and the character count.

        Args:
            title: Exact Wikipedia page title, for example "Nelson Mandela".

        Returns:
            dict: {"title": str, "characters": int}. characters is the length
            of the full page. 0 means the title was blank or the page is missing.
        """
        content = page_tool.get_page(title)
        return {"title": title, "characters": len(content)}

    get_page = log_calls(get_page)

    # Pydantic AI does not take llm_client=. The earlier ToyAIKit / hand-written
    # agents used the sync AzureOpenAI client and passed it in. This Agent
    # wants a Model object, and that model talks through an async client.
    #
    # model_name is the Azure deployment name (AZURE_OPENAI_DEPLOYMENT),
    # not the public model id such as gpt-4o.
    #
    # AzureProvider's own env fallback for the version is OPENAI_API_VERSION.
    # This project stores the version in AZURE_OPENAI_API_VERSION, so pass it
    # explicitly. Passing openai_client= also works:
    #   AzureProvider(openai_client=AsyncAzureOpenAI(...))
    # The string form Agent("azure:" + deployment_name) only works if
    # OPENAI_API_VERSION is set, because that form builds AzureProvider()
    # with no arguments.
    deployment_name = os.environ["AZURE_OPENAI_DEPLOYMENT"]
    # The OpenAI SDK default is Timeout(timeout=600, connect=5.0). It does
    # not read OPENAI_CLIENT_* from the environment. On this machine
    # *.openai.azure.com resolves to a local proxy, and the TCP handshake
    # takes longer than 5 seconds, so the call dies as ConnectTimeout /
    # "Request timed out" before Azure sends a status.
    timeout = httpx2.Timeout(
        connect=float(os.environ["OPENAI_CLIENT_CONNECT_TIMEOUT"]),
        read=float(os.environ["OPENAI_CLIENT_READ_TIMEOUT"]),
        write=float(os.environ["OPENAI_CLIENT_WRITE_TIMEOUT"]),
        pool=float(os.environ["OPENAI_CLIENT_POOL_TIMEOUT"]),
    )
    azure_client = AsyncAzureOpenAI(
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
        azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
        api_version=os.environ["AZURE_OPENAI_API_VERSION"],
        timeout=timeout,
    )
    model = OpenAIChatModel(
        deployment_name,
        provider=AzureProvider(openai_client=azure_client),
    )

    # A bare title only gets get_page, and only one tool call is allowed.
    # A question may search once and then open one page.
    query = 'Nelson Mandela'
    title_only = is_page_title(query)
    tools = [get_page] if title_only else [search, get_page]
    limits = UsageLimits(
        request_limit=3 if title_only else 5,
        tool_calls_limit=1 if title_only else 2,
    )
    print(f"USER: {query}", flush=True)
    print(
        f"title_only={title_only} tools={[fn.__name__ for fn in tools]} "
        f"tool_calls_limit={limits.tool_calls_limit}",
        flush=True,
    )

    # Docstrings on search_wikipedia and get_page become the tool descriptions.
    agent = Agent(
        model,
        name="Search Wikipedia Agent",
        instructions=instructions,
        tools=tools,
    )

    # run_sync blocks until the model stops calling tools. result.output is
    # the final text. The limits above end the loop if it tries to continue.
    with capture_run_messages() as messages:
        try:
            result = agent.run_sync(query, usage_limits=limits)
        except ModelHTTPError as err:
            print(f"MODEL ERROR status={err.status_code} body={err.body}", flush=True)
            printMessages(messages)
            raise
        except UsageLimitExceeded as err:
            print(f"LOOP STOPPED {err}", flush=True)
            printMessages(messages)
            raise
    print(result.output)
    printMessages(result.all_messages())

    #Interactive QA Loop
"""     from pydantic_ai import RunUsage
    messages = []
    usage = RunUsage()
    while True:
        query = input("Enter a question: ")
        if query.lower() in ["quit", "exit", "q"]:
            break
        result = agent.run_sync(query, message_history=messages)
        usage = usage + result.usage
        printMessages(result.new_messages()) #only messages for new prompt
        messages.extend(result.new_messages()) """

