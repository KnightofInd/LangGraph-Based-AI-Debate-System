# LangGraph-Based AI Debate System

A sophisticated command-line AI debate system built with LangGraph that orchestrates structured debates between two specialized AI agents: a Researcher and an Engineer. The system manages memory, enforces turn-taking, and provides impartial judgment using Google's Gemini API.

## 🎯 Project Overview

This system creates engaging debates by having two AI agents with distinct personalities argue different perspectives on user-provided topics. The debate follows a structured 2-round format with memory management and concludes with an AI judge evaluating the arguments.

## 🏗️ System Architecture

```mermaid
graph TB
    A[User Input] --> B[Memory Node]
    B --> C{Route Decision}
    C -->|Round 0 - Even| D[Engineer Agent]
    C -->|Round 1 - Odd| E[Researcher Agent]
    C -->|Round >= 2| F[Judge Agent]
    D --> G[Memory Update]
    E --> H[Memory Update]
    G --> I{Continue?}
    H --> I
    I -->|Yes| B
    I -->|No| F
    F --> J[END - Results]
    
    style A fill:#e1f5fe
    style D fill:#f3e5f5
    style E fill:#e8f5e8
    style F fill:#fff3e0
    style J fill:#ffebee
```

## 🔄 Debate Flow

```mermaid
sequenceDiagram
    participant U as User
    participant M as Memory
    participant E as Engineer
    participant R as Researcher
    participant J as Judge
    participant L as Logger

    U->>M: Enter debate topic
    M->>E: Round 0 (Engineer starts)
    E->>M: Practical argument
    M->>R: Round 1 (Researcher responds)
    R->>M: Academic argument
    M->>J: All rounds complete
    J->>J: Evaluate arguments
    J->>L: Log final decision
    J->>U: Declare winner with reasoning
```

## 🤖 Agent Personalities

```mermaid
mindmap
  root((AI Agents))
    Engineer
      Practical
      Solution-oriented
      Technical focus
      "In practice..."
      "From experience..."
    Researcher
      Academic
      Evidence-based
      Theoretical
      "Studies show..."
      "Evidence suggests..."
    Judge
      Impartial
      Logical analysis
      Clear reasoning
      Winner declaration
```

## 🧠 Memory Management

```mermaid
graph LR
    A[New Argument] --> B[Memory Node]
    B --> C[Update State]
    C --> D[Agent History]
    C --> E[Opponent's Last Argument]
    D --> F[Current Agent]
    E --> F
    F --> G[Generate Response]
    G --> A
    
    style B fill:#e3f2fd
    style F fill:#f1f8e9
```

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- Gemini API key from Google AI Studio

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd LangGraph-Based-AI-Debate-System
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

### Running the System

```bash
python main.py
```

Follow the prompts to enter a debate topic and watch the AI agents engage in structured argumentation.

## 📁 Project Structure

```mermaid
graph TD
    A[LangGraph-Based-AI-Debate-System] --> B[main.py]
    A --> C[debate_graph.py]
    A --> D[gemini_api.py]
    A --> E[agents/]
    A --> F[utils/]
    A --> G[exports/]
    A --> H[debate_log.txt]
    
    E --> E1[researcher.py]
    E --> E2[engineer.py]
    E --> E3[judge.py]
    
    F --> F1[prompts.py]
    F --> F2[memory.py]
    F --> F3[logger.py]
    
    G --> G1[dag_diagram.png]
    
    style A fill:#e1f5fe
    style E fill:#f3e5f5
    style F fill:#e8f5e8
    style G fill:#fff3e0
```

## 🔧 Tech Stack

```mermaid
graph LR
    A[Python 3.10+] --> B[LangGraph]
    B --> C[LangChain]
    C --> D[Gemini API]
    D --> E[NetworkX]
    E --> F[Matplotlib]
    F --> G[Graphviz]
    
    style A fill:#306998
    style B fill:#326ce5
    style C fill:#1c4587
    style D fill:#4285f4
    style E fill:#ff6d01
    style F fill:#11557c
    style G fill:#2e8b57
```

## 🎭 Agent Implementation Details

