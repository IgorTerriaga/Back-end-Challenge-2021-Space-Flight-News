from itsdangerous import json
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


def test_postArticles_response_code():
    response = client.post(
        "/articles/",
        headers={"Content-Type": "application/json"},
        json={
            "featured": False,
            "title": "Flight 4",
            "url": "Flight 1",
            "imageUrl": "Flight 1",
            "newsSite": "Flight 1",
            "summary": "Flight 1",
            "publishedAt": "Flight 1",
        },
    )
    assert response.status_code == 200


def test_putArticles_response_code():
    response = client.put(
        "/articles/7",
        headers={"Content-Type": "application/json"},
        json={"featured": True, "title": "Flight 1"},
    )
    assert response.status_code == 200


def test_article_does_not_exist():
    response = client.get("/articles/1", headers={"Content-Type": "application/json"})
    assert response.status_code == 404
    assert response.json() == {"detail": "Artigo não  encontrado"}
