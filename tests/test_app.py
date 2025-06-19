import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import app
def test_index():
    client = app.app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b'AI Mind Map Placeholder' in response.data
