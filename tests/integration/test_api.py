import pytest
from fastapi.testclient import TestClient
from scr.interfaces.api import app

client = TestClient(app)


def test_analyze_success():
    payload = {"text": "This is a wonderful and amazing day!"}
    response = client.post("/analyze", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert "text" in data
    assert "polarity" in data
    assert "subjectivity" in data
    assert data["text"] == payload["text"]
    assert isinstance(data["polarity"], float)


def test_analyze_empty_text_error():
    payload = {"text": ""}
    response = client.post("/analyze", json=payload)
    assert response.status_code == 422


def test_analyze_whitespace_text_error():
    payload = {"text": "   "}
    response = client.post("/analyze", json=payload)
    assert response.status_code == 400
    assert response.json()["detail"] == "Text cannot be empty"


def test_analyze_batch_success():
    payload = {
        "texts": [
            "I love python",
            "This is neutral"
        ]
    }
    response = client.post("/analyze-batch", json=payload)

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 2
    assert data[0]["text"] == "I love python"


def test_analyze_batch_empty_list_error():
    payload = {"texts": []}
    response = client.post("/analyze-batch", json=payload)
    assert response.status_code == 422


def test_analyze_batch_whitespace_error():
    payload = {
        "texts": ["Valid text", "   "]
    }
    response = client.post("/analyze-batch", json=payload)

    assert response.status_code == 400
    assert response.json()["detail"] == "Texts cannot contain empty strings"
