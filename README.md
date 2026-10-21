# System Diagnostics Agent

## Overview

This repository contains a practice project focused on building an AI Agent from scratch using **vanilla Python**. The implementation is based on the concepts taught in **Unit 1 of the Hugging Face AI Agents Course**.

The goal of the project is to build a functional, autonomous Windows System Helper / Diagnostics Agent without using external high-level agent frameworks (such as LangChain, CrewAI, or AutoGen). The agent can inspect system metrics (CPU, RAM, disk space), list running processes sorted by resource consumption, and execute actions such as terminating a specified process by PID.

---

## Key Concepts Applied from Hugging Face AI Agents Course (Unit 1)

### 1. ReAct Pattern (Reasoning and Acting)
The agent follows the classic **ReAct** (Thought -> Action -> Observation) iterative loop:
- **Thought**: The LLM reasons about the user request and current state to decide what diagnostic step to take next.
- **Action**: The LLM outputs a structured tool call in JSON format.
- **Observation**: The agent framework executes the requested tool locally and appends the result back into the message history for the LLM.
- **Final Answer**: When sufficient information is gathered, the LLM provides the final summary and completes the loop.

### 2. Custom Tool Registration and Inspection
- Tools are standard Python functions (`get_system_metrics`, `get_process_metrics`, `kill_process`).
- Tool documentation and signatures are dynamically extracted at runtime using Python's native `inspect` module (`inspect.signature` and `inspect.getdoc`).
- Tools are registered in a `TOOL_REGISTRY` dictionary for execution mapping.

### 3. Dynamic System Prompt Assembly
The system prompt dynamically formats tool definitions into the prompt instructions, guiding the LLM on how to format its thoughts and actions.

### 4. Local LLM Integration via API
Interaction with the local LLM is handled directly using HTTP POST requests to Ollama's `/api/chat` endpoint, managed with configuration parameters loaded from environment files.

---

## Project Structure

```
System Diagnostics Agent/
├── main.py                     # Entry point of the application
├── .env                        # Environment configuration file
├── .gitignore                  # Git ignore rules
├── requirements.txt            # Python dependencies
├── tools/
│   ├── format_tools_for_prompt.py  # Formats function docstrings and signatures into prompt strings
│   ├── read/
│   │   ├── get_system_metrics.py   # Tool: retrieves CPU, RAM, and Disk metrics
│   │   └── get_process_metrics.py  # Tool: lists and sorts system processes by resource usage
│   └── execute/
│       └── kill_process.py        # Tool: terminates a process by PID using psutil
└── utils/
    ├── call_llm.py             # Communication handler for Ollama API
    ├── execute_tool_call.py    # Tool invocation and response string formatting
    ├── run_agent.py            # ReAct loop execution engine
    └── system_prompt.py       # Prompt templates and dynamic tool assembly
```

---

## Environment Variables (.env)

The project uses `python-dotenv` to manage configuration parameters. The `.env` file should be located in the project directory:

```env
MODEL_NAME=qwen3.5:2b
OLLAMA_URL=http://localhost:11434/api/chat
```

### Parameter Description

| Parameter | Description | Default Value |
| --- | --- | --- |
| `MODEL_NAME` | Name of the LLM model hosted in Ollama | `qwen3.5:2b` |
| `OLLAMA_URL` | Endpoint URL for the local Ollama chat API | `http://localhost:11434/api/chat` |

---

## Installation and Setup

1. **Navigate to the project directory:**
   ```bash
   cd "System Diagnostics Agent"
   ```

2. **Set up a Python virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/Scripts/activate  # On Windows (Git Bash)
   # or
   .venv\Scripts\activate          # On Windows (CMD / PowerShell)
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Ensure Ollama is running locally:**
   Make sure Ollama is installed and running with your configured model:
   ```bash
   ollama run qwen3.5:2b
   ```

5. **Run the Agent:**
   ```bash
   python main.py
   ```
