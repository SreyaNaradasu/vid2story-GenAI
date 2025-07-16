import os
import base64
import openai
from dotenv import load_dotenv
from PIL import Image

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def image_to_base64(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

def generate_captions(frames_dir='static/frames'):
    captions = []
    for fname in sorted(os.listdir(frames_dir)):
        if fname.endswith(".jpg"):
            img_b64 = image_to_base64(os.path.join(frames_dir, fname))
            response = openai.ChatCompletion.create(
                model="gpt-4-vision-preview",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": "Describe this image in one sentence."},
                            {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{img_b64}"}}
                        ],
                    }
                ],
                max_tokens=100,
            )
            caption = response["choices"][0]["message"]["content"]
            captions.append(caption)
    return captions
