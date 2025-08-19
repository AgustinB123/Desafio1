from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/api/health")
    assert r.status_code == 200
    assert r.json()["ok"] is True

def test_time_endpoint():
    r = client.get("/api/time")
    data = r.json()
    assert r.status_code == 200
    assert "iso" in data and isinstance(data["iso"], str)
    assert "epoch_ms" in data and isinstance(data["epoch_ms"], int)
    assert "timezone" in data and isinstance(data["timezone"], str)