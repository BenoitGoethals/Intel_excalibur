# tests/test_main.py
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Intel Excalibur API" in response.json()["message"]

def test_docs():
    response = client.get("/docs")
    assert response.status_code == 200

def test_openapi_schema():
    response = client.get("/openapi.json")
    assert response.status_code == 200
    assert "openapi" in response.json()
