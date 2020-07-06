import pytest
from app import app

# Docs
# https://flask.palletsprojects.com/en/1.1.x/testing/#the-first-test

# A fixture gives an object you can use within tests. Usually for data, it
# works well with the Flask testing client to test routes (shown here).
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

# Here we show tests for proper status codes and output (json for API)
def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.get_data().decode('utf-8') == 'Hello, World!' 


def test_api(client):
    response = client.get('/api')
    assert response.status_code == 200
    assert response.get_json()['hello'] == 'api'
