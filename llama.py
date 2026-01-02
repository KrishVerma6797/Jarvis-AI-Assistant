from llama_cpp import Llama
from datetime import datetime
import os
import json

# ================== CONFIG ==================
MODEL_PATH = os.getenv("LLAMA_MODEL_PATH")

if not MODEL_PATH or not os.path.exists(MODEL_PATH):
    raise FileNotFoundError(
        "LLAMA_MODEL_PATH is not set or model file not found."
    )

# ================== LOAD MODEL ==================
llm = Llama(
    model_path=MODEL_PATH,
    n_ctx=4096,
    n_threads=8,
    n_gpu_layers=0,  # CPU mode
    verbose=False
)

# ================== MAIN FUNCTION ==================
def ask_llama(user_input: str) -> str:
    if not user_input.strip():
        return ""

    system_prompt = (
        "You are Jarvis, a helpful voice assistant. "
        "Give short, clear, direct answers. "
        "Do not repeat the question."
    )

    prompt = f"""
<start_of_turn>system
{system_prompt}
<end_of_turn>
<start_of_turn>user
{user_input}
<end_of_turn>
<start_of_turn>assistant
"""

    try:
        result = llm(
            prompt,
            max_tokens=80,
            temperature=0.3,
            top_p=0.9,
            stop=["<end_of_turn>"]
        )

        return result["choices"][0]["text"].strip()

    except Exception:
        return "Sorry, I couldn't process that request."


# ================== LOGGING ==================
def log_interaction(prompt, response, log_file="jarvis_log.json"):
    entry = {
        "timestamp": datetime.now().isoformat(),
        "prompt": prompt,
        "response": response
    }

    try:
        if os.path.exists(log_file):
            with open(log_file, "r", encoding="utf-8") as f:
                logs = json.load(f)
        else:
            logs = []

        logs.append(entry)

        with open(log_file, "w", encoding="utf-8") as f:
            json.dump(logs, f, indent=4)

    except:
        pass
