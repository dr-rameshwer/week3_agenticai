"""
Exercise 05: Dynamic Few-Shot Prompt Builder
Course Instructor: Dr. Rameshwer

Task:
Implement a function that programmatically builds a few-shot prompt
from a list of exemplar dictionaries and appends the target query.
"""

from typing import List, Dict

def build_few_shot_prompt(system_task: str, exemplars: List[Dict[str, str]], target_input: str) -> str:
    """Builds a formatted few-shot prompt string.

    Args:
        system_task: Instructions defining the classification task.
        exemplars: List of dicts with keys 'input' and 'output'.
        target_input: The unseen text to classify.

    Returns:
        A complete prompt string ready for LLM invocation.
    """
    prompt_lines = [system_task.strip(), ""]

    # TODO: Iterate through exemplars and append each example block
    for idx, ex in enumerate(exemplars, start=1):
        prompt_lines.append(f"### Example {idx}")
        prompt_lines.append(f"Input: {ex['input']}")
        prompt_lines.append(f"Output: {ex['output']}")
        prompt_lines.append("")

    # TODO: Append the target query
    prompt_lines.append("### Target Query")
    prompt_lines.append(f"Input: {target_input}")
    prompt_lines.append("Output:")

    return "\n".join(prompt_lines)

if __name__ == "__main__":
    demo_task = "Classify the sentiment of student feedback as Positive, Neutral, or Negative."
    demo_examples = [
        {"input": "The lab equipment worked flawlessly.", "output": "Positive"},
        {"input": "The lecture slides were not uploaded on time.", "output": "Negative"}
    ]
    test_target = "The textbook arrived today as scheduled."

    generated_prompt = build_few_shot_prompt(demo_task, demo_examples, test_target)
    print("--- Generated Few-Shot Prompt ---")
    print(generated_prompt)
