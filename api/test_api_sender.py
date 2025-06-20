import requests

# Test GET /ping/
response = requests.get("http://127.0.0.1:8000/ping/")
print(response.json())  # Should return {"status": "alive", "message": "API is running!"}

# Test POST /echo/
test_data = {"key": "value", "test": True}
response = requests.post(
    "http://127.0.0.1:8000/echo/",
    json=test_data
)
print(response.json())  # Should echo back your data with a success message