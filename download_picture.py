import os
from pathlib import Path

import requests


def download_picture(url, path):
    response = requests.get(url)
    response.raise_for_status()
    with open(Path(path, os.path.basename(url)), 'wb') as file:
        file.write(response.content)
