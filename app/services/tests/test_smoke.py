from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health():
    response = client.get("/api/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_market():
    response = client.get("/api/market/spx")

    assert response.status_code == 200
    assert response.json()["symbol"] == "SPX"
