import json
from generate_non_preferred import generate_non_preferred
from generate_preferred_output import generate_preferred_output

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

def generate_jsonl(preferred_output_file, non_preferred_output_file, prompt_file, output_jsonl_file):
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
    for i, (key, value) in enumerate(preferred_output.items()):
        result = make_json_object(prompts[i], value, non_preferred_output[i])
        data.append(result)

    # Write to a .jsonl file
    with open("creative-milkshake/beauty.jsonl", "w") as f:
        for item in data:
            json.dump(item, f)
            f.write("\n")

def get_paths(author):
    paths = {}

    paths["links_file"] = f"{author}/remaining/links.txt"
    paths["output_path_base"] = f"{author}/downloads/videos/"
    paths["preferred_output_file"] = f"{author}/downloads/preferred_output.json"
    paths["bad_data_file"] = f"{author}/downloads/files_not_added.txt"
    paths["non_preferred_output_file"] =  f"{author}/non_preferred_output.txt"
    paths["prompts_file"] =  f"{author}/prompts.txt"
    paths["categorization_file_base"] =  f"{author}/downloads/transcripts_categorized"
    oaths["output_jsonl_file"] = f"{author}/output.jsonl"
    
    return paths

if __name__ == "__main__":
    paths = get_paths("creative-milkshake")

    links_file = paths["links_file"]
    output_path_base = paths["output_path_base"]
    preferred_output_file = paths["preferred_output_file"]
    bad_data_file = paths["bad_data_file"]

    generate_preferred_output(links_file, output_path_base, preferred_output_file, bad_data_file)

    non_preferred_output_file = paths["non_preferred_output_file"]
    prompts_file = paths["prompts_file"]
    categorization_file_base = paths["categorization_file_base"]

    generate_non_preferred(preferred_output_file, non_preferred_output_file, prompts_file, categorization_file_base)

    output_jsonl_file = paths["output_jsonl_file"]
    generate_jsonl(preferred_output_file, non_preferred_output_file, prompt_file, output_jsonl_file)

    # TODO: remove remaining from directory above
    # TODO: concanetate jsonfile files