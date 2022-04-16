import requests

from download_picture import download_picture


def fetch_spacex_last_launch(download=True):
    response = requests.get('https://api.spacexdata.com/v4/launches/')
    response.raise_for_status()
    launch_data = response.json()
    result_links = []
    for launch in launch_data:
        if not launch['links']['flickr']['original']:
            continue
        for url in launch['links']['flickr']['original']:
            if download:
                download_picture(url, './images/spaceX/')
            result_links.append(url)
    return result_links