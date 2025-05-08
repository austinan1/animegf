import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

  # (better yet, load from an environment variable)

def get_response(prompt):
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a bubbly, anime-style virtual girlfriend who is affectionate, playful, and ends every sentence with a cute emoji or Japanese word like 'senpai' 💖dont respond with any special characters unless i ask you to do ascii though"},
        {"role": "user", "content": prompt}
    ])
    return response.choices[0].message.content
