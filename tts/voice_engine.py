import os
import time
import threading
from dotenv import load_dotenv
from elevenlabs import ElevenLabs, play, stream

load_dotenv()
client = ElevenLabs(api_key=os.getenv("ELEVEN_API_KEY"))

def speak_text(text):
    audio = client.generate(
        text=text,
        voice="LS4IY3ZgosBoEhqMPpkb",  # Replace with your custom voice if needed
        model="eleven_monolingual_v1",
        stream = True
    )

    def display_words():
        words = text.split()
        delay = 0.2  # Time between words; tweak to match voice speed
        time.sleep(0.1)
        for word in words:
            print(word, end=' ', flush=True)
            time.sleep(delay)
        print()  # Newline after message

    display_thread = threading.Thread(target=display_words)
    display_thread.start()

    play(audio)
    display_thread.join()
    
    
    