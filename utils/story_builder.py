import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def build_story(captions, transcript):
    prompt = (
        "You are a creative storyteller. Using the following image captions and transcript from a short video, "
        "generate a coherent, emotional short story.

"
        f"Image Captions:
{captions}

"
        f"Transcript:
{transcript}

"
        "Story:"
    )
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=500
    )
    return response['choices'][0]['message']['content']
