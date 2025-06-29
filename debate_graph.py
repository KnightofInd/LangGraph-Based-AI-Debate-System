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
    graph.add_node("Judge", judge_node)
    graph.add_node("Memory", memory_node)

    # Logic for routing based on round number
    def route_step(state: DebateState) -> str:
        if state["round"] >= ROUNDS:
            return "Judge"
        return "Researcher" if state["round"] % 2 == 1 else "Engineer"

    # Connect Memory to the right node based on round
    graph.add_conditional_edges("Memory", route_step, {
        "Researcher": "Researcher",
        "Engineer": "Engineer",
        "Judge": "Judge"
    })

    # Back-edges to return to Memory
    graph.add_edge("Researcher", "Memory")
    graph.add_edge("Engineer", "Memory")
    graph.add_edge("Judge", END)

    # Entry point
    graph.set_entry_point("Memory")

    # Compile
    debate = graph.compile()

    # Run the debate and get final state
    result = debate.invoke(state)

    # ✅ Manually generate DAG diagram


    # Print results
    print("\n🧾 Debate Finished!")
    print(f"\n🏆 Winner: {result['winner']}")
    print(f"\n🧠 Reasoning: {result['reason']}")

    # Save transcript and result to file
    log_debate(result)
    generate_dag_diagram()

# 🔧 DAG diagram using graphviz (pure Python, no pygraphviz)
def generate_dag_diagram():
    G = nx.DiGraph()

    # Nodes
    G.add_node("UserInput")
    G.add_node("Memory_1")
    G.add_node("Researcher")
    G.add_node("Memory_2")
    G.add_node("Engineer")
    G.add_node("Memory_3")
    G.add_node("Judge")
    G.add_node("END")

    # Edges for 2-round structure
    G.add_edge("UserInput", "Memory_1")
    G.add_edge("Memory_1", "Researcher")
    G.add_edge("Researcher", "Memory_2")
    G.add_edge("Memory_2", "Engineer")
    G.add_edge("Engineer", "Memory_3")
    G.add_edge("Memory_3", "Judge")
    G.add_edge("Judge", "END")

    # Position nodes neatly
    pos = {
        "UserInput": (0, 4),
        "Memory_1": (2, 4),
        "Researcher": (4, 5),
        "Memory_2": (6, 4),
        "Engineer": (8, 3),
        "Memory_3": (10, 2),
        "Judge": (12, 1),
        "END": (14, 0),
    }

    # Plotting
    plt.figure(figsize=(12, 6))
    nx.draw_networkx_nodes(G, pos, node_size=2500, node_color="#B0E0E6")
    nx.draw_networkx_edges(G, pos, arrowstyle="->", arrowsize=20)
    nx.draw_networkx_labels(G, pos, font_size=10, font_weight="bold")

    # Save the plot
    os.makedirs("exports", exist_ok=True)
    plt.title("LangGraph Debate Flow (2 Rounds)", fontsize=14)
    plt.axis("off")
    plt.tight_layout()
    plt.savefig("exports/dag_diagram.png")
    plt.close()
