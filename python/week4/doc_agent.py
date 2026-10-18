"""
https://aishippinglabs.com/courses/ai-buildcamp/testing/project-structure/streaming-pydanticai?cohort=4

"""
from typing import Any, Dict
import httpx2
import os
from dataclasses import dataclass

from pydantic_ai import Agent, AgentRunResult
from pydantic_ai.run import AgentRun
from pydantic_ai._agent_graph import ModelRequestNode, CallToolsNode
from pydantic_ai.messages import FunctionToolCallEvent
from openai import AsyncAzureOpenAI
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.azure import AzureProvider
from pydantic_ai.result import StreamedRunResult

import dotenv

from tools import SearchTools

dotenv.load_dotenv()

DEFAULT_INSTRUCTIONS = """
You're a documentation assistant.

Answer the user question using only the documentation knowledge base.

Make 3 iterations:

1) First iteration:
   - Perform one search using the search tool to identify potentially relevant documents.
   - Explain (in 2-3 sentences) why this search query is appropriate for the user question.

2) Second iteration:
   - Analyze the results from the previous search.
   - Based on the filenames or documents returned, perform:
       - Up to 2 additional search queries to refine or expand coverage, and
       - One or more get_file calls to retrieve the full content of the most relevant documents.
   - For each search or get_file call, explain (in 2-3 sentences) why this action is necessary and how it helps answer the question.

3) Third iteration:
   - Analyze the retrieved document contents from get_file.
   - Synthesize the information from these documents into a final answer to the user.

IMPORTANT:
- At every step, explicitly explain your reasoning for each search query or file retrieval.
- Use only facts found in the documentation knowledge base.
- Do not introduce outside knowledge or assumptions.
- If the answer cannot be found in the retrieved documents, clearly inform the user.

Additional notes:
- The knowledge base is entirely about Evidently, so you do not need to include the word "evidently" in search queries.
- Prefer retrieving and analyzing full documents (via get_file) before producing the final answer.
""".strip()


SIMPLE_INSTRUCTIONS = """
You're a documentation assistant.

Answer the user question using only the documentation knowledge base.

Make 3 iterations:

1) First iteration:
   - Perform one search using the search tool to identify potentially relevant documents.

2) Second iteration:
   - Analyze the results from the previous search.
   - Based on the filenames or documents returned, perform:
       - Up to 2 additional search queries to refine or expand coverage, and
       - One or more get_file calls to retrieve the full content of the most relevant documents.

3) Third iteration:
   - Analyze the retrieved document contents from get_file.
   - Synthesize the information from these documents into a final answer to the user.

IMPORTANT:
- Use only facts found in the documentation knowledge base.
- Do not introduce outside knowledge or assumptions.
- If the answer cannot be found in the retrieved documents, clearly inform the user.

Additional notes:
- The knowledge base is entirely about Evidently, so you do not need to include the word "evidently" in search queries.
- Prefer retrieving and analyzing full documents (via get_file) before producing the final answer.
""".strip()


"""
@dataclass is a Python decorator from the standard library (dataclasses).
It turns a class into a simple data holder by generating the boilerplate methods for you.

Without the decorator you would write __init__, and usually __repr__ and __eq__, by hand.
With it, Python generates those from the type annotations.

__init__ runs when you create an instance and stores the arguments as attributes.
__repr__ builds the string you see when you print an object or inspect it in a debugger.
    It looks like the code that would recreate the object, for example:
    DocumentationAgentConfig(model='openai:gpt-4o', name='docs', instructions='...')
__eq__ defines ==. Two configs are equal when every field has the same value.

You can construct an instance by naming fields or relying on the defaults:

    config = DocumentationAgentConfig()
    config = DocumentationAgentConfig(model='openai:gpt-4o', name='docs')

That gives you config.model, config.name, and config.instructions as normal attributes.
The generated methods also mean two configs compare equal when their fields match,
and printing one shows the field values.

A few things it does not do: it does not validate types at runtime, and fields stay
mutable unless you pass frozen=True. For validation and parsing, libraries like
Pydantic are the usual next step.
"""
@dataclass
class DocumentationAgentConfig:
    model: str = 'openai:gpt-4o-mini'
    name: str = 'search'
    instructions: str = SIMPLE_INSTRUCTIONS


