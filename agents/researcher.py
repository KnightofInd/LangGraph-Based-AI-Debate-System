# agents/researcher.py
from gemini_api import query_gemini
from utils.prompts import get_researcher_prompt

def researcher_node(state):
    topic = state["topic"]
    memory = state.get("memory", [])
    round_no = state["round"]

    prompt = get_researcher_prompt(topic, memory)
    response = query_gemini(prompt)

    print(f"[Researcher - Round {round_no}]")
    print(response + "\n")

    return {
        "agent_output": {
            "agent": "Researcher",
            "text": response
        }
    }
