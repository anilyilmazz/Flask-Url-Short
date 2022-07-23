import json

from ..source import create_app
import pytest

@pytest.fixture
def app():
    app = create_app("test")
    return app

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

def test_url_list(client):
    response = client.get("/")
    assert response.status == 200
    assert isinstance(response.data, list)

def test_create_url(client):
    new_url_data = {
        'url': "https://www.google.com/",
    }
    response = client.post("/", data=json.dumps(new_url_data))
    assert response.status == 200
    assert isinstance(response.data, dict)
