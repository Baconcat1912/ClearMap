"""Utility helpers for communicating with Together AI."""

from __future__ import annotations

import os
from together import Together


def get_ai_response(message: str) -> str:
    """Send a chat message to Together AI and return the response."""
    api_key = os.getenv("TOGETHER_API_KEY")
    if not api_key:
        return f"You said: {message} (no AI key configured)"

    client = Together(api_key=api_key)
    try:
        response = client.chat.completions.create(
            model="deepseek-ai/DeepSeek-R1-Distill-Llama-70B-free",
            messages=[{"role": "user", "content": message}],
        )
        return response.choices[0].message.content
    except Exception as exc:  # pragma: no cover - network errors are difficult to test
        return f"Error contacting AI service: {exc}"

