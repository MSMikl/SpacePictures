import os
from pathlib import Path

import requests
import telegram
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
    result_list = []
    for picture in response.json():
        if picture['hdurl']:
            download_picture(picture['hdurl'], './images/NASA/')
            result_list.append(picture['hdurl'])
    return result_list    


def fetch_nasa_epic(token, count=5):
    params = {'api_key': token}
    response = requests.get('https://epic.gsfc.nasa.gov/api/natural', params=params)
    result_list = []
    for picture in response.json():
        if count:
            url = 'https://epic.gsfc.nasa.gov/archive/natural/{}/{}/{}/png/{}.png'.format(
                picture['identifier'][:4],
                picture['identifier'][4:6],
                picture['identifier'][6:8],
                picture['image'])
            download_picture(url, './images/NASA/EPIC/')
            count -= 1
            result_list.append(url)
        else:
            break
    return result_list

    
if __name__ == '__main__':
    nasa_token = 'pnjMEf1nJ28Ex3YktOmRbmLy9CEMsJMicBu7qHFJ'
    telegram_token = '5218325640:AAGfAiFpY-2J4ChJAZ6I1KbTLxuR5Jj_6Fg'
    tbot = telegram.Bot(token=telegram_token)
    tbot.send_photo(photo=fetch_nasa_apod(nasa_token)[0], chat_id=176649151)
    