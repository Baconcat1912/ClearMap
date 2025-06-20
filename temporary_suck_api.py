from together import Together


def get_ai_response(message: str) -> str:
    """Send a chat message to Together AI and return the response."""
    api_key = "775cefd068e94367678bd64a998e8f778c2297c86ce4aa13fb3ccf0c02ae096c"
    #hardcoding that is stupid but I dont rlly care....
    if not api_key:
        return f"You said: {message} (no AI key configured)"
    client = Together(api_key=api_key)
    try:
        response = client.chat.completions.create(
            model="deepseek-ai/DeepSeek-R1-Distill-Llama-70B-free",
            messages=[{"role": "user", "content": message}],
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error contacting AI service: {e}"