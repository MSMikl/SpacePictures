import requests

from download_picture import download_picture


def fetch_spacex_last_launch(download=True):
    response = requests.get('https://api.spacexdata.com/v4/launches/')
    response.raise_for_status()
    launch_data = response.json()
    launch_number = 0
    result_list = []
    while not launch_data[launch_number]['links']['flickr']['original']:
        launch_number += 1
    for url in launch_data[launch_number]['links']['flickr']['original']:
        if download:
            download_picture(url, './images/spaceX/')
        result_list.append(url)
