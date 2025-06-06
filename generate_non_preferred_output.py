# To run this code, need to run it from python virtual env
# python3 -m venv openai-env
# source openai-env/bin/activate
import json
from openai import OpenAI

client = OpenAI()

def extract_name_and_description(key, transcript, categorization_file_base):
    response = client.responses.create(
        model="gpt-4.1",
        instructions="Given the transcript of an ad, determine the product or service name and what the product or service does. Reply with a dictionary of [brand_name, product_description]",
        input=transcript)

    with open(f"{categorization_file_base}/{key}.txt", "w") as f:
        output = response.output_text + ", " + transcript
        f.write(output)

    return response.output_text

def make_non_preferred_output(name, description):
    response = client.responses.create(
        model="gpt-4.1",
        instructions="Never provide shot directions; only provide the copy for transcripts. Write in a more formal tone.",
        input=f"Write me ad copy for: {name}. Product or service description: {description}",
    )
    return response.output_text

def generate_non_preferred(preferred_output_file, non_preferred_output_file, prompts_file, categorization_file_base):
    # Read the file
    with open(preferred_output_file, "r") as f:
        content = f.read()

    # Parse the list using json.loads()
    data_list = json.loads(content)

    non_preferred = []
    prompts = []
    
    # Iterate over elements
    for i, (key, value) in enumerate(data_list.items()):
        transcript = value
        response = extract_name_and_description(key, transcript, categorization_file_base)
        values = response.split(",")
        print(values)
        
        ## For if it stops midway:
        # with open(f"{categorization_file_base}/{key}.txt", "r") as f:
        #     lines = f.readlines()
        
        # result = lines[0]
        # parts = [part.strip() for part in result.split(",")]

        # name = parts[0]
        # description = ", ".join(parts[1:])

        name = values[0]
        description = values[1]

        non_preferred_script = make_non_preferred_output(name, description)
        non_preferred.append(non_preferred_script)

        prompt = f"Write me the ad copy for a social media ad for {name}. Product description: {description}"
        prompts.append(prompt)
        print(prompt)

    with open(non_preferred_output_file, "w") as f:
        json.dump(non_preferred, f, ensure_ascii=False, indent=2)

    with open(prompts_file, "w") as f:
        json.dump(prompts, f, ensure_ascii=False, indent=2)

# if __name__ == "__main__":
#     preferred_output_file = "creative-milkshake/downloads/beauty/beauty_preferred_output.json"
#     non_preferred_output_file = "creative-milkshake/beauty/beauty_non_preferred_output.txt"
#     prompts_file = "creative-milkshake/beauty_prompts.txt"
#     categorization_file_base = "creative-milkshake/downloads/beauty/transcripts_categorized"

#     generate_non_preferred(preferred_output_file, non_preferred_output_file, prompts_file, categorization_file_base)


