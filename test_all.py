"""
Automated Self-Test Suite
Prepared by Dr. Rameshwer | Full-Stack AI Engineer

Tests all 10 steps to verify code correctness and schema validation.
Run with:
    pytest
or
    python test_all.py
"""

import subprocess
import sys
from pydantic import ValidationError
from fastapi.testclient import TestClient

def test_step01():
    res = subprocess.run([sys.executable, "01_hello_llm.py"], capture_output=True, text=True)
    assert res.returncode == 0
    assert "Step 1: Hello LLM" in res.stdout

def test_step02():
    res = subprocess.run([sys.executable, "02_tokens_and_cost.py"], capture_output=True, text=True)
    assert res.returncode == 0
    assert "Step 2: Tokens and Cost" in res.stdout

def test_step03():
    res = subprocess.run([sys.executable, "03_temperature.py"], capture_output=True, text=True)
    assert res.returncode == 0
    assert "Step 3: Temperature" in res.stdout

def test_step04():
    res = subprocess.run([sys.executable, "04_system_instructions.py"], capture_output=True, text=True)
    assert res.returncode == 0
    assert "Step 4: System Instructions" in res.stdout

def test_step05():
    res = subprocess.run([sys.executable, "05_few_shot_prompting.py"], capture_output=True, text=True)
    assert res.returncode == 0
    assert "Step 5: Few-Shot" in res.stdout

def test_step06():
    res = subprocess.run([sys.executable, "06_step_by_step_reasoning.py"], capture_output=True, text=True)
    assert res.returncode == 0
    assert "Step 6: Step-by-Step" in res.stdout

def test_step07():
    res = subprocess.run([sys.executable, "07_pydantic_validation.py"], capture_output=True, text=True)
    assert res.returncode == 0
    assert "Step 7: Pydantic" in res.stdout

def test_step08():
    res = subprocess.run([sys.executable, "08_structured_output.py"], capture_output=True, text=True)
    assert res.returncode == 0
    assert "Step 8: Structured Output" in res.stdout

def test_step09():
    res = subprocess.run([sys.executable, "09_tool_calling.py"], capture_output=True, text=True)
    assert res.returncode == 0
    assert "Step 9: Function / Tool Calling" in res.stdout

def test_step10_fastapi():
    from importlib import import_module
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
    print(" All 10 Steps Passed Verification!")
