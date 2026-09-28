# Topic 01: LLM Fundamentals & Your First API Call

**Prepared by Dr. Rameshwer**  
*Course Instructor: Dr. Rameshwer*  
*Student Learning Resource | Practical Module 01*

---

## 1. Learning Objectives
By the end of this topic, you will be able to:
1. Distinguish clearly between an underlying machine learning model, an API endpoint, and a client SDK.
2. Manage secret API credentials securely using environment variables (`.env`).
3. Initialize the Google GenAI client (`google-genai`).
4. Send a text prompt programmatically and extract the textual response.
5. Implement defensive error handling around network calls.

---

## 2. Why Are We Learning This?
In modern software engineering, you rarely train frontier multi-billion parameter models from scratch on personal machines. Instead, software engineers integrate frontier models as cloud microservices using secure APIs. Mastering programmatic API invocation is the prerequisite first step for every AI engineer.

---

## 3. Concept in Simple Words
Think of a Large Language Model (LLM) as a remote intelligence server. You send it a text message (the **Prompt**), the model processes the message, and it sends back an answer (the **Response**). The **SDK** (Software Development Kit) is a Python library that handles the networking, formatting, and authentication so you can interact with the server in just 3 lines of Python code.

---

## 4. Real-World Analogy
Imagine ordering food at a restaurant:
* **The Kitchen / Chef**: The LLM running on massive GPU clusters in a cloud datacenter.
* **The Menu & Order Slip**: The API specification and your prompt.
* **The Waiter**: The Python SDK (`google-genai`) that takes your order, delivers it securely to the kitchen, and brings your meal (the response) back to your table.
* **Your Table Reservation Pass**: The **API Key** verifying you are authorized to order.

---

## 5. Technical Explanation
When you invoke `client.models.generate_content(...)`:
1. The SDK serializes your prompt into an HTTP POST request payload.
2. It attaches your secret `GEMINI_API_KEY` to the request headers.
3. The request is transmitted over TLS/HTTPS to Google's inference servers.
4. The remote server tokenizes your prompt, passes it through the Transformer layers of `gemini-2.5-flash`, performs autoregressive token generation, and returns a JSON payload containing the generated text, finish reason, and token usage metadata.
5. The SDK parses the JSON response into a Python object with an accessible `.text` attribute.

---

## 6. Important Terminology
* **Model**: The trained neural network weights (e.g., `gemini-2.5-flash`).
* **API (Application Programming Interface)**: The network protocol allowing your code to communicate with Google's servers.
* **SDK (Software Development Kit)**: The official Python library (`google-genai`) wrapping the API.
* **API Key**: A secret cryptographic string that authenticates your requests.
* **Environment Variable**: A dynamic value stored in your operating system shell or loaded from a `.env` file to keep secrets out of source code.

---

## 7. Python Syntax & Concepts Encountered
* `import os`: Python's built-in module for interacting with the operating system.
* `from dotenv import load_dotenv`: Loads key-value pairs from a local `.env` file into `os.environ`.
* `from google import genai`: Imports the official Google GenAI Python SDK.
* `os.getenv("KEY_NAME")`: Reads the value of an environment variable.
* `try ... except ...`: Python's mechanism for handling runtime errors gracefully.

---

## 8. Smallest Working Example (`01_hello_llm.py`)

```python
import os
from dotenv import load_dotenv
from google import genai

# Step 1: Load environment variables from .env file
load_dotenv()

# Step 2: Read the secret API key
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY is missing! Check your .env file.")

# Step 3: Initialize the client
client = genai.Client(api_key=api_key)

# Step 4: Send a prompt to the model
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain Artificial Intelligence in one concise sentence."
)

# Step 5: Display the response text
print("Response from LLM:")
print(response.text)
```

---

