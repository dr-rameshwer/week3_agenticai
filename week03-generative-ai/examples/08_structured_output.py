"""
Program: 08_structured_output.py
Course: Generative AI & Python Development
Course Instructor: Dr. Rameshwer

Concept: Guaranteed Structured JSON Output using Pydantic schemas
         and constrained decoding (response_schema, response_mime_type).
"""

import os
import sys
from typing import List
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

print("=" * 50)
print("PROGRAM: 08_structured_output.py")
print("Course Instructor: Dr. Rameshwer")
print("=" * 50)

# Step 1: Define the Pydantic schema for structured output
class CourseFeedbackAnalysis(BaseModel):
    course_code: str = Field(description="Course code identifier, e.g. CS301")
    sentiment: str = Field(description="Positive, Neutral, or Negative")
    sentiment_score: float = Field(ge=0.0, le=1.0, description="Confidence score")
    key_topics: List[str] = Field(description="Key topics extracted from review")
    recommended_action: str = Field(description="Concrete recommendation for instructor")

student_review = """
I really enjoyed CS301 this semester! The coding assignments on FastAPI and Pydantic were
extremely practical, though the server deployment lecture went a bit too fast in week 3.
Overall, one of the best courses in the department!
"""

if not api_key:
    print("[NOTICE]: Running in educational simulation mode (No API Key).")
    mock_json = """{
        "course_code": "CS301",
        "sentiment": "Positive",
        "sentiment_score": 0.95,
        "key_topics": ["FastAPI", "Pydantic", "Server Deployment"],
        "recommended_action": "Provide supplementary materials or extra lab time for server deployment."
    }"""
    parsed = CourseFeedbackAnalysis.model_validate_json(mock_json)
    print("--- Validated Pydantic Instance (Simulated) ---")
    print(f"Course: {parsed.course_code}")
    print(f"Sentiment: {parsed.sentiment} (Score: {parsed.sentiment_score})")
    print(f"Topics: {', '.join(parsed.key_topics)}")
    print(f"Action: {parsed.recommended_action}")
    print("=" * 50)
    sys.exit(0)

try:
    from google import genai
    from google.genai import types

    client = genai.Client(api_key=api_key)
    model_name = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

    # Step 2: Configure generation with response_schema
    config = types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=CourseFeedbackAnalysis,
        temperature=0.0
    )

    response = client.models.generate_content(
        model=model_name,
        contents=f"Analyze the following student feedback review:\n{student_review}",
        config=config
    )

    # Step 3: Validate and parse into Pydantic instance
    parsed_result = CourseFeedbackAnalysis.model_validate_json(response.text)

    print("--- Successfully Validated Pydantic Model ---")
    print(f"Course Code:        {parsed_result.course_code}")
    print(f"Sentiment:          {parsed_result.sentiment} (Confidence: {parsed_result.sentiment_score})")
    print(f"Key Topics:         {', '.join(parsed_result.key_topics)}")
    print(f"Recommended Action: {parsed_result.recommended_action}")
    print("=" * 50)

except Exception as e:
    print(f"[ERROR]: Execution failed: {e}")
    sys.exit(1)
