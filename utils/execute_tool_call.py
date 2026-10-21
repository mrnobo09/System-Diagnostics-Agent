import json
from tools.read import (
    get_system_metrics,
    get_process_metrics
)
from tools.execute   import (
    kill_process
)
TOOL_REGISTRY = {
    "get_system_metrics": get_system_metrics,
    "get_process_metrics": get_process_metrics,
    "kill_process":kill_process
}

def execute_tool_call(action_str:str) -> str:
    print(f"DEBUG: Entering execute_tool_call(action_str={action_str})")
    try:
        data = json.loads(action_str.strip())
        func_name = data.get("tool")
        kwargs = data.get("args", {})

        if func_name not in TOOL_REGISTRY:
            return f"Error: Tool '{func_name}' not found."

        result = TOOL_REGISTRY[func_name](**kwargs)

        return json.dumps(result,indent=2) if isinstance(result, (dict, list)) else str(result)
    except json.JSONDecodeError:
        return f"Error: Action must be valid JSON like {{\x22tool\x22: \x22name\x22, \x22args\x22: {{...}}}}"
    except Exception as e:
        return f"Tool Execution Error: {e}"

    

