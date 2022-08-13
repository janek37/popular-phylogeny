import time
from io import BytesIO
from os import makedirs

import requests
from PIL import Image, UnidentifiedImageError

from clade import BaseClade, Clade, Species
from data import LIFE


def make_thumbnails(clade: BaseClade):
    if isinstance(clade, Species):
        make_thumbnail(clade)
    elif isinstance(clade, Clade):
        for child in clade.children:
            make_thumbnails(child)


def make_thumbnail(species: Species):
    url = get_thumbnail_url(species.image.image_url)
    print(species.name, url, sep="\t")
    wait = 1
    while True:
        try:
            image = open_image(url)
            ext = url.rsplit(".", 1)[-1]
            image.save(f"thumbnails/{species.name}.{ext}")
            break
        except UnidentifiedImageError:
            print("retrying...")
            time.sleep(wait)
            wait *= 2


def get_thumbnail_url(image_url: str) -> str:
    filename = image_url.rsplit("/", 1)[-1]
    extension = filename.rsplit(".", 1)[-1]
    if extension not in ["jpg", "JPG", "jpeg", "JPEG", "png", "PNG", "gif", "GIF"]:
        filename += ".jpg"
    return image_url.replace("/commons/", "/commons/thumb/") + "/300px-" + filename


def open_image(url: str):
    response = requests.get(
        url,
        headers={
            "User-Agent": "popular-phylogeny/1.0; (https://github.com/janek37/popular-phylogeny)"
        },
    )
    return Image.open(BytesIO(response.content))


if __name__ == "__main__":
    makedirs("thumbnails", exist_ok=True)
    make_thumbnails(LIFE)