from typing import Literal
from pydantic import BaseModel, Field
class RAGResponse(BaseModel):
    """
    This model provides a structured answer with metadata about the response,
    including confidence, categorization, and follow-up suggestions.
    """

    answer: str = Field(description="The main answer to the user's question in markdown")
    found_answer: bool = Field(description="True if relevant information was found in the documentation")
    confidence: float = Field(description="Confidence score from 0.0 to 1.0 indicating how certain the answer is")
    confidence_explanation: str = Field(description="Explanation about the confidence level")
    answer_type: Literal["how-to", "explanation", "troubleshooting", "comparison", "reference"] = Field(description="The category of the answer")
    followup_questions: list[str] = Field(description="Suggested follow-up questions the user might want to ask")


"""
We feed each delta into a StreamingJSONParser from jaxn - the same library we used in 
foundation week.

1. on_value_chunk prints the answer field character by character as it arrives. 
2. on_field_end prints answer_type when it's complete. 
3. on_array_item_end prints each follow-up question as it finishes.

If you skipped the streaming structured output lesson from week 1, you can check it out 
for more details on jaxn. But it's also fine to just copy the handler and use it.
"""
from jaxn import JSONParserHandler, StreamingJSONParser
class RAGResponseHandler(JSONParserHandler):
    def on_value_chunk(self, path: str, field_name: str, chunk: str) -> None:
        if path == '' and field_name == 'answer':
            print(chunk, end='', flush=True)

    def on_field_end(self, path: str, field_name: str, value: str, parsed_value: Any = None) -> None:
        if path == '' and field_name == 'answer_type':
            print('\nanswer type:', value)

    def on_array_item_end(self, path: str, field_name: str, item: Dict[str, Any] = None) -> None:
        if field_name == 'followup_questions':
            print('follow up question:', item)


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

def create_agent(
        config: DocumentationAgentConfig,
        search_tools: SearchTools
    ) -> Agent:
    tools = [search_tools.search, search_tools.get_file]
    
    search_agent = Agent(
        name=config.name,
        model=azure_model(),
        instructions=config.instructions,
        tools=tools
    )

    return search_agent



class NamedCallback:

    def __init__(self, agent):
        self.agent_name = agent.name

    async def print_function_calls(self, ctx, event):
        # Detect nested streams
        if hasattr(event, "__aiter__"):
            async for sub in event:
                await self.print_function_calls(ctx, sub)
            return

        if isinstance(event, FunctionToolCallEvent):
            tool_name = event.part.tool_name
            args = event.part.args
            print(f"TOOL CALL ({self.agent_name}): {tool_name}({args})")

    async def __call__(self, ctx, event):
        return await self.print_function_calls(ctx, event)


async def run_agent(
        agent: Agent,
        user_prompt: str,
        message_history=None
    ) -> AgentRunResult:
    callback = NamedCallback(agent)

    if message_history is None:
        message_history = []

    result = await agent.run(
        user_prompt,
        event_stream_handler=callback,
        message_history=message_history
    )

    return result



async def run_agent_structured(
        agent: Agent,
        user_prompt: str,
        message_history=None
    ) -> AgentRunResult:
    callback = NamedCallback(agent)

    if message_history is None:
        message_history = []

    result = await agent.run(
        user_prompt,
        event_stream_handler=callback,
        message_history=message_history,
        output_type=RAGResponse
    )

    return result

async def print_stream_node(node: ModelRequestNode, agent_run: AgentRun):
    async with node.stream(agent_run.ctx) as stream:
        async for text in stream.stream_text(delta=True):
            print(text, end='', flush=True)
    print()


"""
We iterate over stream.stream_responses() and check each part. 
If it's a tool-call part with the name final_result, we extract the new chunk. 
The part.args field contains the accumulated JSON so far, so we compute the delta by 
stripping what we already had: args_new[len(args_so_far):].
"""
async def print_stream_node_structured(node: ModelRequestNode, agent_run: AgentRun):
    args_so_far = ""

    parser = StreamingJSONParser(RAGResponseHandler())

    async with node.stream(agent_run.ctx) as stream:
        async for response in stream.stream_response():
            for part in response.parts:
                if part.part_kind != 'tool-call':
                    continue
                if part.tool_name != 'final_result':
                    continue

                args_new = part.args
                args_new_chunk = args_new[len(args_so_far):]
                args_so_far = args_new

                parser.parse_incremental(args_new_chunk)


    print()

