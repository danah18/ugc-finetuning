import json
import os
from glob import glob
from langdetect import detect
from openai import OpenAI
from collections import Counter

def merge_jsonl_files(jsonl_files, output_file):
    client = OpenAI()
    seen_messages = set()
    seen_pretranslation = set()
    unique_entries = []

    for file_path in jsonl_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                try:
                    entry = json.loads(line)
                    preferred_output = entry.get("preferred_output", [])
                    if not preferred_output or not isinstance(preferred_output, list):
                        continue

                    message = preferred_output[0].get("content")
                    if not message:
                        continue

                    language = detect(message)

                    # Skip if message already seen
                    if language == "en":
                        if message in seen_messages:
                            continue
                        seen_messages.add(message)

                        # Check for similarity
                        too_similar = False
                        for existing_entry in unique_entries:
                            percent, _ = common_words_percentage_total(message, existing_entry)
                            if percent > 85:
                                print(f"Ignoring {percent}%: {message}")
                                too_similar = True
                                break

                        if not too_similar:
                            unique_entries.append(entry)
                    else:
                        if message in seen_pretranslation:
                            continue
                        seen_pretranslation.add(message)

                        # Translate
                        response = client.responses.create(
                            model="gpt-4.1",
                            instructions=f"Translate this ad from {language} to English. Only reply with the translation, do not reply with any extra content",
                            input=message
                        )
                        translated = response.output_text.strip()

                        if translated in seen_messages:
                            continue
                        seen_messages.add(translated)

                        # Build translated entry clone
                        translated_entry = entry.copy()
                        translated_entry["preferred_output"][0]["content"] = translated

                        too_similar = False
                        for existing_entry in unique_entries:
                            percent, _ = common_words_percentage_total(translated, existing_entry)
                            if percent > 85:
                                too_similar = True
                                print(f"Ignoring {percent}%: {translated}")
                                break

                        if not too_similar:
                            unique_entries.append(translated_entry)

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


def common_words_percentage_total(text1, entry2):
    text2 = entry2.get("preferred_output", [])[0].get("content", "")
    words1 = text1.lower().split()
    words2 = text2.lower().split()

    counter1 = Counter(words1)
    counter2 = Counter(words2)

    common = counter1 & counter2
    total_common = sum(common.values())

    average_len = (len(words1) + len(words2)) / 2
    percentage = (total_common / average_len) * 100 if average_len > 0 else 0

    return percentage, dict(common)

# Example usage:
# paths = build_list()
paths = ['all-creative-milkshake.jsonl', 'almost-all-experts.jsonl', 'combined_output.jsonl']
merge_jsonl_files(paths, "all-experts.jsonl")

# need to also merge with the creative-milkshake info + the og combined-outptu

# x = "Discover how to remove shadow banning on Instagram. Posts hidden for buying followers and using too many hashtags. I found a way to grow my page without looking like spam—PathSocial. I signed up, used their guide to reach my niche audience, and now my posts have a lot of engagement. It's nice to see real followers enjoying what I post instead of bots ruining my social media engagement. The growth was almost automatic, incredible. I'm impressed with PathSocial, I wish I had found it sooner. There’s an easier way to grow on IG. Sign up today."
# y = "Discover how to remove shadowbanning on Instagram. Posts get hidden for buying followers and using too many hashtags. I found a way to grow my page without looking like spam: Path Social. I signed up, used their guide to reach my niche audience, and now my posts get a lot of engagement. It’s nice to see real followers enjoying what I share instead of bots ruining my social media engagement. The growth was almost automatic. Amazing. Impressed with Path Social—I wish I’d found it sooner. There’s an easier way to grow on IG. Sign up today."
# (p,c) = common_words_percentage_total(x, y)
# print(p)
# print(c)