# Topic 10: Building Production AI Microservices with FastAPI

**Prepared by Dr. Rameshwer**  
*Course Instructor: Dr. Rameshwer*  
*Student Learning Resource | Practical Module 10*

---

## 1. Learning Objectives
By the end of this topic, you will be able to:
1. Explain what a REST API and microservice architecture are.
2. Initialize a FastAPI application with automated OpenAPI / Swagger documentation (`/docs`).
3. Define strongly-typed request and response payloads using Pydantic.
4. Implement asynchronous route handlers (`async def`) for non-blocking I/O.
5. Deploy and test the microservice using Uvicorn and HTTP test clients.

---

## 2. Why Are We Learning This?
Python scripts running in a terminal cannot serve web browsers, mobile apps, or frontend dashboards. To make your AI models accessible to other software systems, you must wrap them inside a high-throughput, production-ready REST API microservice.

---

## 3. Concept in Simple Words
**FastAPI** is a Python web framework that lets you turn any Python function into a web URL (an **Endpoint**). When a user sends a JSON message over the internet to your endpoint, FastAPI validates the data, runs your AI logic, and returns a clean JSON response.

---

## 4. Real-World Analogy
Think of a bank's Drive-Through ATM:
* **The Slot (Endpoint)**: Where you insert your card and PIN (`POST /api/v1/advisory`).
* **The Validation Mechanism (Pydantic)**: Verifies that your PIN is 4 digits and your card is not expired.
* **The Vault Computer (FastAPI + LLM Backend)**: Processes the transaction asynchronously.
* **The Cash Dispenser (Response)**: Returns the verified result in standard currency (JSON).

---

## 5. Technical Explanation
When an HTTP POST request hits `/api/v1/explain`:
1. **Uvicorn** receives the raw TCP/HTTP stream and forwards the ASGI event to FastAPI.
2. FastAPI uses **Pydantic** to parse and validate the request body against `ExplainRequest`. If invalid, it returns `422 Unprocessable Entity` immediately.
3. The asynchronous handler `async def explain_concept(...)` is scheduled on Python's `asyncio` event loop.
4. The handler calls the LLM API without blocking worker threads.
5. FastAPI serializes the returned data into `ExplainResponse` and transmits HTTP `200 OK`.

---

## 6. Important Terminology
* **REST API**: Representational State Transfer protocol using HTTP methods (`GET`, `POST`).
* **Endpoint / Path Operation**: A specific URL route (e.g., `/api/v1/generate`) mapped to a Python function.
* **ASGI (Asynchronous Server Gateway Interface)**: The standard interface between async Python web servers (Uvicorn) and web frameworks (FastAPI).
* **OpenAPI / Swagger UI**: Automated interactive documentation generated at `/docs`.

---

## 7. Python Syntax & Concepts Encountered
* `app = FastAPI(title=...)`: Creating the application instance.
* `@app.get("/path")` and `@app.post("/path", response_model=...)`: Route decorators.
* `async def`: Defining asynchronous coroutine functions.
* `raise HTTPException(status_code=400, detail="...")`: Returning standard HTTP errors.

---

## 8. Smallest Working Example (`10_fastapi_ai.py`)

```python
import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from google import genai
from pydantic import BaseModel, Field
import uvicorn

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key) if api_key else None

# Step 1: Initialize FastAPI app
app = FastAPI(
    title="Academic AI Advisory Microservice",
    description="Course Instructor: Dr. Rameshwer | Week 3 Student Learning Resource",
    version="1.0.0"
)

# Step 2: Define Request and Response Schemas
class AdvisoryRequest(BaseModel):
    subject: str = Field(min_length=2, max_length=50, description="Academic subject area")
    question: str = Field(min_length=5, max_length=300, description="Specific student inquiry")

class AdvisoryResponse(BaseModel):
    subject: str
    explanation: str
    status: str = "success"

# Step 3: Health Check Endpoint
@app.get("/health", tags=["System"])
def health_check():
    """Returns the operational status of the microservice."""
    return {"status": "healthy", "service": "academic-ai-advisor", "version": "1.0.0"}

# Step 4: Core AI Generation Endpoint
@app.post("/api/v1/advisory", response_model=AdvisoryResponse, tags=["AI Services"])
async def get_advisory(request: AdvisoryRequest):
    """Processes a student academic inquiry and returns tailored mentor advice."""
    if not client:
        # Fallback simulation if no API key is set
        return AdvisoryResponse(
            subject=request.subject,
            explanation=f"[Simulated Advisor]: Focus on core {request.subject} fundamentals regarding: {request.question}"
        )
    
    try:
        prompt = f"Subject: {request.subject}\nStudent Question: {request.question}\nProvide concise academic advice in under 3 sentences."
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return AdvisoryResponse(
            subject=request.subject,
            explanation=response.text.strip()
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM generation failed: {str(e)}")

# Step 5: Direct Execution Block
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
```

