print("Starting process")

from dotenv import load_dotenv
load_dotenv()

from scraper import fetch_image
from inference import generate_caption
from web import make_post

if __name__ == '__main__':
    print("Really starting process")

    image = fetch_image()
    caption = generate_caption(image)
    make_post(caption, image)

    print()
    print("kthxbai")