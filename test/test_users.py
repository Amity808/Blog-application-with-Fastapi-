import json
import os
import sys
from fastapi.testclient import TestClient

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app

client = TestClient(app)


def test_create_user():
    data = {
        'name': 'bolarinwavc',
        'email': 'bolarinwam@gmail.com',
        'password': 'bolarinwam'
    }
    response = client.post("/users/", json.dumps(data))

    assert response.status_code == 201
    assert response.json()
