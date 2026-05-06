from atproto import Client, models
import os

def make_client():
    client = Client(base_url="https://bsky.social")
    client.login(
        os.environ.get("BSKY_HANDLE"),
        os.environ.get("BSKY_PASSWORD"),
    )
    return client

def make_post(text, image_path):
    client = make_client()

    embed = None
    if image_path:
        with open(image_path, "rb") as f:
            img_data = f.read()

        upload = client.upload_blob(img_data)

        embed = models.AppBskyEmbedImages.Main(
            images=[
                models.AppBskyEmbedImages.Image(
                    image=upload.blob,
                    alt=text,
                )
            ]
        )

    print("Made the post!")
    return client.send_post(text=text, embed=embed)