"""
Solution 07: Pydantic Schema Validator
Course Instructor: Dr. Rameshwer

Reference Solution for Exercise 07.
"""

from typing import List
from pydantic import BaseModel, Field, field_validator

class CourseSyllabus(BaseModel):
    course_code: str = Field(min_length=5, max_length=10, description="e.g. CS101")
    title: str = Field(min_length=3, description="Course title")
    credits: int = Field(ge=1, le=4, description="Credit hours")
    modules: List[str] = Field(default_factory=list, description="Course topics/modules")

    @field_validator("course_code")
    @classmethod
    def validate_uppercase_code(cls, v: str) -> str:
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
    s = CourseSyllabus(
        course_code="CS401",
        title="Distributed Systems",
        credits=4,
        modules=["Consensus", "Replication", "Fault Tolerance"]
    )
    print("Valid syllabus:", s.model_dump())
