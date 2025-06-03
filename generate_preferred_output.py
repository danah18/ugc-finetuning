import re
import json
from vimeo_download import download_vimeo_video
from transcribe import transcribe

def generate_preferred_output(links_file, output_path_base, preferred_output_file, bad_data_file):
    transcripts = {}

    files_not_added = []

    # Read the file
    with open(links_file, "r") as file:
        lines = file.readlines()
        output_path=output_path_base + "%(title)s.%(ext)s"

        for url in lines:
            # Download the video
            download_vimeo_video(url, output_path)
            mp3_filename = url.split('/')[-1].strip()

            # Transcribe and add to array
            transcription = transcribe(output_path_base, mp3_filename)

            if (len(transcription) < 65):
                files_not_added.append(mp3_filename)
            else:
                transcripts[mp3_filename] = transcription.rstrip('\n')

        print("[*****] Files not added: " + str(files_not_added))

    with open(preferred_output_file, "w") as file:
        json.dump(transcripts, file)

    with open(, "w") as file:
        file.write(str(files_not_added))

# if __name__ == "__main__":
#     links_file = "creative-milkshake/beauty-links.txt"
#     output_path_base = "creative-milkshake/downloads/beauty/videos/"
#     preferred_output_file = "creative-milkshake/downloads/beauty/beauty_preferred_output.json"
#     bad_data_file = "creative-milkshake/downloads/beauty/files_not_added.txt"

#     generate_preferred_output(links_file, output_path_base, preferred_output_file, bad_data_file)