async def print_tool_calls(node: CallToolsNode, agent_run: AgentRun, agent_name: str):
    async with node.stream(agent_run.ctx) as events:
        async for event in events:
            if isinstance(event, FunctionToolCallEvent):
                tool_name = event.part.tool_name
                args = event.part.args
                print(f"TOOL CALL ({agent_name}): {tool_name}({args})")

"""
PydanticAI supports streaming text output. Let's try the simple approach first, then see why we need something more powerful.
Simple Streaming with run_stream

********* run_stream Stops on Any Text

PydanticAI's run_stream has a limitation: it treats ANY text output as the final answer and stops the agent loop.

Our instructions tell the agent to "explain your reasoning" at every step. But with run_stream, that explanation text is detected as the final result and the agent stops. The tool call never executes.

Inside run_stream, PydanticAI checks every incoming part in _get_final_result_event (https://github.com/pydantic/pydantic-ai/blob/v1.59.0/pydantic_ai_slim/pydantic_ai/models/__init__.py#L1373-L1380). 
When a TextPart arrives, it stops with FinalResultEvent:

if isinstance(new_part, TextPart) and params.allow_text_output:
    return FinalResultEvent(tool_name=None, tool_call_id=None)

Then in the run_stream loop, the stream_to_final function catches this event and breaks:

async for event in stream:
    yield event
    if isinstance(event, _messages.FinalResultEvent):
        final_result_event = event
        break  # stops reading the stream

No more requests to OpenAI. The agent stops.

With agent.run(), this doesn't happen. The decision logic lives in CallToolsNode._run_stream which prioritizes tool calls over text:

# At the moment, we prioritize at least executing tool calls if they are present.
if tool_calls:
    async for event in self._handle_tool_calls(ctx, tool_calls):
        yield event
    return

In case of run, if both text and tool calls are present, tools get executed and the loop continues.
One workaround is to remove the "explain" requirement from the instructions. We create SIMPLE_INSTRUCTIONS that drop the explanation lines.
With simple instructions, the agent doesn't generate text between tool calls - it goes straight to making tool calls and only produces text for the final answer. run_stream works fine in this case.
But we lose the reasoning output. If we want the agent to explain what it's doing (which could be useful for the user), we need a different approach.

"""
async def run_agent_stream_simple(
        agent: Agent,
        user_prompt: str,
        message_history=None
    ) -> StreamedRunResult:
    callback = NamedCallback(agent)

    if message_history is None:
        message_history = []

    async with agent.run_stream(
        user_prompt,
        event_stream_handler=callback,
        message_history=message_history
    ) as stream:

        """
        Instead of returning a complete result, run_stream gives us an async context manager. 
        Inside it, result.stream_text(delta=True) yields text chunks as the model generates them.

        delta=True means we only get the new text since the last chunk, not the accumulated 
        response. 

        end='' prevents print from adding newlines between chunks. 

        flush=True tells the terminal to display each chunk immediately - without it, Python 
        buffers the output and only shows it when a newline arrives.
        """
        async for message in stream.stream_text(delta=True):
            print(message, end='', flush=True)
        print()
    return stream


