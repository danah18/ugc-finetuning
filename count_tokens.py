import json
import tiktoken

def count_tokens_in_jsonl(jsonl_path, model="gpt-4o"):
    encoding = tiktoken.encoding_for_model(model)
    total_tokens = 0
    total_lines = 0

    with open(jsonl_path, 'r', encoding='utf-8') as f:
        for line in f:
            total_lines += 1
            try:
                item = json.loads(line)
                
                # Extract and flatten all messages into one string
                messages = item.get("input", {}).get("messages", [])
                prompt_text = " ".join(msg.get("content", "") for msg in messages)

                # Extract chosen and rejected completions
                chosen = item.get("preferred_output", [{}])[0].get("content", "")
                rejected = item.get("non_preferred_output", [{}])[0].get("content", "")

                # Tokenize each part
                prompt_tokens = encoding.encode(prompt_text)
                chosen_tokens = encoding.encode(chosen)
                rejected_tokens = encoding.encode(rejected)

                total_tokens += len(prompt_tokens) + len(chosen_tokens) + len(rejected_tokens)
            
            except Exception as e:
                print(f"Error on line {total_lines}: {e}")

    print(f"Total lines: {total_lines}")
    print(f"Estimated tokens: {total_tokens}")

# Example usage
count_tokens_in_jsonl("all-experts.jsonl", model="gpt-4o")

# Total lines: 1328
# Estimated tokens: 440508