import pytest
from fastapi.testclient import TestClient

from src.main import main


@pytest.fixture(name="client", scope="function")
def get_client():
    return TestClient(main())
