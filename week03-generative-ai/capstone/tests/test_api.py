"""
Integration Tests for Student Academic Advisory Microservice
Course Instructor: Dr. Rameshwer

Uses FastAPI TestClient to test all REST endpoints.
"""

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check_endpoint():
    """Verifies the /health status endpoint returns 200 OK."""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "online"
    assert data["instructor"] == "Dr. Rameshwer"
    assert "model" in data

def test_get_valid_student():
    """Verifies looking up an existing student from the registry."""
    response = client.get("/api/v1/students/CS2026")
    assert response.status_code == 200
    data = response.json()
    assert data["roll_no"] == "CS2026"
    assert data["name"] == "Alice Smith"
    assert data["gpa"] == 3.88

def test_get_invalid_student():
    """Verifies that an unknown student roll number returns 404 Not Found."""
    response = client.get("/api/v1/students/UNKNOWN99")
    assert response.status_code == 404
    assert "not found" in response.json()["detail"].lower()

def test_get_valid_course():
    """Verifies looking up an existing course from the catalogue."""
    response = client.get("/api/v1/courses/CS301")
    assert response.status_code == 200
    data = response.json()
    assert data["course_code"] == "CS301"
    assert "Database" in data["title"]
    assert len(data["prerequisites"]) >= 1

def test_advisory_chat_existing_student():
    """Verifies submitting a student inquiry to the advisory endpoint."""
    payload = {
        "roll_no": "CS2026",
        "query": "What electives should I register for next semester?"
    }
    response = client.post("/api/v1/advisory/chat", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["roll_no"] == "CS2026"
    assert len(data["advisory_recommendation"]) > 10
    assert data["status"] in ["success", "simulated"]

def test_advisory_chat_validation_error():
    """Verifies that empty queries or invalid payload triggers 422 validation error."""
    payload = {
        "roll_no": "C", # Too short! min_length=4
        "query": "Hi"   # Too short! min_length=5
    }
    response = client.post("/api/v1/advisory/chat", json=payload)
    assert response.status_code == 422
