import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

AUTH = ("admin", "admin123")

def test_create_age_group():
    response = client.post(
        "/age-groups",
        auth=AUTH,
        json={"name": "Teste", "min_age": 20, "max_age": 30}
    )
    assert response.status_code == 200
    data = response.json()
    assert "name" in data and data["name"] == "Teste"
    assert data["min_age"] == 20
    assert data["max_age"] == 30

def test_create_enrollment():
    response = client.post(
        "/enrollments",
        auth=AUTH,
        json={"name": "Carlos Teste", "cpf": "00011122233", "age": 25}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["cpf"] == "00011122233"
    assert data["status"] == "pending"

def test_get_enrollment():
    response = client.get(
        "/enrollments/00011122233",
        auth=AUTH
    )
    assert response.status_code == 200
    data = response.json()
    assert data["cpf"] == "00011122233"
    assert data["status"] in ["pending", "approved", "rejected"]
