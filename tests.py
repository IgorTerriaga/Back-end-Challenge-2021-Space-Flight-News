from main import app
from starlette.testclient import TestClient



client = TestClient(app)


def test_welcome_code():
    response = client.get("/")
    assert response.status_code == 200


def test_welcome_response():
    response = client.get("/")
    assert response.json() == {
        "menssagem": "Back-end Challenge 2021 🏅 - Space Flight News"
    }
