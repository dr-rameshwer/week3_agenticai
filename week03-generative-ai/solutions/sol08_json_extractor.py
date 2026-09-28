"""
Solution 08: Resume Data Extractor with Pydantic
Course Instructor: Dr. Rameshwer

Reference Solution for Exercise 08.
"""

from typing import List, Literal
from pydantic import BaseModel, Field

class CandidateProfile(BaseModel):
    full_name: str = Field(min_length=2, description="Candidate full name")
    years_of_experience: float = Field(ge=0.0, description="Total years of tech experience")
    primary_skills: List[str] = Field(description="Top technical skills")
    highest_degree: str = Field(description="Degree title and major")
    hiring_recommendation: Literal["Interview", "Hold", "Reject"] = Field(
        description="Initial recommendation based on qualifications"
    )

def parse_candidate_json(json_str: str) -> CandidateProfile:
    return CandidateProfile.model_validate_json(json_str)

if __name__ == "__main__":
    sample = """{
        "full_name": "David Miller",
        "years_of_experience": 5.0,
        "primary_skills": ["Python", "FastAPI"],
        "highest_degree": "M.S. in Computer Science",
        "hiring_recommendation": "Interview"
    }"""
    res = parse_candidate_json(sample)
    print("Parsed Candidate:", res.full_name, "-", res.hiring_recommendation)
