from .system_prompt import SYSTEM_PROMPT
from .call_llm import call_llm
from .execute_tool_call import execute_tool_call

def run_agent(user_query:str,max_steps:int = 10):
    print(f"DEBUG: Entering run_agent(user_query={user_query}, max_steps={max_steps})")

    messages = [
        {"role":"system","content":SYSTEM_PROMPT},
        {"role":"user","content":user_query}
    ]

    for step in range(max_steps):

        response = call_llm(messages)

        print(response)

        if "Final Answer:" in response:
            print("\n Task Completed")
            return 

        messages.append({"role" : "assistant", "content": response})

        if "Action:" in response:
            action_part = response.split("Action:")[1].split("\n")[0].strip()

            observation = execute_tool_call(action_part)

            obs_str = f"Observation: {observation}"
            print(f"\n{obs_str}\n")
            
            messages.append({"role": "user", "content": obs_str})
        else:
            print("\n Error: Agent did not output a valid 'Action:' or 'Final Answer:'. Stopping loop.")
            break


