import io, re
from io import BytesIO
import streamlit as st
from huggingface_hub import InferenceClient
import config

from groq import generate_response

MATH_SYSTEM = """You are a Math Mastermind.
Solve with clear step-by-step reasoning, correct notation, and a final answer.
Verify when possible; mention an alternative method briefly if relevant. """

CHAT_CSS = """
<style>
.wrap {max-height: 520px; overflow-y: auto; padding-right: 6px;}
.cardborder:1px solid #e6e6e6;background#fff;border-radius;10px;padding:14px 16px;margin:10px 0;
box-shadow:0 1px 2px rgba(0, 0, 0, 0.04);
.q{font-weight:inline-block;background:#FF9800;color:#fff;padding:2px 8px;border-radis:12px;font-
size:12px;margin-left:8px}
</style>
"""

def export_txt(history):
    txt = "".join([f"Q{i}: {h['question']}\nA{i}: {h['answer']}\n\n" for i, h in enumerate(history, 1)])
    bio = io.BytesIO(txt.encode("utf-8")); bio.seek(0); return bio

def teaching_answe(q: str) ->str:
    return generate_response(q, temperature=0.3, max_tokens=1024)

def math_answer(q: str, level: str) -> str:
    prompt = f"{MATH_SYSTEM}\n\nDifficulty: {level}\nMath Problem: {q}"
    return generate_response(prompt, temperature=0.1, max_tokens=1024)
def
