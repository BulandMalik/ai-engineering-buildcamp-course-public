"""Agent that answers from English Wikipedia.

Question 5 gives a page URL. The agent calls get_page once and summarizes.
Question 6 asks a question. The agent searches, then calls get_page once,
then answers. get_page here is GetPageTool.get_excerpt: plain text, capped,
not the 200,000-character wikitext.
"""

import os

import httpx2
from dotenv import load_dotenv
from openai import AsyncAzureOpenAI
from pydantic_ai import Agent, Tool, UsageLimits
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.azure import AzureProvider

from GetPageTool import GetPageTool
from NamedCallback import NamedCallback
from SearchWikipediaTool import SearchWikipediaTool

load_dotenv()

instructions = """
You're a Wikipedia assistant. Answer only from tool results.

Tools:
- search_wikipedia(query): find pages. Use a short query, not a full question.
  It returns titles and snippets. It does not return the article.
- get_page(title): read one page. Pass the exact title, such as "Capybara".
  It returns a plain-text excerpt. It does not return raw wikitext.
- get_page_size(title): count all characters in one page. Use this only when
  the user asks for the page's character count. It returns one integer.

Choose tools based on the task:
- To count search results or inspect result titles, call search_wikipedia.
- To count a page's characters, call get_page_size with the exact title.
- To summarize a page or answer from its contents, call get_page.

If the user message contains a Wikipedia URL like
https://en.wikipedia.org/wiki/Capybara:
- Take the title from the last part of the URL. Replace underscores with spaces.
- Call get_page once with that title.
- Do not call search_wikipedia.
- Then write a short summary and name the main topic in one sentence.
- Stop. Do not call another tool.

If the user asks a question and does not give a page URL:
- Call search_wikipedia once.
- From the titles and snippets, choose the one best page.
- Call get_page once with that title.
- Answer from that excerpt.
- Stop. Do not search again and do not open a second page.

Before each tool call, write 2 or 3 sentences: which tool, the exact argument,
and why. After the last tool returns, give the final answer and stop.
"""


def tool_calls(messages):
    calls = []
    for message in messages:
        for part in message.parts:
            if part.part_kind == "tool-call":
                calls.append(f"{part.tool_name} {part.args}")
    return calls


def azure_model():
    timeout = httpx2.Timeout(
        connect=float(os.environ["OPENAI_CLIENT_CONNECT_TIMEOUT"]),
        read=float(os.environ["OPENAI_CLIENT_READ_TIMEOUT"]),
        write=float(os.environ["OPENAI_CLIENT_WRITE_TIMEOUT"]),
        pool=float(os.environ["OPENAI_CLIENT_POOL_TIMEOUT"]),
    )
    client = AsyncAzureOpenAI(
        api_key=os.environ["AZURE_OPENAI_API_KEY"],
        azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
        api_version=os.environ["AZURE_OPENAI_API_VERSION"],
        timeout=timeout,
    )
    return OpenAIChatModel(
        os.environ["AZURE_OPENAI_DEPLOYMENT"],
        provider=AzureProvider(openai_client=client),
    )


def run_question(agent, question, tool_calls_limit=2):
    print(f"\nUSER: {question}", flush=True)
    result = agent.run_sync(
        question,
        usage_limits=UsageLimits(
            request_limit=tool_calls_limit + 2,
            tool_calls_limit=tool_calls_limit,
        ),
        event_stream_handler=NamedCallback(agent),
    )
    calls = tool_calls(result.all_messages())
    print(f"TOOL CALLS ({len(calls)}):", flush=True)
    for number, call in enumerate(calls, start=1):
        print(f"  {number}. {call}", flush=True)
    print("ANSWER:", flush=True)
    print(result.output, flush=True)
    return result


def create_agent():
    search_tool = SearchWikipediaTool()
    page_tool = GetPageTool()

    # One agent gets every Wikipedia capability. Its instructions choose the
    # right tool for each question.
    get_page = Tool(page_tool.get_excerpt, name="get_page")
    get_page_size = Tool(page_tool.get_page, name="get_page_size")
    search = Tool(search_tool.search_wikipedia, name="search_wikipedia")
    return Agent(
        azure_model(),
        name="Wikipedia Agent",
        instructions=instructions,
        tools=[search, get_page, get_page_size],
    )


def main():
    # Construct the model and agent once, then reuse them for every question.
    # Runs are independent unless message_history is explicitly passed.
    agent = create_agent()

    run_question(
        agent,
        "What is this page about? https://en.wikipedia.org/wiki/Capybara",
        tool_calls_limit=1,
    )
    run_question(
        agent,
        "What are the main threats to capybara populations?",
        tool_calls_limit=2,
    )


if __name__ == "__main__":
    main()
