import pytest
import requests


class MockResponse:
    """Requests.get() mocked to return."""

    def __init__(self, status_code: int, data: dict):
        self.status_code = status_code
        self.data = data

    @property
    def ok(self):
        if self.status_code == 200:
            return True

    def json(self):
        return self.data

@pytest.fixture
def mock_response_api__jikan_v4_anime__fail(monkeypatch):

    def mock_get(*args, **kwargs):
        return MockResponse(
            status_code=400,
            data=None,
        )

    monkeypatch.setattr(requests, "get", mock_get)    

@pytest.fixture
def mock_response_api__jikan_v4_anime__success(monkeypatch):

    def mock_get(*args, **kwargs):
        return MockResponse(
            status_code=200,
            data={
                "data": [
                    {"title": "Title A", "url": "https://example.com/title-a"},
                    {"title": "Title B", "url": "https://example.com/title-b"}
                ]
            },
        )

    monkeypatch.setattr(requests, "get", mock_get)