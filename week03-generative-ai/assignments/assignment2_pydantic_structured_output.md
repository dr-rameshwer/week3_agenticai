# Hands-On Assignment 2: Pydantic Schema Validation & Guaranteed Extraction

**Prepared by Dr. Rameshwer**  
*Full-Stack AI Engineer | React.js | TypeScript | Node.js | Python | RAG | Agentic AI | LangGraph | Building AI-Powered Applications*  
*Self-Paced Training Module with Complete Solution & Self-Evaluation*

---

## 1. Problem Statement
Build an automated Research Paper Metadata Extraction Engine using Pydantic v2 schemas and constrained decoding.

---

## 2. Complete Reference Solution Code

```python
import os
from typing import List, Literal
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

class ResearchPaperReport(BaseModel):
    paper_id: str = Field(description="e.g. arXiv:2401.12345")
    title: str = Field(min_length=5, max_length=200)
    authors: List[str] = Field(min_length=1)
    publication_year: int = Field(ge=1970, le=2026)
    primary_domain: Literal["AI", "Systems", "Security", "Theory", "HCI"]
    key_contributions: List[str] = Field(min_length=2, max_length=5)
    confidence_score: float = Field(ge=0.0, le=1.0)

SAMPLE_ABSTRACT = """
arXiv:2403.09876
Title: Multi-Agent Orchestration for Distributed Microservice Resilience
Authors: Dr. Rameshwer, A. Smith (2025)
Domain: AI
Abstract: We present an agentic AI control loop leveraging Pydantic schema validation and tool calling
to automatically detect and recover microservice failures.
"""

def extract_metadata():
    if not api_key:
        mock = """{
            "paper_id": "arXiv:2403.09876",
            "title": "Multi-Agent Orchestration for Distributed Microservice Resilience",
            "authors": ["Dr. Rameshwer", "A. Smith"],
            "publication_year": 2025,
            "primary_domain": "AI",
            "key_contributions": ["Agentic AI control loop", "Pydantic validation"],
            "confidence_score": 0.98
        }"""
        res = ResearchPaperReport.model_validate_json(mock)
        print("Validated Pydantic Instance:\n", res.model_dump_json(indent=2))
        return res

    from google import genai
    from google.genai import types

    client = genai.Client(api_key=api_key)
    config = types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=ResearchPaperReport,
        temperature=0.0
    )

    response = client.models.generate_content(
        model=os.getenv("GEMINI_MODEL", "gemini-2.5-flash"),
        contents=f"Extract metadata from this research abstract:\n{SAMPLE_ABSTRACT}",
        config=config
    )

    report = ResearchPaperReport.model_validate_json(response.text)
    print("--- Extracted Pydantic Model ---")
    print(report.model_dump_json(indent=2))
    return report

if __name__ == "__main__":
    extract_metadata()
```

---

## 3. Self-Evaluation & Verification
1. Run: `python assignment2_extractor.py`
2. **Self-Check**:
   - Is the response parsed directly via `ResearchPaperReport.model_validate_json` without any `JSONDecodeError`?
   - Try passing invalid year (`publication_year=1800`) to confirm that Pydantic raises `ValidationError`.
