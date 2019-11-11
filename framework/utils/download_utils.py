import base64

import requests

from framework.utils.logger import info


def download_file(url, path):
    info(f"Downloading file from {url} and saving in {path}")
    with open(path, "wb") as download_file:
        download_file.write(requests.get(url).content)


def decode_base64_to_file(url, path):
    image_data = base64.b64decode(url)
    with open(path, 'wb') as f:
        f.write(image_data)
