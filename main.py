# main.py
from debate_graph import run_debate

def main():
    print("🎤 Welcome to the AI Debate System!")
    topic = input("Enter a topic for debate: ").strip()

    if not topic:
        print("❗ Please enter a valid topic.")
        return

    print(f"\n🧠 Starting debate on: '{topic}'...\n")
    run_debate(topic)

if __name__ == "__main__":
    main()
