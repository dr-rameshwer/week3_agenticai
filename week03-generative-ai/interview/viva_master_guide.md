# Viva Voce Examination Guide: Generative AI & Python Microservices

**Prepared by Dr. Rameshwer**  
*Course Instructor: Dr. Rameshwer*  
*Comprehensive Laboratory Viva Voce Examiner Questions & Answers*

---

## 1. Laboratory Viva Questions by Topic

### Module 01: LLM Fundamentals
1. **Q**: *What library loads variables from a `.env` file into Python?*  
   **A**: `python-dotenv` via the `load_dotenv()` function.
2. **Q**: *What happens if you initialize `genai.Client()` with an invalid API key?*  
   **A**: The initial initialization may succeed, but the first API request will raise an authentication error (HTTP 401 or 403 Forbidden).

### Module 02: Token Economics
3. **Q**: *What are the three main token counts returned in `usage_metadata`?*  
   **A**: `prompt_token_count` (input), `candidates_token_count` (output), and `total_token_count` (sum of both).
4. **Q**: *Approximately how many words are in 100 tokens in English?*  
   **A**: Approximately 75 words (or roughly 4 characters per token).

### Module 03: Temperature
5. **Q**: *When should an engineer set temperature to 0.0?*  
   **A**: For deterministic, fact-based tasks such as code generation, math problem solving, JSON extraction, and classification.

### Module 04: System Instructions
6. **Q**: *What is the purpose of setting a system instruction?*  
   **A**: To establish persistent behavioral rules, persona boundaries, formatting mandates, and safety guardrails across the session.

### Module 05: Few-Shot Prompting
7. **Q**: *What is an exemplar in prompt engineering?*  
   **A**: A paired input-output demonstration showing the model exactly how to format and classify target inputs.

### Module 06: Structured Reasoning
8. **Q**: *Why does asking the model to show calculation steps improve arithmetic accuracy?*  
   **A**: The intermediate tokens are stored in the context window and attended to by subsequent attention layers as external working memory.

### Module 07: Pydantic Basics
9. **Q**: *What is the Pydantic v2 method to serialize a model to a Python dictionary?*  
   **A**: `model_instance.model_dump()`.
10. **Q**: *What exception is raised when data violates a Pydantic schema?*  
    **A**: `pydantic.ValidationError`.

### Module 08: Structured Output
11. **Q**: *What parameters in `GenerateContentConfig` force the model to output schema-compliant JSON?*  
    **A**: `response_mime_type="application/json"` and `response_schema=YourPydanticClass`.

### Module 09: Tool Calling
12. **Q**: *How does the model know what arguments a Python tool function requires?*  
    **A**: The SDK inspects the function's type annotations and docstring, compiling them into an OpenAPI JSON Schema.

### Module 10: FastAPI Microservices
13. **Q**: *Where can a developer view interactive Swagger documentation in a FastAPI app?*  
    **A**: At the `/docs` route on the running server.
14. **Q**: *Why are AI route handlers declared with `async def`?*  
    **A**: To avoid blocking the web server worker threads during network I/O calls to the LLM API.
