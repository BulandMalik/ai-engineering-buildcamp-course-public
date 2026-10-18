# Everything We Talked About (Explained Like You're 10)

This file collects every question we went through about `doc_agent.py`, in order,
with simple explanations and examples.

---

## 1. What does `@dataclass` do?

Imagine you have a form you fill out a lot, like a library card:

```
Name: ____
Favorite Book: ____
```

Normally in Python, you'd have to write code by hand that says "take the name
the person gives you and write it on the card, take the favorite book and
write it on the card too." That's boring and repetitive.

`@dataclass` is a magic stamp you put above a class. It tells Python:
"Look at the fields I listed, and automatically build the boring stuff for me."

```python
from dataclasses import dataclass

@dataclass
class DocumentationAgentConfig:
    model: str = 'openai:gpt-4o-mini'
    name: str = 'search'
    instructions: str = SIMPLE_INSTRUCTIONS
```

Without `@dataclass`, you'd have to write all of this yourself:

```python
class DocumentationAgentConfig:
    def __init__(self, model='openai:gpt-4o-mini', name='search', instructions=SIMPLE_INSTRUCTIONS):
        self.model = model
        self.name = name
        self.instructions = instructions

    def __repr__(self):
        return f"DocumentationAgentConfig(model={self.model!r}, name={self.name!r}, instructions={self.instructions!r})"

    def __eq__(self, other):
        return (self.model, self.name, self.instructions) == (other.model, other.name, other.instructions)
```

`@dataclass` writes all of that for you, instantly, just from the three lines
of fields.

### How you use it

```python
config = DocumentationAgentConfig()
config2 = DocumentationAgentConfig(model='openai:gpt-4o', name='docs')
```

### What it does NOT do

- It does not check that `model` is actually a real string at runtime — it trusts you.
- The fields can still be changed after creation (unless you add `frozen=True`).

---

## 2. What do `__init__`, `__repr__`, and `__eq__` actually do?

These are "magic methods." Python calls them for you automatically in certain
situations. Think of them like buttons on a toy that do something automatically
when pressed — you don't press them yourself, Python does.

### `__init__` — the "when you're born" button

This runs the moment you create an object. It's where the object's info gets
filled in.

```python
config = DocumentationAgentConfig(model='openai:gpt-4o', name='docs')
# Python runs __init__ behind the scenes and now:
# config.model == 'openai:gpt-4o'
# config.name == 'docs'
```

### `__repr__` — the "what should I look like on a name tag" button

This runs when you `print()` an object or look at it in a debugger. It's like
a name tag that shows all your important info.

```python
print(config)
# DocumentationAgentConfig(model='openai:gpt-4o', name='docs', instructions='...')
```

### `__eq__` — the "are we the same" button

This runs when you use `==` between two objects. Without it, Python would
normally say two different objects are never equal, even if they look the
same. With `@dataclass`, two configs with the same field values ARE considered
equal.

```python
a = DocumentationAgentConfig(name='search')
b = DocumentationAgentConfig(name='search')
a == b  # True, because every field matches
```

---

## 3. Why do we use `asyncio`, and why are functions defined as `async`?

Imagine you're making toast and also boiling an egg. You don't stand frozen
staring at the toaster waiting — you start the toaster, then start boiling the
egg, and check on both occasionally. That's **async**: doing things that take
time without freezing everything else.

Talking to Azure OpenAI (the AI model) over the internet takes time — maybe a
few seconds. If Python just sat there frozen waiting for the reply, nothing
else could happen during that time.

`async def` marks a function as "this function might need to wait for
something (like a reply from the internet), and that's OK — it won't freeze
the whole program while waiting."

When you call an async function, you have to `await` it, which means
"wait for this to finish, but let other things happen while waiting."

```python
async def run_agent(agent, user_prompt, message_history=None):
    result = await agent.run(user_prompt, ...)  # waits for the AI's reply
    return result
```

Because `agent.run(...)` itself waits on a network call, any function that
calls it must also be `async def`, and must `await` it. This spreads upward:

