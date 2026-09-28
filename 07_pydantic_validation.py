"""
Step 7: Pydantic v2 Fundamentals & Validation
Prepared by Dr. Rameshwer | Full-Stack AI Engineer

What this teaches:
- Pydantic BaseModel for type safety and runtime data validation
- Handling valid vs invalid input data with ValidationError
- Exporting to Python dict (model_dump) and JSON (model_dump_json)
"""

from typing import List, Optional
from pydantic import BaseModel, Field, ValidationError

print("=" * 50)
print("Step 7: Pydantic Validation")
print("Guide: Dr. Rameshwer")
print("=" * 50)

# 1. Define Schema
class StudentProfile(BaseModel):
    roll_no: str = Field(min_length=4, max_length=10)
    name: str = Field(min_length=2)
    gpa: float = Field(ge=0.0, le=4.0)
    courses: List[str] = Field(default_factory=list)
    email: Optional[str] = None

# 2. Test Valid Data
print("--- 1. Valid Student ---")
student = StudentProfile(
    roll_no="CS2026",
    name="Alice Smith",
    gpa=3.85,
    courses=["Data Structures", "Agentic AI"]
)
print("Dict:", student.model_dump())
print("JSON:", student.model_dump_json())

# 3. Test Invalid Data
print("\n--- 2. Invalid Data (Catches Errors) ---")
try:
    invalid = StudentProfile(
        roll_no="CS",  # Error: < 4 chars
        name="A",      # Error: < 2 chars
        gpa=4.95       # Error: > 4.0
    )
except ValidationError as e:
    for err in e.errors():
        print(f"  * Field '{err['loc'][0]}': {err['msg']}")

print("=" * 50)