"""
The Agent Graph

Internally, each PydanticAI agent uses pydantic-graph to manage its execution flow. The agent runs as a graph with 3 node types that repeat in a cycle:

UserPromptNode → ModelRequestNode → CallToolsNode → ModelRequestNode → CallToolsNode → ... → End

These node types are defined in pydantic_ai._agent_graph:

    UserPromptNode handles the initial user prompt and instructions. It runs once at the start
    ModelRequestNode sends a request to the model and receives the response. The name is from the perspective of our code: we're making a request to OpenAI. The response comes back inside this same node. There is no separate "response" node
    CallToolsNode looks at the model's response and decides what to do next. If the model requested tool calls, this node executes them and loops back to ModelRequestNode (to send tool results to the model). If there are no tool calls, it returns End (the agent produced a final answer)

agent.iter() lets you step through this graph one node at a time. Both ModelRequestNode and CallToolsNode support streaming via node.stream(ctx).

For more details, see:

    PydanticAI iteration docs - https://ai.pydantic.dev/agent/#iterating-over-an-agents-graph
    streaming events guide - https://ai.pydantic.dev/agent/#streaming-all-events-and-output
    API reference for Agent.iter - https://ai.pydantic.dev/api/agent/


Streaming with agent.iter()

To get streaming AND proper tool execution, we use agent.iter(). With iter(), we control the loop ourselves, and CallToolsNode decides when to stop - it only stops when there are no more tool calls.

The first version puts everything in one function:

from pydantic_ai.run import AgentRun
from pydantic_ai._agent_graph import ModelRequestNode, CallToolsNode
from pydantic_ai.messages import FunctionToolCallEvent

async def run_agent_stream(
        agent: Agent,
        user_prompt: str,
        message_history=None
    ) -> StreamedRunResult:

    if message_history is None:
        message_history = []

    async with agent.iter(
        user_prompt,
        message_history=message_history
    ) as agent_run:
        async for node in agent_run:
            if Agent.is_user_prompt_node(node):
                print(f"USER PROMPT ({agent.name}): {node.user_prompt}")
            elif Agent.is_model_request_node(node):
                async with node.stream(agent_run.ctx) as stream:
                    async for text in stream.stream_text(delta=True):
                        print(text, end='', flush=True)
                print()
            elif Agent.is_call_tools_node(node):
                async with node.stream(agent_run.ctx) as events:
                    async for event in events:
                        if isinstance(event, FunctionToolCallEvent):
                            tool_name = event.part.tool_name
                            args = event.part.args
                            print(f"TOOL CALL ({agent.name}): {tool_name}({args})")

        return agent_run

agent.iter() starts the agent run and gives us an agent_run object. The async for node in agent_run loop goes through each node in the graph until the agent is done.

For each node type:

    UserPromptNode - we print the user prompt
    ModelRequestNode - we open a stream with node.stream(agent_run.ctx) and print each text delta as it arrives
    CallToolsNode - we stream tool call events and print each FunctionToolCallEvent

The code works but it's deeply nested. Let's extract the streaming logic into helper functions.

print_stream_node handles ModelRequestNode - it opens a stream and prints each text delta:

async def print_stream_node(node: ModelRequestNode, agent_run: AgentRun) -> StreamedRunResult:
    async with node.stream(agent_run.ctx) as stream:
        async for text in stream.stream_text(delta=True):
            print(text, end='', flush=True)
    print()

print_tool_calls handles CallToolsNode - it streams events and prints each tool call:

async def print_tool_calls(node: CallToolsNode, agent_run: AgentRun, agent_name: str):
    async with node.stream(agent_run.ctx) as events:
        async for event in events:
            if isinstance(event, FunctionToolCallEvent):
                tool_name = event.part.tool_name
                args = event.part.args
                print(f"TOOL CALL ({agent_name}): {tool_name}({args})")
"""
async def run_agent_stream(
        agent: Agent,
        user_prompt: str,
        message_history=None
    ):

    if message_history is None:
        message_history = []

    async with agent.iter(
        user_prompt,
        message_history=message_history
    ) as agent_run:
        async for node in agent_run:
            if Agent.is_user_prompt_node(node):
                print(f"USER PROMPT ({agent.name}): {node.user_prompt}")
            elif Agent.is_model_request_node(node):
                await print_stream_node(node, agent_run)
            elif Agent.is_call_tools_node(node):
                await print_tool_calls(node, agent_run, agent.name)

        return agent_run


async def run_agent_stream_structured(
        agent: Agent,
        user_prompt: str,
        message_history=None
    ):

    if message_history is None:
        message_history = []

    async with agent.iter(
        user_prompt,
        message_history=message_history,
        output_type=RAGResponse
    ) as agent_run:
        async for node in agent_run:
            if Agent.is_user_prompt_node(node):
                print(f"USER PROMPT ({agent.name}): {node.user_prompt}")
            elif Agent.is_model_request_node(node):
                await print_stream_node_structured(node, agent_run)
            elif Agent.is_call_tools_node(node):
                await print_tool_calls(node, agent_run, agent.name)

        return agent_run