## 9. Code Explanation — Line by Line
* **Line 1-3**: `import os`, `from dotenv import load_dotenv`, `from google import genai` imports the operating system interface, the `.env` loader, and the Google GenAI SDK.
* **Line 6**: `load_dotenv()` looks for a `.env` file in the current working directory and loads its key-value pairs into the environment.
* **Line 9**: `os.getenv("GEMINI_API_KEY")` retrieves the key.
* **Lines 10-11**: Defensive check. If the key is missing, raises an immediate, helpful `ValueError`.
* **Line 14**: `client = genai.Client(api_key=api_key)` creates an authenticated client session object.
* **Lines 17-20**: `client.models.generate_content(...)` calls the remote model `gemini-2.5-flash` with the prompt string `contents`.
* **Lines 23-24**: `print(response.text)` extracts and displays the raw text generated by the model.

---

## 10. Expected Output
```text
Response from LLM:
Artificial Intelligence is the branch of computer science dedicated to creating systems capable of performing tasks that typically require human intelligence, such as reasoning, learning, and problem-solving.
```

---

## 11. How to Run
```bash
# Make sure your virtual environment is activated and .env is configured
python week03-generative-ai/examples/01_hello_llm.py
```

---

## 12. Experiment Yourself
Try replacing `"Explain Artificial Intelligence in one concise sentence."` with:
1. Prompt A: `"Explain what a Python list is to a 10-year-old in two sentences."`
2. Prompt B: `"Write a 4-line poem about debugging code at midnight."`
3. Prompt C: `"What are the 3 main differences between a list and a tuple in Python?"`

Compare how the response length, vocabulary, and tone change based on your prompt wording.

---

## 13. Common Mistakes
1. **Hardcoding API Keys**: Writing `api_key = "AIzaSy..."` directly in the `.py` file. If committed to GitHub, bots will compromise your key within seconds.
2. **Forgetting `load_dotenv()`**: Calling `os.getenv("GEMINI_API_KEY")` without calling `load_dotenv()` first will return `None`.
3. **Invalid Model Name**: Passing a typo like `model="gemini-flash-2.0"` instead of `model="gemini-2.5-flash"`.

---

## 14. Debugging Exercise
**Buggy Code**:
```python
import os
from google import genai

# Why will this fail on a machine where .env exists?
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
res = client.models.generate_content(model="gemini-2.5-flash", contents="Hi")
```
**Fix**: `from dotenv import load_dotenv; load_dotenv()` must be invoked before `os.getenv()`.

---

## 15. Student Practice Task
Create a script `ex01_first_call.py` that asks the user for their favorite subject via `input("Enter subject: ")` and prompts the LLM to provide 3 exciting career paths in that subject.

---

## 16. Mini Challenge
Wrap the generation call in a `try...except` block that catches network timeouts or invalid API keys, printing a clean user-friendly error message instead of an ugly Python traceback.

---

## 17. Real-World Industry Use
Every enterprise AI application (from customer support chatbots to automated code reviewers) begins with this exact API client initialization and authentication pattern.

---

## 18. Viva Questions
1. *What is the role of `.env` and `python-dotenv` in application security?*  
   **Answer**: To decouple secrets and configuration from code, preventing credential leaks into version control.
2. *What does the `contents` parameter in `generate_content` accept?*  
   **Answer**: A string prompt, a list of strings/parts, or structured content objects.

---

## 19. Interview Questions
1. *Why do production systems use SDKs rather than raw `curl` or `requests` calls?*  
   **Answer**: SDKs provide automatic retries with exponential backoff, connection pooling, typed response objects, streaming support, and authentication handling.

---

## 20. Quick Revision
* **Load `.env` $\to$ Read key $\to$ Initialize `genai.Client()` $\to$ Call `generate_content()` $\to$ Read `response.text`**.

---

## 21. Checklist
- [ ] Virtual environment is active
- [ ] `.env` file exists and contains `GEMINI_API_KEY`
- [ ] `01_hello_llm.py` executed successfully
- [ ] Completed Experiment Yourself prompts
