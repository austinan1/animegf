import os
from dotenv import load_dotenv
from elevenlabs import ElevenLabs, play

load_dotenv()

# Initialize the ElevenLabs client
client = ElevenLabs(
    api_key=os.getenv("ELEVEN_API_KEY")
)

def speak_text(text):
    audio = client.generate(
        text=text,
        voice="Rachel",  # Replace with your custom voice if needed
        model="eleven_monolingual_v1"
    )
    play(audio)