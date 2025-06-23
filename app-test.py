"""Minimal Flask application used for manual testing."""

from __future__ import annotations

import os
from flask import Flask, jsonify, render_template, request
from temporary_suck_api import get_ai_response

app = Flask(__name__)


@app.route("/")
def index() -> str:
    """Render the chat UI."""
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat() -> tuple:
    """Handle a chat message from the client."""
    data = request.get_json(silent=True) or {}
    user_message = data.get("message")
    if not user_message:
        return jsonify({"error": "Missing message"}), 400

    ai_response = get_ai_response(user_message)
    return jsonify({"reply": ai_response}), 200


if __name__ == "__main__":
    debug = os.getenv("FLASK_DEBUG", "false").lower() == "true"
    app.run(debug=debug, host="0.0.0.0", port=8000, use_reloader=debug)

