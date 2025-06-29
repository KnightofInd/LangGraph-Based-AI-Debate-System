# utils/prompts.py

def get_last_opponent_argument(memory, agent_name):
    for item in reversed(memory):
        if item["agent"] != agent_name:
            return item["text"]
    return ""

def get_agent_history(memory, agent_name):
    return [item["text"] for item in memory if item["agent"] == agent_name]

def get_researcher_prompt(topic, memory):
    last_engineer = get_last_opponent_argument(memory, "Researcher")
    history = get_agent_history(memory, "Researcher")

    prompt = f"""You are an academic Researcher debating with a practical Engineer.

Debate Topic: "{topic}"

Your role: Provide a formal, evidence-based academic argument. Refer to studies, theoretical risks, long-term effects, etc.

Guidelines:
- Do NOT repeat past points
- Do NOT break character
- Use formal academic language
- Use phrases like "Studies show", "Evidence suggests", "From a theoretical perspective"

Your past arguments:
{" | ".join(history) if history else "None yet"}

Last statement by Engineer:
"{last_engineer}"

Respond academically and persuasively with a NEW point:
"""
    return prompt


def get_engineer_prompt(topic, memory):
    last_researcher = get_last_opponent_argument(memory, "Engineer")
    history = get_agent_history(memory, "Engineer")

    prompt = f"""You are a practical Engineer debating with an academic Researcher.

Debate Topic: "{topic}"

Your role: Provide a real-world, solution-oriented argument. Talk about feasibility, implementation, costs, and pragmatic decisions.

Guidelines:
- Do NOT repeat past points
- Do NOT break character
- Use practical, technical, or industry-based logic
- Use phrases like "In practice", "From experience", "Technically speaking"

Your past arguments:
{" | ".join(history) if history else "None yet"}

Last statement by Researcher:
"{last_researcher}"

Respond pragmatically with a NEW point:
"""
    return prompt


def get_judge_prompt(topic, memory):
    dialogue = "\n".join([f"{m['agent']}: {m['text']}" for m in memory])

    prompt = f"""You are an impartial Judge evaluating a debate between a Researcher and an Engineer.

Debate Topic: "{topic}"

Instructions:
- Read the debate transcript
- Analyze logical strength, consistency, clarity
- Choose a winner
- Justify your decision

Debate Transcript:
{dialogue}

Now, summarize the debate briefly and declare the winner.
"""
    return prompt
