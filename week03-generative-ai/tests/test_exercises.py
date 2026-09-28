"""
Automated Test Suite for Week 03 Student Exercises & Solutions
Course Instructor: Dr. Rameshwer

Validates functions, schemas, and return formats.
"""

import sys
from pathlib import Path
import pytest
from pydantic import ValidationError

# Add week03 directory to sys.path
WEEK3_DIR = Path(__file__).parent.parent
if str(WEEK3_DIR) not in sys.path:
    sys.path.insert(0, str(WEEK3_DIR))

from exercises.ex02_token_budget import calculate_token_cost
from exercises.ex03_temp_experiment import get_generation_parameters
from exercises.ex04_system_persona import build_academic_system_prompt
from exercises.ex05_few_shot_classifier import build_few_shot_prompt
from exercises.ex06_step_by_step_reasoner import extract_final_gpa
from exercises.ex07_pydantic_validator import CourseSyllabus
from exercises.ex08_json_extractor import parse_candidate_json
from exercises.ex09_custom_tool import query_library_book_status

def test_token_cost_calculator():
    res = calculate_token_cost(1000, 2000)
    assert res["total_tokens"] == 3000
    assert res["total_cost_usd"] > 0

def test_temperature_parameters():
    params_code = get_generation_parameters("code_generation")
    assert params_code["temperature"] == 0.0
    params_creative = get_generation_parameters("creative_writing")
    assert params_creative["temperature"] == 0.9

def test_academic_system_prompt():
    prompt = build_academic_system_prompt()
    assert "Academic Integrity" in prompt
    assert len(prompt) > 20

def test_few_shot_prompt_builder():
    exemplars = [{"input": "Wifi dead", "output": "Infra"}]
    prompt = build_few_shot_prompt("Task", exemplars, "Printer broken")
    assert "### Example 1" in prompt
    assert "Printer broken" in prompt

def test_extract_final_gpa():
    sample = "Calculations: ... checked. FINAL ANSWER: GPA = 3.75"
    assert extract_final_gpa(sample) == 3.75

def test_pydantic_course_syllabus_valid():
    s = CourseSyllabus(
        course_code="CS301",
        title="Database Systems",
        credits=4,
        modules=["SQL", "Indexing"]
    )
    assert s.course_code == "CS301"

def test_pydantic_course_syllabus_lowercase_rejected():
    with pytest.raises(ValidationError):
        CourseSyllabus(
            course_code="cs301", # Should fail validator: must be uppercase!
            title="Database Systems",
            credits=4,
            modules=["SQL", "Indexing"]
        )

def test_pydantic_resume_extractor():
    sample_json = """{
        "full_name": "Sarah Connor",
        "years_of_experience": 6.0,
        "primary_skills": ["Python", "FastAPI"],
        "highest_degree": "M.S.",
        "hiring_recommendation": "Interview"
    }"""
    candidate = parse_candidate_json(sample_json)
    assert candidate.full_name == "Sarah Connor"
    assert candidate.hiring_recommendation == "Interview"

def test_library_tool_lookup():
    found = query_library_book_status("978-0134685991")
    assert found["found"] is True
    assert "Effective Python" in found["title"]

    not_found = query_library_book_status("999-9999999999")
    assert not_found["found"] is False