---

## 9. Code Explanation — Line by Line
* **Line 3**: Imports `FastAPI` and `HTTPException`.
* **Lines 13-17**: Initializes the `FastAPI` instance with title and metadata.
* **Lines 20-27**: Declares `AdvisoryRequest` and `AdvisoryResponse` models using Pydantic.
* **Lines 30-33**: `@app.get("/health")` registers a lightweight health check route.
* **Lines 36-58**: `@app.post("/api/v1/advisory", response_model=AdvisoryResponse)` defines the asynchronous endpoint. It receives `request: AdvisoryRequest`, generates advice, and guarantees an `AdvisoryResponse` return structure.
* **Lines 61-62**: Starts Uvicorn server on `http://127.0.0.1:8000`.

---

## 10. Expected Output & Swagger UI
When running, open your web browser to:
`http://127.0.0.1:8000/docs`

You will see an interactive API dashboard allowing you to test the `/health` and `/api/v1/advisory` endpoints directly!

---

## 11. How to Run
```bash
# Option 1: Run the python script directly
python week03-generative-ai/examples/10_fastapi_ai.py

# Option 2: Run via uvicorn with auto-reload
uvicorn week03-generative-ai.examples.10_fastapi_ai:app --reload --port 8000
```

---

## 12. Experiment Yourself
Using `curl` or Postman, send a POST request:
```bash
curl -X POST "http://127.0.0.1:8000/api/v1/advisory" \
     -H "Content-Type: application/json" \
     -d '{"subject": "Algorithms", "question": "How do I master dynamic programming?"}'
```

---

## 13. Common Mistakes
1. Using blocking synchronous `time.sleep()` inside `async def` endpoints instead of `asyncio.sleep()`.
2. Returning a raw dictionary that does not match `response_model` definitions.

---

## 14. Debugging Exercise
**Buggy Code**:
```python
@app.post("/query")
def query_ai(data): # Missing type annotation!
    return {"ans": data.q}
```
**Fix**: Add type hint `data: QueryRequest` so FastAPI knows how to parse and validate the JSON body.

---

## 15. Student Practice Task
Create a script `ex10_fastapi_endpoint.py` that adds a new endpoint `POST /api/v1/code-review` which accepts a Python code snippet and returns a review with score and suggestions.

---

## 16. Mini Challenge
Add an API key authentication dependency using FastAPI's `Header(alias="X-API-Key")` to secure the advisory endpoint.

---

## 17. Real-World Industry Use
Companies like Netflix, Uber, and OpenAI use FastAPI to serve high-concurrency microservices processing billions of API requests daily.

---

## 18. Viva Questions
1. *What is the difference between `@app.get` and `@app.post`?*  
   **Answer**: `GET` retrieves data from the server without modifying state; `POST` sends payload data in the HTTP request body to create or process resources.
2. *Why is `/docs` so powerful for developer collaboration?*  
   **Answer**: It automatically generates an interactive Swagger UI documentation interface derived directly from Python type annotations.

---

## 19. Interview Questions
1. *Why is FastAPI significantly faster than traditional frameworks like Flask or Django for AI endpoints?*  
   **Answer**: FastAPI natively uses asynchronous `asyncio` and `uvicorn` (ASGI), allowing a single worker thread to handle thousands of concurrent pending I/O requests without blocking.

---

## 20. Quick Revision
* Define app with `app = FastAPI()`.
* Annotate request/response with Pydantic `BaseModel`.
* Use `async def` for I/O operations.
* Explore interactive docs at `/docs`.

---

## 21. Checklist
- [ ] Understand REST architecture and ASGI
- [ ] Started Uvicorn server on port 8000
- [ ] Tested `/docs` in browser
- [ ] Sent POST request with `curl` / Swagger UI
