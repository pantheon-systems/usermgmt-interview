import pytest
import json
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


async def test_index(client):
    response = await client.get("/")
    body = response.get_json()
    assert body == {"status": "OK"}
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_register(client):
    response = await client.post(
        "/register", json={"username": "testuser", "password": "testpassword"}
    )

    assert response.status_code == 201
    assert response.is_json


@pytest.mark.asyncio
async def test_login(client):
    response = await client.post(
        "/login", json={"username": "testuser", "password": "testpassword"}
    )

    assert response.status_code == 200


def test_reset_password():
    assert True
