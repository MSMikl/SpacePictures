import os
from pathlib import Path

import requests


def download_picture(url, path):
    Path(path).mkdir(parents=True, exist_ok=True)
    response = requests.get(url)
    if response.ok:
        path = Path(path, os.path.basename(url))
        with open(path, 'wb') as file:
            file.write(response.content)
    return
