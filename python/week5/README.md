# Week 5 Homework: Monitoring a Trivia Agent with Logfire

Build a trivia quiz agent, instrument it with monitoring, and analyze its behavior through traces. The tools are already in this folder. The work is the agent, the monitoring, the queries, and the analysis.

PydanticAI and Logfire are the recommended stack. Any agent framework and any observability platform can answer the homework questions, including one you built yourself.

The quiz uses the [Open Trivia Database](https://opentdb.com/). The API is free and needs no authentication. Categories are listed on the [API config page](https://opentdb.com/api_config.php).

## How a session works

1. Pick a category and say something like "Let's play 3 medium questions from History".
2. The agent fetches questions from the API and asks the first one with multiple-choice options.
3. You answer. The agent says whether you are right or wrong, then asks the next question.
4. After the last question, the agent gives the final score and explains the correct answers.

If a homework answer does not match an option exactly, pick the closest option.

## Tools

`trivia_tools.py` talks to Open Trivia DB.

| Method | What it does |
| --- | --- |
| `get_categories()` | Lists every category id and name from `https://opentdb.com/api_category.php` |
| `get_questions(amount, category, difficulty)` | Fetches multiple-choice questions. `amount` is 1–10. `difficulty` is `easy`, `medium`, or `hard` |

Each question comes back with the correct answer and the wrong answers. HTML entities in the API text are unescaped.

The API allows one request per IP about every 5 seconds. Only one category can be requested per call. A call returns at most 50 questions.

## Run the tools

From this directory:

```bash
uv run python main.py
```

`main.py` prints the category list, then 10 easy questions from category 10.

## Project dependencies

`pyproject.toml` already includes `pydantic-ai`, `logfire`, and `requests`.
