import json

<iframe src="https://player.vimeo.com/video/1072475389?controls=0&amp;loop=1&amp;app_id=122963" width="240" height="426" frameborder="0" allow="autoplay; fullscreen; picture-in-picture; clipboard-write; encrypted-media" title="2025 - InFlow" data-ready="true"></iframe>

# Example input with multiple non-preferred outputs
# In JSONL these need to end up being represented as different entries
data = [
    {
        "input": "Explain gravity.",
        "preferred_output": "Gravity is the force that attracts two bodies toward each other.",
        "non_preferred_outputs": [
            "Gravity makes things float.",
            "It's a magical downward wind.",
            "Gravity pulls everything into the sky."
        ]
    },
    # Add more examples here...
]

# Write expanded entries to .jsonl
with open("expanded_dpo_dataset.jsonl", "w", encoding="utf-8") as f:
    for entry in data:
        input_text = entry["input"]
        preferred = entry["preferred_output"]
        for non_pref in entry["non_preferred_outputs"]:
            json.dump({
                "input": input_text,
                "preferred_output": preferred,
                "non_preferred_output": non_pref
            }, f)
            f.write("\n")

Today we're going to be spotlighting the benefits of the adaptogen rhodiola. it offers more focus,
enhanced memory recall and concentration workout stamina and endurance when paired with vitamins b6
B9-b12 magnesium and green tea Rhodiola is shown
To have An impact on mental alertness all while being in a relaxed state giving you energy without
The jitters