- `run_agent` is `async` because it awaits `agent.run(...)`.
- `run_agent_stream` is `async` because it awaits streaming pieces of the model's reply.
- `main()`-style code uses `asyncio.run(...)` to actually kick off the very first async function, since regular Python code can't `await` anything on its own.

```python
if __name__ == "__main__":
    import asyncio
    asyncio.run(run_agent_question())
```

**The simple rule:** Because the AI client we use (`AsyncAzureOpenAI`) only
knows how to work in "wait, but don't freeze" mode, every function in the
chain that eventually talks to it also has to be async, all the way up to the
very first line that starts everything.

---

## 4. The import error we fixed

We had a broken line:

```python
import pydantic_ai.run.stream as stream
from pydantic_ai.run.stream import StreamedRunResult
```

This crashed with:

```
ModuleNotFoundError: No module named 'pydantic_ai.run.stream'; 'pydantic_ai.run' is not a package
```

**Why:** `pydantic_ai.run` is a single file (like one page), not a folder
(package) with more pages inside it. So Python can't look "inside" it for
something called `stream`.

**The fix:** The thing we actually wanted, `StreamedRunResult`, lives in a
different file: `pydantic_ai.result`. We changed the import to:

```python
from pydantic_ai.result import StreamedRunResult
```

And removed the broken line entirely, since it wasn't needed.

---

## 5. The Agent Graph — the big one

This is the trickiest part, so let's use a board game analogy.

### Think of it like a board game with 3 kinds of spaces

Imagine a board game with only 3 types of spaces you can land on:

1. 🟦 **Start Space** (`UserPromptNode`) — this is where your question gets written down.
2. 🟨 **Ask-the-Wizard Space** (`ModelRequestNode`) — you ask the AI wizard a question and listen to the answer.
3. 🟩 **Do-What-the-Wizard-Said Space** (`CallToolsNode`) — if the wizard said "go search this" or "go fetch that file," you do it here.

The rules of the board are always the same:

- 🟦 Start → always goes to 🟨 Ask-the-Wizard.
- 🟨 Ask-the-Wizard → always goes to 🟩 Do-What-the-Wizard-Said, carrying whatever the wizard just said.
- 🟩 Do-What-the-Wizard-Said → looks at what the wizard said:
  - If the wizard asked for tools (searches, file lookups) → go back to 🟨 Ask-the-Wizard (to tell the wizard what you found).
  - If the wizard just gave a final answer with no requests → go to 🏁 **End**.

### The important part: the board doesn't pre-draw your whole path

Nobody draws your exact path on the board before you start playing. The
*rules* for each space exist ahead of time, but your actual path (how many
times you bounce between the wizard and the tools) is discovered step by step,
AS you play — because it depends on what the wizard actually says, which you
don't know yet.

### What `agent.iter(...)` gives you

Calling `agent.iter(user_prompt)` is like saying "let's start this game" and
placing your piece on 🟦 Start. That's it. Nothing else has happened yet.

It also gives you `agent_run` — think of this as your **notebook** for the
whole game. Every space you land on writes something into this notebook: your
question, the wizard's replies, the tool results. The notebook keeps growing
the whole game, and everyone (every space) reads from the SAME notebook.

### What `async for node in agent_run:` does, one turn at a time

This is the "take a turn" loop. Each time through the loop:

1. It plays out whatever space you're currently standing on (this is where the
   real work happens — asking the wizard, or doing the tools).
2. Playing that space decides which space comes next.
3. It moves your piece there and hands you that new space to look at.

It keeps doing this, turn after turn, until a space says "go to 🏁 End" —
then the loop stops.

```python
async for node in agent_run:
    if Agent.is_user_prompt_node(node):
        print(f"USER PROMPT ({agent.name}): {node.user_prompt}")
    elif Agent.is_model_request_node(node):
        await print_stream_node(node, agent_run)
    elif Agent.is_call_tools_node(node):
        await print_tool_calls(node, agent_run, agent.name)

return agent_run
```

Walking through an example game:

