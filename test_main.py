from fastapi.testclient import TestClient
from main import app
import pytest

client = TestClient(app)

def test_shorten_and_redirect():
    # 1) Shorten a URL
    response = client.post("/shorten", json={"url": "https://www.example.com"})
    assert response.status_code == 200
    data = response.json()
    assert "short_url" in data

    short_url = data["short_url"]
    slug = short_url.rsplit("/", 1)[-1]

    # 2) GET the slug
    redirect_response = client.get(f"/{slug}", follow_redirects=False)
    assert redirect_response.status_code == 307
    assert redirect_response.headers["location"] == "https://www.example.com"
