import os
import requests
from dotenv import load_dotenv

load_dotenv()

MODEL_NAME = os.getenv("MODEL_NAME", "qwen3.5:2b")
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/chat")

def call_llm(prompt: str) -> str:
    print(f"DEBUG: Entering call_llm(prompt={prompt})")
    """Sends the context to Ollama"""

    payload = {
        "model":MODEL_NAME,
        "messages": prompt,
        "stream" : False,
        "options": {
            "temperature": 0.0,
            "stop": ["Observation:", "\nObservation"]
        }
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        return response.json().get("message", {}).get("content", "")

    except Exception as e:
        return f"Error communicating with Ollama: {e}"
