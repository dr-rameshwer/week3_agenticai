"""
Exercise 07: Pydantic Schema Validator
Course Instructor: Dr. Rameshwer

Task:
Define a Pydantic schema `CourseSyllabus` with field validation constraints:
- course_code: str (min 5 chars, max 10 chars, uppercase)
- title: str (min 3 chars)
- credits: int (between 1 and 4)
- modules: list of strings (minimum 2 modules)
"""

from typing import List
from pydantic import BaseModel, Field, field_validator

class CourseSyllabus(BaseModel):
    # TODO 1: Define course_code with min_length=5, max_length=10
    course_code: str = Field(min_length=5, max_length=10, description="e.g. CS101")

    # TODO 2: Define title with min_length=3
    title: str = Field(min_length=3, description="Course title")

    # TODO 3: Define credits with ge=1, le=4
    credits: int = Field(ge=1, le=4, description="Credit hours")

    # TODO 4: Define modules list
    modules: List[str] = Field(default_factory=list, description="Course topics/modules")

    @field_validator("course_code")
    @classmethod
    def validate_uppercase_code(cls, v: str) -> str:
        # TODO 5: Enforce that course_code is uppercase
        if not v.isupper():
            raise ValueError("course_code must be uppercase (e.g., 'CS301').")
        return v

    @field_validator("modules")
    @classmethod
    def validate_module_count(cls, v: List[str]) -> List[str]:
        if len(v) < 2:
            raise ValueError("Course syllabus must contain at least 2 modules.")
        return v

if __name__ == "__main__":
    syllabus = CourseSyllabus(
        course_code="CS301",
        title="Generative AI Systems",
        credits=4,
        modules=["Prompt Engineering", "Pydantic Schemas", "FastAPI Microservices"]
    )
    print("--- Validated Course Syllabus ---")
    print(syllabus.model_dump_json(indent=2))
