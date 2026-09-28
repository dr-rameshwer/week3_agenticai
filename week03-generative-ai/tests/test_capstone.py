"""
Automated Test Suite for Capstone Microservice
Course Instructor: Dr. Rameshwer

Runs the full suite of integration tests on the capstone application.
"""

import sys
from pathlib import Path
from fastapi.testclient import TestClient

CAPSTONE_DIR = Path(__file__).parent.parent / "capstone"
if str(CAPSTONE_DIR) not in sys.path:
    sys.path.insert(0, str(CAPSTONE_DIR))

from app.main import app

client = TestClient(app)

def test_capstone_health():
    res = client.get("/health")
    assert res.status_code == 200
    assert res.json()["status"] == "online"

def test_capstone_student_lookup():
    res = client.get("/api/v1/students/CS2026")
    assert res.status_code == 200
    assert res.json()["name"] == "Alice Smith"

def test_capstone_course_lookup():
    res = client.get("/api/v1/courses/CS301")
    assert res.status_code == 200
    assert res.json()["credits"] == 4

def test_capstone_advisory_chat():
    payload = {
        "roll_no": "CS2026",
        "query": "Can I enroll in CS401 next term?"
    }
    res = client.post("/api/v1/advisory/chat", json=payload)
    assert res.status_code == 200
    assert "advisory_recommendation" in res.json()
