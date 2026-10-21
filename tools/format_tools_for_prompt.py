import inspect

def format_tools_for_prompt(tool_registry: dict) -> str:
    print(f"DEBUG: Entering format_tools_for_prompt(tool_registry={tool_registry})")

    tool_descriptions = []
    for name, func in tool_registry.items():

        sig = inspect.signature(func)

        doc = inspect.getdoc(func) or "No Description"

        tool_descriptions.append(f"- {name}{sig}: {doc}")

    return "\n".join(tool_descriptions)
        
