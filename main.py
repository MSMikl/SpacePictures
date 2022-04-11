import os
from pathlib import Path

import requests
from urllib.parse import urlparse


def download_picture(url, path):    
    Path(path).mkdir(parents=True, exist_ok=True)
    response = requests.get(url)
    if response.ok:
        path = Path(path, os.path.basename(url))
        with open(path, 'wb') as file:
            file.write(response.content)
            

def file_extension_check(url):
    return os.path.splitext(urlparse(url).path)[1]
        
        
def fetch_spacex_last_launch():
    response = requests.get('https://api.spacexdata.com/v4/launches/')
    response.raise_for_status()
    launch_data = response.json()
    launch_number = 0
    while not launch_data[launch_number]['links']['flickr']['original']:
        launch_number += 1
    for picture in launch_data[launch_number]['links']['flickr']['original']:
        download_picture(picture, './images/spaceX/')
 

def fetch_nasa_apod(token, count=5):
    params = {'api_key': token, 'count': count}
    response = requests.get('https://api.nasa.gov/planetary/apod', params=params)
    for picture in response.json():
        download_picture(picture['hdurl'], './images/NASA/')
    


def fetch_nasa_epic(token, count=5):
    params = {'api_key': token}
    response = requests.get('https://epic.gsfc.nasa.gov/api/natural', params=params)
    for picture in response.json():
        if count:
            url = 'https://epic.gsfc.nasa.gov/archive/natural/{}/{}/{}/png/{}.png'.format(
                picture['identifier'][:4],
                picture['identifier'][4:6],
                picture['identifier'][6:8],
                picture['image'])
            print(url)
            download_picture(url, './images/NASA/EPIC/')
            count -= 1
        else:
            return
    
if __name__ == '__main__':
    nasa_token = 'pnjMEf1nJ28Ex3YktOmRbmLy9CEMsJMicBu7qHFJ'
    fetch_nasa_epic(nasa_token, 3)