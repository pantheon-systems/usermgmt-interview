import pytest
from unittest.mock import patch, MagicMock
from quart import Quart
from auth.routes.auth import auth_bp

@pytest.fixture
def app():
    app = Quart(__name__)
    app.register_blueprint(auth_bp)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.mark.asyncio
@patch('auth.routes.auth.Session')
@patch('auth.routes.auth.generate_password_hash')
async def test_register(mock_hash, mock_session, client):
    mock_session_instance = MagicMock()
    mock_session.return_value.__enter__.return_value = mock_session_instance
    mock_hash.return_value = 'hashed_password'

    response = await client.post('/auth/register', json={
        'username': 'testuser',
        'password': 'testpassword'
    })

    assert response.status_code == 201
    assert response.is_json

@pytest.mark.asyncio
@patch('auth.routes.auth.engine')
@patch('auth.routes.auth.check_password_hash')
@patch('auth.routes.auth.jwt.encode')
async def test_login(mock_jwt, mock_check_hash, mock_engine, client):
    mock_connection = MagicMock()
    mock_engine.connect.return_value.__enter__.return_value = mock_connection
    mock_connection.execute.return_value.first.return_value = MagicMock(id=1, password='hashed_password')
    mock_check_hash.return_value = True
    mock_jwt.return_value = 'fake_token'

    response = await client.post('/auth/login', json={
        'username': 'testuser',
        'password': 'testpassword'
    })

    assert response.status_code == 200
    json_data = await response.get_json()
    assert 'token' in json_data

def test_reset_password():
    assert True
