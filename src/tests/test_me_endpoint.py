from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_me_endpoint_structure():
    response = client.get("/me")
    assert response.status_code == 200
    data = response.json()

    assert data["status"] == "success"
    assert "user" in data
    assert "email" in data["user"]
    assert "name" in data["user"]
    assert "stack" in data["user"]
    assert "timestamp" in data
    assert "fact" in data
