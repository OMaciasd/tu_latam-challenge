import pytest
from app.app import app


@pytest.fixture
def client():
    """Configure client Flask App test."""
    with app.test_client() as client:
        yield client


def test_homepage(client):
    """Test Web init."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, World!' in response.data
