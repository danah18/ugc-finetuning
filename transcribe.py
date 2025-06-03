# To run this code, need to run it from python virtual env
# python3 -m venv openai-env
# source openai-env/bin/activate
import os
from openai import OpenAI
from openai import InternalServerError
from langdetect import detect

def transcribe(download_directory, mp3_filename):
    transcript_file_name = "creative-milkshake/downloads/beauty/transcripts/" + mp3_filename.split('.')[0] + ".txt"

    if os.path.exists(transcript_file_name):
        with open(transcript_file_name, 'r') as f:
            return f.read()
    else:
        client = OpenAI()
        download_path = download_directory + mp3_filename
        audio_file = open(download_path, "rb")

        try:
            transcription = client.audio.transcriptions.create(
                model="gpt-4o-transcribe", 
                file=audio_file, 
                response_format="text"
            )   

            if (len(transcription) > 65):
                language = detect(transcription)

                if language == "en":
                    with open(transcript_file_name, "a") as transcript_file:
                        transcript_file.write(transcription)
                else:
                    response = client.responses.create(
                        model="gpt-4.1",
                        instructions=f"Given the transcript of an ad, translate it from {language} to English. Reply only with the translated transcript.",
                        input=transcription)

                    with open(transcript_file_name, "a") as transcript_file:
                        transcript_file.write(response.output_text)
                    
        except InternalServerError:
            return ""

        return transcription