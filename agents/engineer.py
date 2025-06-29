# agents/engineer.py
from gemini_api import query_gemini
from utils.prompts import get_engineer_prompt

def engineer_node(state):
    topic = state["topic"]
    memory = state.get("memory", [])
    round_no = state["round"]

    prompt = get_engineer_prompt(topic, memory)
    response = query_gemini(prompt)

    print(f"[Engineer - Round {round_no}]")
    print(response + "\n")

    return {
        "agent_output": {
            "agent": "Engineer",
            "text": response
        }
    }

