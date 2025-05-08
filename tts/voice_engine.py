import os
import time
from dotenv import load_dotenv
from elevenlabs import ElevenLabs, play

load_dotenv()
client = ElevenLabs(api_key=os.getenv("ELEVEN_API_KEY"))

def speak_text(text):
    audio = client.generate(
        text=text,
        voice="Anime GF",  # Replace with your custom voice if needed
        model="eleven_monolingual_v1"
    )
    words = text.split()
    play(audio)
    for word in words:
        print(word, end=' ', flush=True)
        time.sleep(0.2)
    print()

    
    