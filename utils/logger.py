# utils/logger.py
from datetime import datetime

def log_debate(state):
    log_path = "debate_log.txt"
    with open(log_path, "a", encoding="utf-8") as f:
        f.write("="*60 + "\n")
        f.write(f"🗓️  Debate Date: {datetime.now()}\n")
        f.write(f"🎯 Topic: {state['topic']}\n\n")

        for entry in state["memory"]:
            f.write(f"{entry['agent']}:\n{entry['text']}\n\n")

        f.write("🧠 Final Judgment:\n")
        f.write(f"🏆 Winner: {state['winner']}\n")
        f.write(f"📝 Reason: {state['reason']}\n")
        f.write("="*60 + "\n\n")

    print(f"📝 Debate transcript saved to {log_path}")
