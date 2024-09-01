import pytest
from unittest.mock import patch

from app.app import app

@pytest.fixture
def client():
    """Configura el cliente de prueba para la aplicación Flask."""
    with app.test_client() as client:
        yield client

@patch('app.app.create_rabbitmq_connection')
def test_homepage(mock_create_rabbitmq_connection, client):
    """Test inicial de la web con la conexión RabbitMQ mockeada."""
    mock_create_rabbitmq_connection.return_value = (None, None)
    
    response = client.get('/')
    
    assert response.status_code == 200
    assert b'Hello, World!' in response.data
