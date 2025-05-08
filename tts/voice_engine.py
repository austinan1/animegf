from elevenlabs import generate, play, set_api_key
import os
from dotenv import load_dotenv

load_dotenv()
set_api_key(os.getenv("ELEVEN_API_KEY"))

def speak(text):
    audio = generate(
        text=text,
        voice="Rachel",  # You can change this to a custom voice ID
        model="eleven_monolingual_v1"
    )
    play(audio)