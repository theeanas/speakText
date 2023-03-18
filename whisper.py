import os
from pydub import AudioSegment
import openai
from youtubesearchpython import *

openai.api_key = os.getenv("OPENAI_API_KEY")

# PyDub handles time in milliseconds
twenty_minutes = 20 * 60 * 1000

podcast = AudioSegment.from_mp3("yasser.mp3")

# Whisper's API can only take 25MB of audio.
# todo: fix it to loop through.
first_20_minutes = podcast[:twenty_minutes]
first_20_minutes.export("yasser0_20.mp3", format="mp3")

audio_file= open("yasser0_20.mp3", "rb")

# Talk to the Whisper API
transcript = openai.Audio.transcribe(model="whisper-1", file=audio_file, response_format="text", language="ar")
print(transcript)

output_file = open("yasser-output.txt", "w")
output_file.write(transcript.text)
# todo: write the logic that segments and feeds into Whisper.
