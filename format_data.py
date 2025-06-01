import json

# Example data
data = [
    {
        "input": "What is the capital of France?",
        "preferred_output": "The capital of France is Paris.",
        "non_preferred_output": "France doesn't have a capital."
    },
    # Add more examples here...
]

# Write to .jsonl
with open("dpo_dataset.jsonl", "w", encoding="utf-8") as f:
    for entry in data:
        json.dump(entry, f)
        f.write("\n")

