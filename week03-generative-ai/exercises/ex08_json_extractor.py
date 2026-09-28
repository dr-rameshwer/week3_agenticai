"""
Exercise 08: Resume Data Extractor with Pydantic
Course Instructor: Dr. Rameshwer

Task:
Define a Pydantic schema for parsing raw candidate resume text
and validate extraction.
"""

from typing import List, Literal
from pydantic import BaseModel, Field

class CandidateProfile(BaseModel):
    # TODO 1: Define fields for candidate resume extraction
    full_name: str = Field(min_length=2, description="Candidate full name")
    years_of_experience: float = Field(ge=0.0, description="Total years of tech experience")
    primary_skills: List[str] = Field(description="Top technical skills")
    highest_degree: str = Field(description="Degree title and major")
    hiring_recommendation: Literal["Interview", "Hold", "Reject"] = Field(
        description="Initial recommendation based on qualifications"
    )

def parse_candidate_json(json_str: str) -> CandidateProfile:
    """Validates raw JSON string against CandidateProfile."""
    return CandidateProfile.model_validate_json(json_str)

if __name__ == "__main__":
    sample_json = """{
        "full_name": "David Miller",
        "years_of_experience": 4.5,
        "primary_skills": ["Python", "FastAPI", "Pydantic", "PyTorch"],
        "highest_degree": "B.Tech in Computer Science",
        "hiring_recommendation": "Interview"
    }"""

    profile = parse_candidate_json(sample_json)
    print("--- Extracted Candidate Profile ---")
    print(f"Name:   {profile.full_name}")
    print(f"Exp:    {profile.years_of_experience} years")
    print(f"Skills: {', '.join(profile.primary_skills)}")
    print(f"Status: {profile.hiring_recommendation}")
