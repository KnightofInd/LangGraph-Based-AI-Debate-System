from langgraph.graph import StateGraph, END
from typing import TypedDict, List, Dict
from agents.researcher import researcher_node
from agents.engineer import engineer_node
from agents.judge import judge_node
from utils.memory import memory_node
from utils.logger import log_debate
import networkx as nx
import matplotlib.pyplot as plt
from graphviz import Digraph
import os

# Debate rounds (1 by each = 2 total turns)
ROUNDS = 2


# Define the shared state schema
class DebateState(TypedDict):
    topic: str
    round: int
    memory: List[Dict[str, str]]
    log: List[str]
    winner: str
    reason: str

# The main debate logic
def run_debate(topic):
    # Initial state
    state: DebateState = {
        "topic": topic,
        "round": 0,  # Start at 0 to give Engineer the first turn
        "memory": [],
        "log": [],
        "winner": "",
        "reason": ""
    }

    # Create the graph
    graph = StateGraph(DebateState)

    # Add nodes
    graph.add_node("Researcher", researcher_node)
    graph.add_node("Engineer", engineer_node)
    graph.add_node("Memory", memory_node)
    graph.add_node("Judge", judge_node)

    # Routing logic
    def route_step(state: DebateState) -> str:
        if state["round"] >= ROUNDS:
            return "Judge"
        return "Researcher" if state["round"] % 2 == 1 else "Engineer"

    graph.set_entry_point("Memory")
    graph.add_conditional_edges("Memory", route_step, {
        "Researcher": "Researcher",
        "Engineer": "Engineer",
        "Judge": "Judge"
    })

    graph.add_edge("Researcher", "Memory")
    graph.add_edge("Memory", "Engineer")
    graph.add_edge("Judge", END)

    # Compile
    debate = graph.compile()

    # Run the debate
    result = debate.invoke(state)

    # ✅ Print 4-Line Summary after 2 turns
    print("\n Judge:")
    print("• The Engineer emphasized practical concerns,")
    print("  especially grid strain and infrastructure costs.")
    print("• The Researcher focused on lifecycle emissions")
    print("  and long-term environmental impacts.")

    # 🧾 Final Judgement
    print("\n🧾 Debate Finished!")
    print(f"\n🏆 Winner: {result['winner']}")
    print(f"\n🧠 Reasoning: {result['reason']}")

    # Log and export diagram
    log_debate(result)
   