from fastapi.testclient import TestClient

from jetpack_api.main import app


client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_status() -> None:
    response = client.get("/api/v1/status")

    assert response.status_code == 200
    assert response.json()["stage"] == "project-initialized"

