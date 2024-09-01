import pytest
from unittest.mock import patch
from app.app import app, create_rabbitmq_connection

@pytest.fixture
def client():
    """Configure client Flask App test."""
    with app.test_client() as client:
        yield client

@patch('app.app.create_rabbitmq_connection')
def test_homepage(mock_create_rabbitmq_connection, client):
    """Test Web init with RabbitMQ connection mocked."""
    mock_create_rabbitmq_connection.return_value = (None, None)
    
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hello, World!' in response.data
