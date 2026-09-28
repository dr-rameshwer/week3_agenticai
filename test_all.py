"""
Automated Self-Test Suite
Prepared by Dr. Rameshwer | Full-Stack AI Engineer

Tests all 11 steps to verify code correctness and schema validation.
Run with:
    pytest
or
    python test_all.py
"""

import subprocess
import sys
from pathlib import Path
from pydantic import ValidationError
from fastapi.testclient import TestClient

BASE_DIR = Path(__file__).parent

def run_step(filename: str) -> subprocess.CompletedProcess:
    filepath = BASE_DIR / filename
    return subprocess.run([sys.executable, str(filepath)], capture_output=True, text=True)

def test_step01():
    res = run_step("01_hello_llm.py")
    assert res.returncode == 0
    assert "Step 1: Hello LLM" in res.stdout

def test_step02():
    res = run_step("02_tokens_and_cost.py")
    assert res.returncode == 0
    assert "Step 2: Tokens and Cost" in res.stdout

def test_step03():
    res = run_step("03_temperature.py")
    assert res.returncode == 0
    assert "Step 3: Temperature" in res.stdout

def test_step04():
    res = run_step("04_system_instructions.py")
    assert res.returncode == 0
    assert "Step 4: System Instructions" in res.stdout

def test_step05():
    res = run_step("05_few_shot_prompting.py")
    assert res.returncode == 0
    assert "Step 5: Few-Shot" in res.stdout

def test_step06():
    res = run_step("06_step_by_step_reasoning.py")
    assert res.returncode == 0
    assert "Step 6: Step-by-Step" in res.stdout

def test_step07():
    res = run_step("07_pydantic_validation.py")
    assert res.returncode == 0
    assert "Step 7: Pydantic" in res.stdout

def test_step08():
    res = run_step("08_structured_output.py")
    assert res.returncode == 0
    assert "Step 8: Structured Output" in res.stdout

def test_step09():
    res = run_step("09_tool_calling.py")
    assert res.returncode == 0
    assert "Step 9: Function / Tool Calling" in res.stdout

def test_step10_fastapi():
    from importlib import import_module
    if str(BASE_DIR) not in sys.path:
        sys.path.insert(0, str(BASE_DIR))
    mod = import_module("10_fastapi_ai_service")
    client = TestClient(mod.app)
    
    # Test health
    health = client.get("/health")
    assert health.status_code == 200
    assert health.json()["status"] == "online"

    # Test advisory POST
    res = client.post("/api/v1/advisory", json={"subject": "AI", "question": "How to learn LangGraph?"})
    assert res.status_code == 200
    assert "advice" in res.json()

def test_step11_campus_capstone():
    from importlib import import_module
    if str(BASE_DIR) not in sys.path:
        sys.path.insert(0, str(BASE_DIR))
    cap = import_module("11_campus_ai_capstone")
    client = TestClient(cap.app)

    # Test GET /
    home = client.get("/")
    assert home.status_code == 200
    assert home.json()["status"] == "ONLINE"

    # Test POST /chat for student 1 (Aarav)
    res1 = client.post("/chat", json={"message": "What is the status of AI-2026-001?"})
    assert res1.status_code == 200
    assert "Aarav Sharma" in res1.json()["reply"]
    assert "ELIGIBLE" in res1.json()["reply"]

    # Test POST /chat for student 2 (Priya)
    res2 = client.post("/chat", json={"message": "Can AI-2026-002 write the exam?"})
    assert res2.status_code == 200
    assert "Priya Patel" in res2.json()["reply"]
    assert "NOT ELIGIBLE" in res2.json()["reply"]

if __name__ == "__main__":
    print("Running Self-Tests...")
    test_step01()
    test_step02()
    test_step03()
    test_step04()
    test_step05()
    test_step06()
    test_step07()
    test_step08()
    test_step09()
    test_step10_fastapi()
    test_step11_campus_capstone()
    print(" All 11 Steps Passed Verification!")
