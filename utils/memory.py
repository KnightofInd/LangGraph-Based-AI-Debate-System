def memory_node(state):
    memory = state.get("memory", [])
    agent_output = state.get("agent_output")
    round_no = state["round"]

    if agent_output:
        memory.append(agent_output)

    return {
        "memory": memory,
        "round": round_no + 1
    }
