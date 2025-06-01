# To run this code, need to run it from python virtual env
# python3 -m venv openai-env
# source openai-env/bin/activate

from openai import OpenAI

def transcribe(download_directory, mp3_filename):
    client = OpenAI()
    download_path = download_directory + mp3_filename
    audio_file = open(download_path, "rb")

    transcription = client.audio.transcriptions.create(
         model="gpt-4o-transcribe", 
         file=audio_file, 
         response_format="text"
    )   

    transcript_file_name = "creative-milkshake/downloads/beauty/transcripts/" + mp3_filename.split('.')[0] + ".txt"

    with open(transcript_file_name, "a") as transcript_file:
        transcript_file.write(transcription)

    return transcription