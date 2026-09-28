"""
Exercise 02: Token Budget & Cost Calculator
Course Instructor: Dr. Rameshwer

Task:
Calculate the exact financial cost of an LLM query given token usage counts.
Rates:
- Prompt Tokens: $0.075 per 1,000,000 tokens
- Candidate Tokens: $0.30 per 1,000,000 tokens
"""

def calculate_token_cost(prompt_tokens: int, candidate_tokens: int) -> dict:
    """Calculates total tokens and estimated USD cost.

    TODO: Implement the arithmetic calculations.
    """
    # TODO 1: Compute total tokens
    total_tokens = prompt_tokens + candidate_tokens

    # TODO 2: Compute input cost ($0.075 per 1M)
    input_cost = (prompt_tokens / 1_000_000.0) * 0.075

    # TODO 3: Compute output cost ($0.30 per 1M)
    output_cost = (candidate_tokens / 1_000_000.0) * 0.30

    # TODO 4: Compute total cost
    total_cost = input_cost + output_cost

    return {
        "prompt_tokens": prompt_tokens,
        "candidate_tokens": candidate_tokens,
        "total_tokens": total_tokens,
        "total_cost_usd": round(total_cost, 8)
    }

if __name__ == "__main__":
    test_metrics = calculate_token_cost(prompt_tokens=450, candidate_tokens=850)
    print("--- Token Budget Report ---")
    print(f"Input Tokens:  {test_metrics['prompt_tokens']}")
    print(f"Output Tokens: {test_metrics['candidate_tokens']}")
    print(f"Total Tokens:  {test_metrics['total_tokens']}")
    print(f"Total Cost:    ${test_metrics['total_cost_usd']:.8f} USD")
