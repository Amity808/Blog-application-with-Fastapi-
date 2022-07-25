import json
import os
import sys

from routers.oauth2 import get_current_user
import pytest
from fastapi.testclient import TestClient

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app

client = TestClient(app)


@pytest.fixture
def client():
    """
    Return an API Client
    """
    app.dependency_overrides = {}
    return TestClient(app)


@pytest.fixture
def client_authenticated():
    """
    Returns an API client which skips the authentication
    """

    def skip_auth():
        pass

    app.dependency_overrides[get_current_user] = skip_auth
    return TestClient(app)


def test_create_blog(client_authenticated):
    data = {
        "title": "Sodiqs", "body": "thisss"
    }
    response = client_authenticated.post("/blog", json.dumps(data), headers={"Authorization": "Bearer"})
    assert response.status_code == 201
    assert response.json() == data
