import json
import os
from glob import glob

def merge_jsonl_files(jsonl_files, output_file):
    seen_messages = set()
    unique_entries = []

    for file_path in jsonl_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    entry = json.loads(line)
                    message = entry.get("preferred_output", {})[0].get("content")
                    if message not in seen_messages:
                        seen_messages.add(message)
                        unique_entries.append(entry)
                except json.JSONDecodeError:
                    print(f"Skipping invalid JSON in {file_path}: {line.strip()}")

    with open(output_file, 'w', encoding='utf-8') as out_f:
        for entry in unique_entries:
            out_f.write(json.dumps(entry) + '\n')

def build_list():
    file_path = "experts/experts-done.txt"
    jsonl_paths = []

    with open(file_path, 'r', encoding='utf-8') as f:
        for expert in f:
            jsonl_paths.append(f"experts/{expert.strip()}/output.jsonl")
    return jsonl_paths

# Example usage:
paths = build_list()
merge_jsonl_files(paths, "combined_output.jsonl")

# need to also merge with the creative-milkshake info
