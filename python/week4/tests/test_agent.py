import asyncio
import re

from judge import assert_criteria
from sql_agent import agent
from utils import collect_tools

#QUESTION = "How many trips had more than 5 passengers?"
# COUNT(*) FROM trips WHERE passenger_count > 5
#TRIPS_WITH_MORE_THAN_5_PASSENGERS = "22413"


# Pytest collects any function named test_* in a test_*.py file.
# No decorator is required for a plain assertion test.
def test_trips_with_more_than_5_passengers():
    question = "How many trips had more than 5 passengers?"
    expected_answer = "22413"

    result = agent.run_sync(question)
    output = result.output

    assert isinstance(output.sql_query, str)
    assert output.sql_query.strip()
    assert expected_answer in output.result_text


"""
In test_agent.py, write a test that:

    Ask "What is the most common payment type?"
    Asserts the first tool call is get_schema
    Asserts that run_sql is also called

What is the name of the second tool the agent calls?
"""
def test_most_common_payment_type():
    question = "What is the most common payment type?"
    expected_answer = "22413"
    expected_tool_calls = ["get_schema", "run_sql"]

    result = agent.run_sync(question)
    calls = collect_tools(result.all_messages())
    # Pytest captures stdout and hides it when the test passes.
    # Run with -s to see this: uv run pytest tests/test_agent.py -s
    print(calls)

    assert calls[0].startswith("get_schema")
    assert calls[1].startswith("run_sql")


def test_highest_average_fare_by_hour():
    question = "Which hour of the day has the highest average fare amount?"
    criteria = [
        "the SQL query correctly calculates average fare by hour of day",
        "the result identifies a specific hour as having the highest average fare",
        "the result includes the actual average fare amount",
    ]

    result = agent.run_sync(question)
    asyncio.run(assert_criteria(result, criteria))


def tool_names(result):
    return [call.split()[0] for call in collect_tools(result.all_messages())]


def assert_scenario(question, columns, expected):
    """Check tool order, the columns used in the SQL, and the result value."""
    result = agent.run_sync(question)
    output = result.output
    names = tool_names(result)

    assert names[0] == "get_schema"
    assert "run_sql" in names[1:]
    sql = output.sql_query.lower()
    for column in columns:
        assert column.lower() in sql, output.sql_query
    if isinstance(expected, str):
        assert expected.lower() in output.result_text.lower(), output.result_text
        return
    numbers = [float(match) for match in re.findall(r"-?\d+(?:\.\d+)?", output.result_text)]
    assert any(abs(number - expected) < 0.02 for number in numbers), output.result_text


def test_average_tip_for_credit_card_payments():
    # Columns: tip_amount, payment_type. Credit card tips average about 4.17.
    assert_scenario(
        "What is the average tip amount for credit card payments?",
        ["tip_amount", "payment_type"],
        4.17,
    )


def test_pickup_location_with_most_trips():
    # Column: PULocationID. Location 132 has the most trips.
    assert_scenario(
        "Which pickup location (PULocationID) has the most trips?",
        ["PULocationID"],
        132,
    )


def test_average_fare_for_trips_longer_than_10_miles():
    # Columns: fare_amount, trip_distance. Average fare is about 62.88.
    assert_scenario(
        "What is the average fare for trips longer than 10 miles?",
        ["fare_amount", "trip_distance"],
        62.88,
    )


def test_trips_with_zero_passengers():
    # Filter column: passenger_count. passenger_count = 0 matches 31465 trips.
    assert_scenario(
        "How many trips had zero passengers recorded?",
        ["passenger_count"],
        31465,
    )


def test_busiest_day_of_week():
    # Column: tpep_pickup_datetime. Wednesday has the most trips.
    assert_scenario(
        "What is the busiest day of the week for taxi trips?",
        ["tpep_pickup_datetime"],
        "Wednesday",
    )