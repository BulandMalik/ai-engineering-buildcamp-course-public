import tempfile
from pathlib import Path
import json
import os


MODEL_PRICES = {
    "openai:gpt-4o-mini": {"input": 0.15, "output": 0.60},
    "openai:gpt-4o": {"input": 2.50, "output": 10.00},
    "openai:gpt-5.2": {"input": 1.75, "output": 14.00},
    "openai:gpt-5.4-mini": {"input": 0.75, "output": 4.50},
    "gpt-5.4-mini": {"input": 0.75, "output": 4.50},
    "anthropic:claude-haiku-4-5": {"input": 1.00, "output": 5.00},
    "anthropic:claude-sonnet-4-6": {"input": 3.00, "output": 15.00},
}

COST_FILE = Path(tempfile.gettempdir()) / "pytest_cost_tracker.jsonl"

def prices_for(model_name):
    name = model_name.lower()
    if name in MODEL_PRICES:
        return MODEL_PRICES[name]
    prefixed = name if ":" in name else f"openai:{name}"
    return MODEL_PRICES.get(prefixed)


def calculate_cost(model_name, input_tokens, output_tokens):
    prices = prices_for(model_name)
    if prices is None:
        return 0
    input_cost = (input_tokens / 1_000_000) * prices["input"]
    output_cost = (output_tokens / 1_000_000) * prices["output"]
    return input_cost + output_cost

def reset_cost_file():
    COST_FILE.unlink(missing_ok=True)

from collections import defaultdict

#usages = defaultdict(RunUsage)

def capture_usage(model, result):
    # AgentRunResult.usage is a property in PydanticAI 2.57, while older
    # versions exposed it as a method. Support both APIs.
    usage = result.usage() if callable(result.usage) else result.usage
    entry = {
        "model": model,
        "input_tokens": usage.input_tokens,
        "output_tokens": usage.output_tokens,
    }
    with open(COST_FILE, "a") as f:
        f.write(json.dumps(entry) + "\n")    


def display_total_usage():
    print()

    if not COST_FILE.exists():
        print("Total cost: $0.000000")
        return

    totals = {}
    for line in COST_FILE.read_text().splitlines():
        entry = json.loads(line)
        model = entry["model"]
        if model not in totals:
            totals[model] = {"input_tokens": 0, "output_tokens": 0}
        totals[model]["input_tokens"] += entry["input_tokens"]
        totals[model]["output_tokens"] += entry["output_tokens"]

    total_cost = 0
    for model, tokens in totals.items():
        cost = calculate_cost(model, tokens["input_tokens"], tokens["output_tokens"])
        print(f"{model}: ${cost:.6f}")
        total_cost += cost
    print(f"Total cost: ${total_cost:.6f}")

