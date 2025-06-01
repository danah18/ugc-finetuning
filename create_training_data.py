import json

# Define your data as a list of dictionaries
def make_json_object(user_prompt, preferred_output, non_preferred_output):
    json_object = {
        "input": {
            "messages": [
                {"role": "system", "content": "You are a copywriter at an ad agency that specializes in social media ads for TikTok and Instagram. You specialize in creating ads in the style of user-generated content, which are ads that appear to be organically created by individuals that use the product or service."},
                {"role": "user", "content": user_prompt} 
            ]
        },
        "preferred_output": [
            {"role": "assistant", "content": preferred_output}
        ],
        "non_preferred_output": [
            {"role": "assistant", "content": non_preferred_output}
        ]
    }

    return json_object

def generate_jsonl():
    preferred_output_file = "creative-milkshake/beauty_preferred_output.txt"
    non_preferred_output_file = "creative-milkshake/beauty_non_preferred_output.txt"
    prompt_file = "creative-milkshake/beauty_prompts.txt"

    data = []

    # Read contents of preferred output
    with open(preferred_output_file, "r") as f:
        preferred_output_content = f.read()
    preferred_output = json.loads(preferred_output_content)

    # Read contents of non preferred output
    with open(non_preferred_output_file, "r") as f:
        non_preferred_output_content = f.read()
    non_preferred_output = json.loads(non_preferred_output_content)

    # Read contents of prompts
    with open(prompt_file, "r") as f:
        prompt_content = f.read()
    prompts = json.loads(prompt_content)

    # Create an index iterator and use what's accessed to make json object
    for i in range(len(preferred_output)):
        result = make_json_object(prompts[i], preferred_output[i], non_preferred_output[i])
        data.append(result)

    # Write to a .jsonl file
    with open("creative-milkshake/beauty.jsonl", "w") as f:
        for item in data:
            json.dump(item, f)
            f.write("\n")

if __name__ == "__main__":
    generate_jsonl()

# make_prompt alongside non_preferred_output generation
# Write me the ad copy for a social media ad for the Inala Power Potion. It is a beauty product focused on growing hair. 