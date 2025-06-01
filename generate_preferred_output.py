import re
from vimeo_download import download_vimeo_video
from transcribe import transcribe

transcripts = []

# Read the file
with open("creative-milkshake/beauty-links.txt", "r") as file:
    lines = file.readlines()
    output_path_base = "creative-milkshake/downloads/beauty/"
    output_path=output_path_base + "%(title)s.%(ext)s"

    for url in lines:
        # Download the video
        download_vimeo_video(url, output_path)
        mp3_filename = url.split('/')[-1].strip()

        # Transcribe and add to array
        transcription = transcribe(output_path_base, mp3_filename)
        transcripts.append(transcription.rstrip('\n'))

with open("creative-milkshake/beauty_preferred_output.txt", "w") as file:
    file.write(str(transcripts))

# write the array to a text file: creative-milkshake/beauty_non_preferred_output.txt 
# use the text files to create non-preferred output, don't call openai anymore