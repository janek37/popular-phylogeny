import os.path
import time
import urllib.parse
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
    url = species.image.get_thumbnail_url()
    filename = urllib.parse.unquote(url.rsplit("/", 1)[-1])
    output_filename = f"thumbnails/{filename}"
    if os.path.exists(output_filename):
        return
    print(species.name, url, sep="\t")
    wait = 1
    while True:
        try:
            image = open_image(url)
            image.save(output_filename)
            break
        except UnidentifiedImageError:
            print("retrying...")
            time.sleep(wait)
            wait *= 2


def open_image(url: str):
    response = requests.get(
        url,
        headers={
            "User-Agent": "popular-phylogeny/1.0; (https://github.com/janek37/popular-phylogeny)"
        },
    )
    return Image.open(BytesIO(response.content))


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        os.chdir(sys.argv[1])
    makedirs("thumbnails", exist_ok=True)
    make_thumbnails(LIFE)
