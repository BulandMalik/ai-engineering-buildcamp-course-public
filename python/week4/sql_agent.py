"""Agent that answers questions about the taxi trips table."""

import os
import sys
from pathlib import Path

import httpx2
from dotenv import load_dotenv
from openai import AsyncAzureOpenAI
from pydantic import BaseModel, Field
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIChatModel
from pydantic_ai.providers.azure import AzureProvider

from sql_tools import SQLTools
from utils import collect_tools

load_dotenv(Path(__file__).with_name(".env"))


class SQLResult(BaseModel):
    """Structured answer from a SQL question."""

    sql_query: str = Field(description="The SQL query that produced the answer")
    result_text: str = Field(description="Text returned by run_sql, including the header")
    row_count: int = Field(description="Number of data rows in result_text, excluding the header")


instructions = """
You answer questions about NYC yellow taxi trips stored in DuckDB.
The only table is trips.

Always call get_schema before you run any SQL. Use the column names and
types it returns. Do not guess column names.

Then call run_sql with a DuckDB query that answers the question.
Answer only what was asked. Do not add filters the user did not request.
If run_sql returns an error, fix the query and call run_sql again.

Return SQLResult from the successful query:
- sql_query is the query you ran
- result_text is the run_sql text, unchanged
- row_count is the number of data rows, not counting the header line
"""


def azure_model() -> OpenAIChatModel:
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


sql_tools = SQLTools()

agent = Agent(
    azure_model(),
    name="SQL Agent",
    output_type=SQLResult,
    instructions=instructions,
    tools=[sql_tools.get_schema, sql_tools.run_sql],
)


def main():
    if len(sys.argv) > 1:
        question = " ".join(sys.argv[1:]).strip()
    else:
        question = input("Ask a question: ").strip()
    if not question:
        return

    result = agent.run_sync(question)
    calls = collect_tools(result.all_messages())
    print(f"TOOL CALLS ({len(calls)}):")
    for number, call in enumerate(calls, start=1):
        print(f"  {number}. {call}")
    print("ANSWER:")
    print(result.output)


if __name__ == "__main__":
    main()
