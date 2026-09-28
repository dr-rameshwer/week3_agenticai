# Technical Interview Deep-Dive: Generative AI & Backend Engineering

**Prepared by Dr. Rameshwer**  
*Course Instructor: Dr. Rameshwer*  
*In-Depth Technical Interview Questions, System Design, and Architectural Scenarios*

---

## 1. Core Architecture & Sampling Mechanics

### Q1: Explain how nucleus sampling (Top-p) works in conjunction with Temperature.
**Answer**:
Nucleus sampling (Top-p) dynamically bounds the candidate token pool before temperature sampling occurs:
1. Logits are converted to probabilities via standard Softmax.
2. Tokens are sorted in descending order of probability.
3. The cumulative probability sum is computed: $S_k = \sum_{i=1}^k P(y_i)$.
4. The candidate pool is truncated at the smallest index $k$ where $S_k \ge p$ (e.g., $p=0.95$). All other tokens outside this nucleus are discarded.
5. Softmax with temperature $T$ is then re-normalized across this truncated subset.

This prevents the model from selecting catastrophic low-probability tokens from the long tail while preserving diversity among plausible alternatives.

---

### Q2: What is the KV Cache in Transformer inference, and why is prompt caching so impactful for token pricing?
**Answer**:
During autoregressive token generation, computing attention scores requires Key ($K$) and Value ($V$) projections for all preceding tokens in the context window.
* Without caching, each new token step would require recomputing $K$ and $V$ matrices for the entire sequence, resulting in $\mathcal{O}(N^2)$ computational complexity per token.
* The **KV Cache** stores previously computed $K$ and $V$ tensors in GPU VRAM, reducing next-token generation complexity to $\mathcal{O}(N)$.
* **Prompt Caching** allows cloud API providers to persist the KV tensors of static system instructions or long documents across multiple consecutive API calls. This enables providers to discount prompt token pricing by up to $50\text{--}75\%$ and dramatically reduce Time-To-First-Token (TTFT) latency.

---

## 2. Pydantic v2 & Type Safety

### Q3: Contrast Pydantic `BaseModel` vs standard Python `dataclasses`.
**Answer**:
* **`dataclasses`**: Standard library decorator (`@dataclass`) that automatically writes `__init__`, `__repr__`, and `__eq__`. It does **not** perform runtime type checking or coercion by default (e.g., assigning a string to an integer field succeeds without error).
* **Pydantic `BaseModel`**: Full data parsing and validation engine. It enforces runtime type coercion, recursive nested validation, custom field constraints (`Field`), serialization hooks (`model_dump`), and exports JSON Schema definitions required for LLM constrained decoding.

---

## 3. Tool Calling & Agentic Execution

### Q4: How does a Tool-Calling Agent handle multi-step reasoning where tool output from step 1 is required for tool input in step 2?
**Answer**:
The agent orchestrator implements a **ReAct (Reasoning + Acting) loop**:
1. Turn 1: Model receives user prompt $\to$ Emits `tool_call_1(query="...")`.
2. App executes `tool_call_1` $\to$ Sends `tool_response_1` back to model conversation history.
3. Turn 2: Model receives updated history $\to$ Determines information is still incomplete $\to$ Emits `tool_call_2(filter=tool_response_1.id)`.
4. App executes `tool_call_2` $\to$ Returns `tool_response_2`.
5. Turn 3: Model synthesizes both tool responses $\to$ Emits final natural language response $\to$ Orchestrator terminates loop.

---

## 4. Production API Engineering

### Q5: How do you design an LLM microservice to handle streaming responses (Server-Sent Events) in FastAPI?
**Answer**:
1. In the LLM SDK, invoke streaming generation (e.g., `client.models.generate_content_stream(...)`).
2. Define an asynchronous Python generator function:
   ```python
   async def token_generator():
       for chunk in stream:
           yield f"data: {chunk.text}\n\n"
   ```
3. Return `starlette.responses.StreamingResponse(token_generator(), media_type="text/event-stream")`.
4. This sends token deltas to the frontend client in real-time, drastically reducing perceived user latency.
