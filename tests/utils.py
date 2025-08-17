import pytest

from src.main import app


def resolve_url(name: str, **kwargs):
    return app.url_path_for(name, **kwargs)


MOCK_DT = "2025-08-17T14:35:22+00:00"


class TestClientMixin:

    STATUS_OK = 200
    STATUS_CREATED = 201

    @pytest.fixture(autouse=True)
    def _setup(self, client):
        self.client = client
