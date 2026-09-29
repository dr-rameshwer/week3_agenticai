"""
Step 8: Guaranteed Structured JSON Output
Prepared by Dr. Rameshwer | Full-Stack AI Engineer

What this teaches:
- Using response_schema to force the LLM to output guaranteed JSON matching a Pydantic class
- Eliminates regex/markdown cleaning hacks in production
"""

import os
from typing import List, Literal
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY", "")

print("=" * 50)
print("Step 8: Structured Output with Pydantic")
print("Guide: Dr. Rameshwer")
print("=" * 50)

class CourseReview(BaseModel):
    course_code: str
    sentiment: Literal["Positive", "Neutral", "Negative"]
    confidence: float = Field(ge=0.0, le=1.0)
    key_topics: List[str]
    recommendation: str

review_text = "CS301 was fantastic! The hands-on FastAPI and Pydantic sessions were practical and clear."

def run_step():
    if api_key.startswith("AIzaSy") and len(api_key) > 20:
        try:
            from google import genai
            from google.genai import types
            client = genai.Client(api_key=api_key)
            response = client.models.generate_content(
                model=os.getenv("GEMINI_MODEL", "gemini-3.6-flash"),
                contents=f"Analyze this student review:\n{review_text}",
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    response_schema=CourseReview,
                    temperature=0.0
                )
            )
            result = CourseReview.model_validate_json(response.text)
            print("--- Parsed Pydantic Object ---")
            print(f"Course:         {result.course_code}")
            print(f"Sentiment:      {result.sentiment} (Confidence: {result.confidence})")
            print(f"Topics:         {', '.join(result.key_topics)}")
            print(f"Recommendation: {result.recommendation}")
            return
        except Exception:
            pass

    print("[NOTICE]: (Offline Simulation Mode)")
    mock_json = '{"course_code": "CS301", "sentiment": "Positive", "confidence": 0.98, "key_topics": ["FastAPI", "Pydantic"], "recommendation": "Maintain practical labs"}'
    res = CourseReview.model_validate_json(mock_json)
    print("--- Parsed Pydantic Object (Simulated) ---")
    print(f"Course:         {res.course_code}")
    print(f"Sentiment:      {res.sentiment} (Confidence: {res.confidence})")
    print(f"Topics:         {', '.join(res.key_topics)}")
    print(f"Recommendation: {res.recommendation}")

if __name__ == "__main__":
    run_step()
    print("=" * 50)
