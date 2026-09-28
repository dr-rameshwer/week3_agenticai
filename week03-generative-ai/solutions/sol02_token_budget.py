"""
Solution 02: Token Budget & Cost Calculator
Course Instructor: Dr. Rameshwer

Reference Solution for Exercise 02.
"""

def calculate_token_cost(prompt_tokens: int, candidate_tokens: int) -> dict:
    total_tokens = prompt_tokens + candidate_tokens
    input_cost = (prompt_tokens / 1_000_000.0) * 0.075
    output_cost = (candidate_tokens / 1_000_000.0) * 0.30
    total_cost = input_cost + output_cost

    return {
        "prompt_tokens": prompt_tokens,
        "candidate_tokens": candidate_tokens,
        "total_tokens": total_tokens,
        "total_cost_usd": round(total_cost, 8)
    }

if __name__ == "__main__":
    report = calculate_token_cost(450, 850)
    print("--- Reference Solution 02 Report ---")
    print(report)
