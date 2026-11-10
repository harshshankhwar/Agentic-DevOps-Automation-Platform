
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "backend"))

from fastapi.testclient import TestClient
from app.main import app

# Create a test client
client = TestClient(app)


# Test 1: Home API
def test_home():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["status"] == "Running"


# Test 2: Health Check API
def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "Healthy"


# Test 3: Project Information API
def test_project():
    response = client.get("/project")

    assert response.status_code == 200
    assert response.json()["project"] == "Agentic AI-Based DevOps Automation Platform"
