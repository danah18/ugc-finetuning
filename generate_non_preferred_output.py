# To run this code, need to run it from python virtual env
# python3 -m venv openai-env
# source openai-env/bin/activate
import json
from openai import OpenAI

client = OpenAI()

def extract_name_and_description(index, transcript):
    response = client.responses.create(
        model="gpt-4.1",
        instructions="Given the transcript of an ad, determine the product or service name and what the product or service does. Reply a comma-separated list of [brand_name, product_description]",
        input=transcript)

    with open(f"creative-milkshake/downloads/beauty/transcripts_categorized/{index}.txt", "w") as f:
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

def generate(preferred_output_file):
    # Read the file
    with open(preferred_output_file, "r") as f:
        content = f.read()

    # Parse the list using json.loads()
    data_list = json.loads(content)

    non_preferred = []
    
    # Iterate over elements
    for index, value in enumerate(data_list):
        transcript = value
        response = extract_name_and_description(index, transcript)
        values = response.split(",")

        name = values[0]
        description = values[1]

        non_preferred_script = make_non_preferred_output(name, description)

        non_preferred.append(non_preferred_script)

    with open(f"creative-milkshake/beauty_non_preferred_output.txt", "w") as f:
        json.dump(non_preferred, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    generate("creative-milkshake/beauty_preferred_output.txt")







