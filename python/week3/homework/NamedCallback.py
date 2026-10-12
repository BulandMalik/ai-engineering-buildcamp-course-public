from pydantic_ai.messages import FunctionToolCallEvent

# Listener for a Pydantic AI run. Pass an instance as the event stream
# handler so each tool call is printed as it happens, labeled with the
# agent that made it. This class does not run tools and does not change
# the agent's answer. It only prints.
#
# Two agents can share this class. Each instance keeps its own name, so
# the printed line still says which agent fired the call.
class NamedCallback:

    def __init__(self, agent):
        # agent.name is only used in the printed line.
        self.agent_name = agent.name

    async def print_function_calls(self, ctx, event):
        # One model step can hand us a single event, or a stream of events.
        # A stream has __aiter__. Walk it and handle each item the same way.
        # ctx is the run context Pydantic AI passes in. This method does not
        # read it; it is kept so the signature matches the handler.
        if hasattr(event, "__aiter__"):
            async for sub in event:
                await self.print_function_calls(ctx, sub)
            return

        # FunctionToolCallEvent is the moment the model asks to call a tool.
        # part.tool_name is the function name (search, get_file, ...).
        # part.args is the arguments object the model sent.
        # Every other event (text deltas, tool results, the final answer)
        # is ignored.
        if isinstance(event, FunctionToolCallEvent):
            tool_name = event.part.tool_name
            args = event.part.args
            print(f"TOOL CALL ({self.agent_name}): {tool_name}({args})")

    async def __call__(self, ctx, event):
        # __call__ makes the instance itself callable. Pydantic AI calls
        # handler(ctx, event). This forwards that pair into
        # print_function_calls, so you can pass NamedCallback(agent)
        # where an async function is expected.
        return await self.print_function_calls(ctx, event)
