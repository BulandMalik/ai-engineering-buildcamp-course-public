import logfire

from trivia_tools import TriviaTools
from trivia_agent import TriviaAgent
from utils import collect_tools


# Send traces when a Logfire token or a local `logfire auth` login is present.
# The agent still runs if neither is configured.
logfire.configure(service_name="trivia-agent", send_to_logfire="if-token-present")
logfire.instrument_pydantic_ai()


def main():
    trivia_tools = TriviaTools()

    print(trivia_tools.get_categories())
    print(trivia_tools.get_questions(10, 10, "easy"))

def trivia_agent():
    quiz = TriviaAgent("Trivia Agent", logfire)
    messages = []
    prompt = input("What do you want to play? ").strip()

    # Turn-taking is this loop. Each run_sync is a new model call.
    # message_history sends back the earlier questions, tool results, and
    # answers, which is how the agent still knows question 1 on the next turn.
    # The instructions decide the reply: one question, then a grade, then the
    # next question, and a line starting with "Final score:" when the quiz ends.
    # Nothing here says "ask question 2" or which choice is correct.
    while prompt and prompt.lower() not in {"quit", "exit", "q"}:
        result = quiz.agent.run_sync(prompt, message_history=messages)
        messages = result.all_messages()
        print()
        print(result.output)
        if "final score:" in str(result.output).lower():
            break
        prompt = input("\nYour answer: ").strip()

    print()
    print(collect_tools(messages))

def run(prompt):

    quiz = TriviaAgent("Trivia Agent", logfire)
    message_history = []

    with quiz.logfire.span('trivia_session'):
        while True:
            result = quiz.agent.run_sync(prompt, message_history=message_history)
            print(result.output)
            message_history = result.all_messages()

            prompt = input("You (write 'stop' to stop): ")
            if not prompt or prompt.lower().strip() == 'stop':
                break

def calculate_cost(input_tokens, output_tokens):
    """Approximate cost at gpt-4o-mini rates: $0.15 / 1M input, $0.60 / 1M output."""
    input_cost = (input_tokens / 1_000_000) * 0.15
    output_cost = (output_tokens / 1_000_000) * 0.60
    return input_cost + output_cost


def reconstruct_session(trace_id, client, min_timestamp):
    """Turn a grouped session trace into one AgentRunResult and its gpt-4o-mini cost.

    Token counts are the sum of every invoke_agent span in the trace.
    """
    import trace_replay

    trace = trace_replay.fetch_session_trace(trace_id, client, min_timestamp=min_timestamp)
    result = trace_replay.trace_to_run_result(trace)
    cost = calculate_cost(result.usage.input_tokens, result.usage.output_tokens)
    return result, cost


def reading_logfire_data():
    import os
    from datetime import datetime, timedelta, timezone

    from dotenv import load_dotenv
    from logfire.query_client import LogfireQueryClient

    load_dotenv()
    # The query API rejects LOGFIRE_TOKEN. That token only sends traces.
    client = LogfireQueryClient(read_token=os.environ["LOGFIRE_READ_TOKEN"])
    started = datetime.now(timezone.utc) - timedelta(days=2)

    # sessions: only the grouped-quiz parents. span_name is trivia_session and
    # parent_span_id is null. Each row is the root span of one quiz, and its
    # trace_id is that whole session. Older quizzes with no trivia_session
    # wrapper are not in this list. trivia-agent is the service name on every
    # span, not the span name.
    #
    # SELECT trace_id, min(start_timestamp) AS started, count(*) AS spans
    # FROM records
    # WHERE service_name = 'trivia-agent'
    # GROUP BY trace_id
    sessions = client.query_json_rows(
        """
        SELECT trace_id, span_id, parent_span_id, span_name, start_timestamp
        FROM records
        WHERE service_name = 'trivia-agent'
          AND span_name = 'trivia_session'
          AND parent_span_id IS NULL
        ORDER BY start_timestamp
        """,
        min_timestamp=started,
    )
    # runs: every invoke_agent span. A run inside a session has parent_span_id
    # set to that session's span_id. A run from before the wrapper has
    # parent_span_id null, so that span is the root of its own trace.
    runs = client.query_json_rows(
        """
        SELECT trace_id, span_id, parent_span_id, span_name, start_timestamp
        FROM records
        WHERE service_name = 'trivia-agent'
          AND span_name = 'invoke_agent Trivia Agent'
        ORDER BY start_timestamp
        """,
        min_timestamp=started,
    )

    # Keep the runs whose parent is a session span. The other runs stay out.
    runs_by_parent = {}
    for run in runs["rows"]:
        runs_by_parent.setdefault(run["parent_span_id"], []).append(run)

    for session in sessions["rows"]:
        children = runs_by_parent.get(session["span_id"], [])
        print(
            f"{session['trace_id']}  span_id={session['span_id']}  "
            f"parent_span_id={session['parent_span_id']}  "
            f"agent_runs={len(children)}  started={session['start_timestamp']}"
        )
        
        result, cost = reconstruct_session(session['trace_id'], client, started)
        usage = result.usage
        print(
            f"input_tokens={usage.input_tokens}  output_tokens={usage.output_tokens}  "
            f"cost=${cost:.6f}"
        )
        print(result.output)

if __name__ == "__main__":
    #main()
    #trivia_agent()
    #run("Let's play 5 easy questions from Science & Nature")
    reading_logfire_data()

