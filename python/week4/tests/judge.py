from pydantic import BaseModel, Field
from pydantic_ai import Agent 

from sql_agent import azure_model
from utils import collect_tools


judge_instructions = f"""
You are an expert judge evaluating the performance of an AI agent.
""".strip()


"""
The judgement field is important - it forces the LLM to explain its reasoning before 
deciding pass/fail. 
Without it, the judge might be lazy and just output True/False without thinking.
"""
class JudgeCriterion(BaseModel):
    """
    Evaluation of a single test requirement or behavioral rule.
    """
    criterion_description: str = Field(
        description="The specific requirement or rule that the agent is being evaluated against."
    )
    passed: bool = Field(
        description="Indicates whether the agent's response and actions successfully satisfied this requirement."
    )
    judgement: str = Field(
        description="A clear explanation of why the agent passed or failed, referencing specific evidence from the agent's output or tool calls."
    )


class JudgeFeedback(BaseModel):
    """
    The complete evaluation report from the judge agent, summarizing performance across all criteria.
    """
    criteria: list[JudgeCriterion] = Field(
        description="A collection of individual evaluations for each performance requirement provided in the test."
    )
    feedback: str = Field(
        description="A holistic summary of the agent's performance, providing overall context and identifying key strengths or failures."
    )


"""
We send the agent output as JSON using model_dump_json(). JSON is token-heavy, so if you 
want to cut costs, you could implement a to_text() method on your output model. 

For tool call results, I typically don't include them - they can be large and aren't usually 
useful for the judge.
"""
def create_judge_agent():
    agent = Agent(
        name="judge",
        model=azure_model(),
        instructions=judge_instructions,
        output_type=JudgeFeedback
    )
    return agent


"""
The prompt template includes the agent's output, tool calls, and the criteria to evaluate:
"""
judge_user_prompt_template = """
Evaluate the agent's performance based on the following criteria:
<CRITERIA>
{criteria}
</CRITERIA>

The agent's final output was:
<AGENT_OUTPUT>
{output}
</AGENT_OUTPUT>

Tool calls:
<TOOL_CALLS>
{tool_calls}
</TOOL_CALLS>

Return one criterion for each requirement, in the same order.
""".strip()



"""
evaluate_agent_performance collects tool calls, formats the prompt, and runs the judge.
assert_criteria checks that every criterion passed.
"""
async def evaluate_agent_performance(result, criteria) -> JudgeFeedback:
    messages = result.new_messages()
    tool_calls = collect_tools(messages)
    output = result.output.model_dump_json()

    judge_agent = create_judge_agent()
    judge_user_prompt = judge_user_prompt_template.format(
        criteria='\n'.join(criteria),
        output=output,
        tool_calls='\n'.join(tool_calls),
    )

    print("\n\n--------------------------------\n\n")
    print("judge_user_prompt:", judge_user_prompt)
    print("\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n")
    print("tool_calls:", tool_calls)
    print("\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n")
    print("output:", output)
    print("\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n")
    print("criteria:", criteria)
    print("\n\n--------------------------------\n\n")

    judge_result = await judge_agent.run(judge_user_prompt)
    return judge_result.output


async def assert_criteria(result, criteria):
    feedback = await evaluate_agent_performance(result, criteria)

    print('judge feedback:')
    print(feedback.feedback)

    for criterion in feedback.criteria:
        print(f"{criterion.criterion_description}: {criterion.judgement}")
        assert criterion.passed, f"{criterion.criterion_description}: {criterion.judgement}"
