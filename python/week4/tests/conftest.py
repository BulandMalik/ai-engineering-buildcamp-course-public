"""Record the cost of every model call during pytest.

pytest loads this file automatically. The two hooks below bookend the session:

1. pytest_sessionstart clears the previous cost file and wraps Agent.run.
2. pytest_sessionfinish reads that file and prints the total cost.

Tests do not call capture_usage themselves. agent.run_sync and the judge both
end up in Agent.run, so one wrap records every model call.
"""

from pydantic_ai import Agent

from tests.cost_tracker import capture_usage
from tests.cost_tracker import display_total_usage
from tests.cost_tracker import reset_cost_file


def _model_name(agent):
    """Return the deployment name stored on the agent, such as gpt-5.4-mini."""
    model = getattr(agent, "model", None)
    return getattr(model, "model_name", None) or str(model)


def pytest_sessionstart(session):
    # Drop the cost file from the last pytest run so this total starts at zero.
    reset_cost_file()

    # Keep the real method, then replace it with a version that also records tokens.
    # run_sync calls self.run, so wrapping run covers both the SQL agent and the judge.
    original_run = Agent.run

    async def run(self, *args, **kwargs):
        result = await original_run(self, *args, **kwargs)
        # Append this run's model name and token counts to the cost file.
        capture_usage(_model_name(self), result)
        return result

    Agent.run = run


def pytest_sessionfinish(session, exitstatus):
    # Print one line per model, then the combined cost for this test session.
    display_total_usage()
