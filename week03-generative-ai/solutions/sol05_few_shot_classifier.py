"""
Solution 05: Dynamic Few-Shot Prompt Builder
Course Instructor: Dr. Rameshwer

Reference Solution for Exercise 05.
"""

from typing import List, Dict

def build_few_shot_prompt(system_task: str, exemplars: List[Dict[str, str]], target_input: str) -> str:
    prompt_lines = [system_task.strip(), ""]
    for idx, ex in enumerate(exemplars, start=1):
        prompt_lines.append(f"### Example {idx}")
        prompt_lines.append(f"Input: {ex['input']}")
        prompt_lines.append(f"Output: {ex['output']}")
        prompt_lines.append("")

    prompt_lines.append("### Target Query")
    prompt_lines.append(f"Input: {target_input}")
    prompt_lines.append("Output:")

    return "\n".join(prompt_lines)

if __name__ == "__main__":
    task = "Classify campus support tickets."
    examples = [{"input": "Wi-Fi is down", "output": "Infrastructure"}]
    print(build_few_shot_prompt(task, examples, "Projector broken"))
