# agents/judge.py
from gemini_api import query_gemini
from utils.prompts import get_judge_prompt

def judge_node(state):
    topic = state["topic"]
    memory = state.get("memory", [])

    prompt = get_judge_prompt(topic, memory)
    response = query_gemini(prompt)

    print("[Judge Decision]")
    print(response + "\n")

    winner = "Draw"
    if "Researcher" in response and "Engineer" not in response:
        winner = "Researcher"
    elif "Engineer" in response and "Researcher" not in response:
        winner = "Engineer"

    return {
        "winner": winner,
        "reason": response
    }
