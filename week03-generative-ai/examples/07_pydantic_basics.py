"""
Program: 07_pydantic_basics.py
Course: Generative AI & Python Development
Course Instructor: Dr. Rameshwer

Concept: Pydantic v2 fundamentals, BaseModel, Field constraints,
         ValidationError handling, serialization (model_dump, model_dump_json).
"""

from typing import List, Optional
from pydantic import BaseModel, Field, ValidationError

print("=" * 50)
print("PROGRAM: 07_pydantic_basics.py")
print("Course Instructor: Dr. Rameshwer")
print("=" * 50)

# Step 1: Define Schema with type annotations and validation constraints
class StudentProfile(BaseModel):
    roll_no: str = Field(min_length=4, max_length=10, description="Unique student ID")
    name: str = Field(min_length=2, max_length=100, description="Student full name")
    gpa: float = Field(ge=0.0, le=4.0, description="GPA on a 4.0 scale")
    enrolled_courses: List[str] = Field(default_factory=list, description="Course list")
    email: Optional[str] = Field(default=None, description="Campus email address")

# Step 2: Instantiate Valid Model
print("--- 1. Validating Correct Data ---")
student1 = StudentProfile(
    roll_no="CS2026",
    name="Alice Smith",
    gpa=3.85,
    enrolled_courses=["Data Structures", "Generative AI Engineering"]
)

print(f"Validated Object:  {student1}")
print(f"Dictionary Export: {student1.model_dump()}")
print(f"JSON Export:       {student1.model_dump_json()}")

# Step 3: Trigger and Handle Validation Errors
print("\n--- 2. Handling Corrupted Data with ValidationError ---")
try:
    student_invalid = StudentProfile(
        roll_no="CS",     # Violation: min_length=4
        name="X",         # Violation: min_length=2
        gpa=4.95          # Violation: le=4.0
    )
except ValidationError as e:
    print(f"Caught {len(e.errors())} Validation Errors:")
    for err in e.errors():
        field_name = ".".join(str(loc) for loc in err["loc"])
        error_msg = err["msg"]
        print(f"  * Field '{field_name}': {error_msg}")

print("=" * 50)
print("Execution completed successfully.")
