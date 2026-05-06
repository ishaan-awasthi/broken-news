from openai import OpenAI
import base64
import os

def generate_caption(image_path):
    client = OpenAI(
        api_key=os.environ.get("XAI_API_KEY"),
        base_url="https://api.x.ai/v1",
    )

    with open(image_path, "rb") as f:
        image_data = base64.standard_b64encode(f.read()).decode("utf-8")

    response = client.chat.completions.create(
        model="grok-4.3",
        max_tokens=300,
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_data}",
                        },
                    },
                    {
                        "type": "text",
                        "text": open("prompt.txt").read(),
                    },
                ],
            }
        ],
    )

    print("Got caption from Grok!")
    return response.choices[0].message.content.strip()