from fastapi.testclient import TestClient

from main import app


def test_search__success(mock_response_api__jikan_v4_anime__success):
    client = TestClient(app)
    response = client.get("/anime", params=[("q", "some-text")])

    assert response.status_code == 200
    assert response.json() == {
            "count": 2,
            "results": [
                {"title": "Title A", "url": "https://example.com/title-a"},
                {"title": "Title B", "url": "https://example.com/title-b"}
            ],
        }

def test_search__fail(mock_response_api__jikan_v4_anime__fail):
    client = TestClient(app)
    response = client.get("/anime", params=[("q", "some-text")])

    assert response.status_code == 200
    assert response.json() == {
            "count": 0,
            "results": [],
        }

def test_search__invalid_parameters():
    client = TestClient(app)
    response = client.get("/anime", params=[("q", "")])

    assert response.status_code == 422
