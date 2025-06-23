import requests


def main():
    """Simple helper script to exercise the FastAPI endpoints."""
    # Test GET /ping/
    response = requests.get("http://127.0.0.1:8000/ping/")
    print(response.json())  # {"status": "alive", "message": "API is running!"}

    # Test POST /echo/
    test_data = {"key": "value", "test": True}
    response = requests.post(
        "http://127.0.0.1:8000/echo/",
        json=test_data,
    )
    print(response.json())


if __name__ == "__main__":
    main()
