# NexusFlow-AI 🧠⚡

**NexusFlow-AI** is a **Self-Optimizing Visual Agent Builder for Embodied Codebase Operations**.

Inspired by the best features of:
- **Langflow** (Visual building)
- **Repomix** (Codebase packing for context)
- **TensorZero** (Optimization loops)
- **Genesis** (Embodied action paradigms)

## 🚀 Mission
To create an AI system that doesn't just "chat" about code, but **navigates, visualizes, and physically evolves** codebases through a self-improving agentic workflow.

## 🌟 Key Features

### 1. 📦 Context Packing Engine
Built-in "Repomix-lite" engine that turns entire GitHub repositories or local directories into optimized XML/JSON context prompts for LLMs, handling token limits automatically.

### 2. 🎨 Visual Agent Orchestrator
Drag-and-drop (simulated in v1) interface to chain multiple agents:
- **Architect Agent**: Plans structure.
- **Coder Agent**: Implements files.
- **Reviewer Agent**: Critiques and loops back.

### 3. 🔄 Self-Optimization Loop
Agents track their success rates (e.g., successful compilation, passing tests) and **rewrite their own system prompts** to improve performance over time.

### 4. 🛠️ Embodied File Operations
Direct integration with the file system to Create, Read, Update, and Delete files, not just output text.

## 🏗️ Architecture

```mermaid
graph TD
    User[User] --> UI[Streamlit UI]
    UI --> Packer[Context Packer Module]
    UI --> VisualBuilder[Agent Builder]
    VisualBuilder --> Engine[Execution Engine]
    Packer --> Engine
    Engine --> LLM[LLM Interface (OpenAI/Anthropic)]
    Engine --> FS[File System]
    FS --> Feedback[Feedback Loop]
    Feedback --> Optimizer[Prompt Optimizer]
    Optimizer --> Engine
```

## 💻 Tech Stack
- **Python 3.10+**
- **Streamlit**: For the interactive UI.
- **LangChain Core**: For prompt management.
- **NetworkX**: For managing the agent graph dependencies.
- **Pydantic**: For robust data validation.

## 🏃‍♂️ Getting Started

### Installation
```bash
git clone https://github.com/arturwyroslak/nexus-flow-ai.git
cd nexus-flow-ai
pip install -r requirements.txt
```

### Usage
```bash
streamlit run app.py
```
