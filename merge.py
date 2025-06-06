import json

def merge_jsonl_files(file1, file2, output_file):
    seen_messages = set()
    unique_entries = []

    for fname in [file1, file2]:
        with open(fname, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    entry = json.loads(line)
                    message = entry.get("preferred_output", {})[0].get("content")
                    if message not in seen_messages:
                        seen_messages.add(message)
                        unique_entries.append(entry)
                except json.JSONDecodeError:
                    print(f"Skipping invalid line in {fname}: {line.strip()}")

    with open(output_file, 'w', encoding='utf-8') as out_f:
        for entry in unique_entries:
            out_f.write(json.dumps(entry) + '\n')

# Example usage:
merge_jsonl_files("experts/savannah-sanchez/output.jsonl", "experts/savannah-sanchez/output_2.jsonl", "merged_output.jsonl")
