def collect_tools(messages):
    calls = []
    for message in messages:
        for part in message.parts:
            if part.part_kind == "tool-call":
                calls.append(f"{part.tool_name} {part.args}")
    return calls