### Researcher Agent
- **File**: [`agents/researcher.py`](agents/researcher.py)
- **Style**: Formal, academic, evidence-based
- **Language Patterns**: "Studies show...", "Evidence suggests...", "From a theoretical perspective..."
- **Focus**: Long-term effects, theoretical risks, scholarly research

### Engineer Agent  
- **File**: [`agents/engineer.py`](agents/engineer.py)
- **Style**: Practical, solution-oriented, technical
- **Language Patterns**: "In practice...", "From experience...", "Technically speaking..."
- **Focus**: Implementation feasibility, real-world constraints, practical solutions

### Judge Agent
- **File**: [`agents/judge.py`](agents/judge.py)
- **Role**: Impartial evaluator using [`utils/prompts.py`](utils/prompts.py)
- **Criteria**: Logical strength, consistency, clarity of arguments
- **Output**: Winner declaration with detailed justification

## 🔄 System Workflow

The main workflow is orchestrated by [`debate_graph.py`](debate_graph.py):

1. **Initialization**: User enters topic via [`main.py`](main.py)
2. **Memory Management**: [`utils/memory.py`](utils/memory.py) maintains state
3. **Agent Routing**: Round-based routing (Engineer → Researcher → Judge)
4. **API Integration**: [`gemini_api.py`](gemini_api.py) handles Gemini API calls
5. **Logging**: [`utils/logger.py`](utils/logger.py) saves results to [`debate_log.txt`](debate_log.txt)
6. **Visualization**: Auto-generates DAG diagram in [`exports/dag_diagram.png`](exports/dag_diagram.png)

## 📊 State Management

```mermaid
classDiagram
    class DebateState {
        +str topic
        +int round
        +List~Dict~ memory
        +List~str~ log
        +str winner
        +str reason
    }
    
    class Agent {
        +agent_output: Dict
        +generate_response()
    }
    
    class Memory {
        +update_state()
        +get_history()
        +route_next()
    }
    
    DebateState --> Agent
    DebateState --> Memory
```

## 📈 Usage Examples

### Sample Topics
- "Should electric cars replace hybrid cars?"
- "Is remote work more productive than office work?"
- "Should AI development be regulated by government?"

### Output Format
```
🎤 Welcome to the AI Debate System!
Enter a topic for debate: Should electric cars replace hybrid cars?

🧠 Starting debate on: 'Should electric cars replace hybrid cars?'...

[Engineer - Round 0]
[Engineer's practical argument here]

[Researcher - Round 1]  
[Researcher's academic argument here]

[Judge Decision]
[Judge's evaluation and winner declaration]

🧾 Debate Finished!
🏆 Winner: [Winner]
🧠 Reasoning: [Detailed justification]
```

## 🔧 Key Features

### Memory Management
- **Selective Memory**: Agents receive only relevant context via [`utils/prompts.py`](utils/prompts.py)
- **History Tracking**: Full debate transcript maintained in [`utils/memory.py`](utils/memory.py)
- **Context Awareness**: Prevents argument repetition

### Workflow Orchestration
- **State Management**: Typed state schema with LangGraph in [`debate_graph.py`](debate_graph.py)
- **Conditional Routing**: Dynamic agent selection based on round number
- **DAG Visualization**: Automatic workflow diagram generation

### API Integration
- **Gemini Integration**: RESTful API calls via [`gemini_api.py`](gemini_api.py)
- **Error Handling**: Robust error management for API failures
- **Environment Security**: API keys managed through `.env` file

## 🎯 Future Enhancements

```mermaid
graph TB
    A[Current System] --> B[Extended Rounds]
    A --> C[Multiple Topics]
    A --> D[Agent Customization]
    A --> E[Web Interface]
    A --> F[Export Options]
    
    B --> B1[Configurable debate length]
    C --> C1[Multi-topic debates]
    D --> D1[User-defined personalities]
    E --> E1[Browser-based viewing]
    F --> F1[PDF, JSON exports]
    
    style A fill:#e1f5fe
    style B fill:#f3e5f5
    style C fill:#e8f5e8
    style D fill:#fff3e0
    style E fill:#ffebee
    style F fill:#f1f8e9
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **Google Gemini API** for providing the language model capabilities
- **LangGraph Team** for the excellent workflow orchestration framework
- **LangChain Community** for agent development tools

---