"""
Automated Test Suite for Week 03 Micro-Examples
Course Instructor: Dr. Rameshwer

Tests syntax, imports, and execution of example modules.
"""

import subprocess
import sys
from pathlib import Path

EXAMPLES_DIR = Path(__file__).parent.parent / "examples"

def run_script(script_name: str) -> subprocess.CompletedProcess:
    script_path = EXAMPLES_DIR / script_name
    return subprocess.run(
        [sys.executable, str(script_path)],
        capture_output=True,
        text=True,
        timeout=15
    )

def test_01_hello_llm_execution():
    res = run_script("01_hello_llm.py")
    assert res.returncode == 0
    assert "PROGRAM: 01_hello_llm.py" in res.stdout

def test_02_token_inspector_execution():
    res = run_script("02_token_inspector.py")
    assert res.returncode == 0
    assert "PROGRAM: 02_token_inspector.py" in res.stdout

def test_03_temperature_execution():
    res = run_script("03_temperature.py")
    assert res.returncode == 0
    assert "PROGRAM: 03_temperature.py" in res.stdout

def test_04_system_instruction_execution():
    res = run_script("04_system_instruction.py")
    assert res.returncode == 0
    assert "PROGRAM: 04_system_instruction.py" in res.stdout

def test_05_few_shot_execution():
    res = run_script("05_few_shot.py")
    assert res.returncode == 0
    assert "PROGRAM: 05_few_shot.py" in res.stdout

def test_06_reasoning_execution():
    res = run_script("06_reasoning.py")
    assert res.returncode == 0
    assert "PROGRAM: 06_reasoning.py" in res.stdout

def test_07_pydantic_basics_execution():
    res = run_script("07_pydantic_basics.py")
    assert res.returncode == 0
    assert "PROGRAM: 07_pydantic_basics.py" in res.stdout
    assert "Validated Object:" in res.stdout
    assert "ValidationError" in res.stdout

def test_08_structured_output_execution():
    res = run_script("08_structured_output.py")
    assert res.returncode == 0
    assert "PROGRAM: 08_structured_output.py" in res.stdout

def test_09_tool_calling_execution():
    res = run_script("09_tool_calling.py")
    assert res.returncode == 0
    assert "PROGRAM: 09_tool_calling.py" in res.stdout
