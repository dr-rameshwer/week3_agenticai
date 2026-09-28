# Generative AI & Python Engineering Glossary

**Prepared by Dr. Rameshwer**  
*Course Instructor: Dr. Rameshwer*  
*Standard Reference Glossary of Technical Terms*

---

### A
* **API (Application Programming Interface)**: A structured software protocol that allows two applications to communicate over a network using standard request/response conventions.
* **API Key**: A secret alphanumeric credential used to identify, authenticate, and bill client requests against a remote service.
* **ASGI (Asynchronous Server Gateway Interface)**: The Python standard for asynchronous web servers and applications (e.g., FastAPI, Starlette, Uvicorn).
* **Autoregressive Generation**: A generation process where a model predicts the next token based on all preceding tokens, appending each new token to the sequence iteratively.

### B
* **Base Model**: An LLM trained on vast amounts of raw text data without task-specific reinforcement learning or instruction tuning.
* **BaseModel (Pydantic)**: The foundational class in Pydantic used to define data schemas with automatic runtime validation and serialization.
* **Byte-Pair Encoding (BPE)**: A sub-word tokenization algorithm that iteratively merges the most frequent pairs of bytes/characters in a corpus.

### C
* **Context Window**: The maximum number of tokens (input prompt + output completion) that an LLM can process simultaneously in a single forward pass.
* **Chain of Thought (CoT)**: A prompting technique where the model is guided to generate intermediate reasoning steps before arriving at a final conclusion.

### D
* **Decorator**: A Python function that takes another function as an argument, extends its behavior without modifying it directly, and returns a new function (prefixed with `@`).
* **Deterministic Output**: An output that is identical and reproducible every time a specific input is provided.

### F
* **Few-Shot Prompting**: An in-context learning technique where the prompt includes 2 to 8 input-output examples demonstrating the desired task before providing the target input.
* **FastAPI**: A modern, high-performance web framework for building REST APIs with Python 3.8+ based on standard Python type hints.
* **Function / Tool Calling**: A mechanism allowing an LLM to detect when an external function should be invoked and generate the required structured arguments.

### G
* **Greedy Decoding**: A token selection strategy that always picks the token with the highest logit/probability at each step ($T = 0$).

### H
* **Hallucination**: A phenomenon where an LLM generates factually incorrect, ungrounded, or nonsensical information with high linguistic confidence.
* **HTTP Status Code**: Standardized 3-digit numeric codes returned by servers (e.g., `200 OK`, `400 Bad Request`, `404 Not Found`, `422 Unprocessable Entity`, `500 Internal Server Error`).

### I
* **In-Context Learning**: The ability of an LLM to adapt to new tasks, formatting rules, and guidelines purely from instructions and examples provided inside its context window.

### L
* **Logits**: The raw, unnormalized prediction scores output by the final linear layer of a neural network before applying the Softmax activation.

### O
* **OpenAPI**: A standard, language-agnostic interface specification for REST APIs that allows both humans and computers to discover and understand service capabilities.

### P
* **Prompt**: The complete text, instructions, and context submitted to an LLM to guide its response generation.
* **Pydantic**: A data validation and settings management library for Python using standard type annotations.

### R
* **REST (Representational State Transfer)**: An architectural style for networked applications using standard HTTP methods (`GET`, `POST`, `PUT`, `DELETE`).

### S
* **Softmax**: A mathematical function that converts a vector of numbers (logits) into a probability distribution where all values sum to $1.0$.
* **Structured Output**: Forcing an LLM response to adhere strictly to a predefined schema (like JSON or Pydantic) using constrained decoding grammars.
* **System Instruction**: A high-priority instruction that defines the persona, tone, guardrails, and behavioral parameters of an LLM session.

### T
* **Temperature**: A hyperparameter that scales logits before Softmax to control the randomness and diversity of generated tokens.
* **Token**: The atomic sub-word unit of text processed by language models.

### U
* **Uvicorn**: A lightning-fast ASGI web server implementation for Python.

### V
* **ValidationError (Pydantic)**: An exception raised when input data fails to satisfy the type constraints or validator rules of a Pydantic model.
* **Virtual Environment (`venv`)**: An isolated directory tree containing a Python installation for a particular version of Python, plus a number of additional packages.

### Z
* **Zero-Shot Prompting**: Presenting a prompt to a language model without any input-output examples.