- **Turn 1:** You're handed the 🟦 Start space. You print the question. Nothing has "played" yet.
- Before turn 2, the loop quietly plays the 🟦 Start space for you (writes your question in the notebook) and builds a fresh 🟨 Ask-the-Wizard space.
- **Turn 2:** You're handed that 🟨 Ask-the-Wizard space. You call `print_stream_node`, which does `node.stream(agent_run.ctx)`. **This line is what actually talks to the AI wizard over the internet and prints its words as they arrive.** By the time this finishes, the space already knows what comes next: a 🟩 Do-What-the-Wizard-Said space, built from exactly what the wizard just said.
- **Turn 3:** You're handed that 🟩 space. You call `print_tool_calls`, which does `node.stream(agent_run.ctx)` again. **This line is what actually runs the search or file lookup.** While doing that, this space decides: more requests? → next space is another 🟨 Ask-the-Wizard. Nothing left to do? → next is 🏁 End.
- The loop repeats turns 2–3 as many times as needed — maybe 2 times, maybe 6 — nobody knew the number in advance. It depends on what the wizard asks for.
- Eventually a 🟩 space says "go to End," and the `async for` loop stops by itself.

### So, "does `node.stream(...)` do the real work?" — Yes!

`node.stream(agent_run.ctx)` is the line that actually DOES the thing:

- On a 🟨 Ask-the-Wizard space, it sends your whole notebook so far to Azure
  OpenAI and streams back the reply, word by word.
- On a 🟩 Do-What-the-Wizard-Said space, it actually calls your Python
  functions (`search`, `get_file`) and writes the results in the notebook.

And as a side effect of doing that real work, each space also figures out
what the next space should be — which is how the "board game" extends itself
turn by turn, instead of being planned out from the start.

### What's shared, and what's node-specific?

- **Shared and growing:** `agent_run.ctx` holds one big list of messages (the
  notebook) — question, wizard replies, tool results, in order. Every space
  reads the WHOLE notebook when it needs context (especially the wizard,
  who needs to remember everything said so far to keep making sense).
- **Node-specific:** Each space only *adds* the thing that's its job to add.
  The wizard space adds the wizard's reply. The tools space adds tool results.
  Nobody rewrites old entries — the notebook only grows.

### One-paragraph summary

`agent.iter()` doesn't hand you a fully drawn map before you start. It hands
you a notebook (`agent_run`) and puts you on the first space. Each time you
ask `async for node in agent_run` for the next space, it actually plays out
the space you were just on — which is the moment the real work happens, via
`node.stream(agent_run.ctx)` — writes the result into the shared notebook, and
only THEN figures out and hands you the next space. This repeats, with the
notebook getting longer each time, until a space decides there's nothing more
to do and sends you to End.

---

## 6. The short version we landed on

The first try at a one-sentence summary was:

> All `iter` does is enable a stream in the form of `agent_run` that gets
> adjusted with a new node every iteration. Then for each node type, we
> handle things.

That is close. Three small fixes make it exact:

- `agent.iter()` does more than turn on a stream. It also creates the shared
  notebook (`agent_run.ctx`, mainly the message history) that every node
  reads and writes.
- The new node is not picked when you receive the current one. It is picked
  when the previous node actually runs, inside `node.stream(...)`.
  `async for` just hands you that just-decided node on the next pass.
- In the `ModelRequestNode` and `CallToolsNode` branches, calling
  `node.stream(agent_run.ctx)` is the real work: the HTTP call to Azure, or
  the tool call. The `UserPromptNode` branch only prints. `agent.iter` runs
  that node for you behind the scenes.

So the tightened version is:

> `agent.iter()` sets up one shared, growing notebook (`agent_run`) and starts
> the first node. Each pass of `async for node in agent_run` runs the node you
> are handling. That both does the real work (talking to the model, or calling
> tools) and decides what the next node is, then hands you that next node on
> the following pass. You branch on the node type to do the right thing
> (print, stream text, stream tool calls) until a node decides the answer is
> final and the loop ends.
