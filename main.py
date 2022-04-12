import os
import time
from pathlib import Path

import requests
import telegram
from dotenv import load_dotenv
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
 

def fetch_nasa_apod(token, count=5, download=True):
    params = {'api_key': token, 'count': count}
    response = requests.get('https://api.nasa.gov/planetary/apod', params=params)
    result_list = []
    for picture in response.json():
        try:
            if download:
                download_picture(picture['hdurl'], './images/NASA/')
            result_list.append(picture['hdurl'])
        except:
            print('skip')
            continue
    return result_list    


def fetch_nasa_epic(token, count=5, download=True):
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
            if download:
                download_picture(url, './images/NASA/EPIC/')
            count -= 1
            result_list.append(url)
        else:
            break
    return result_list

    
if __name__ == '__main__':
    load_dotenv()
    nasa_token = os.getenv('NASA_TOKEN')
    telegram_token = os.getenv('TG_TOKEN')
    delay = int(os.getenv('POST_PERIOD'))
    chat_id = os.getenv('CHAT_ID')
    tbot = telegram.Bot(token=telegram_token)
    post_list = fetch_nasa_apod(nasa_token, count=5, download=False)
    for picture in post_list:
        try:
            tbot.send_photo(photo=picture, chat_id=chat_id)
            time.sleep(delay)
        except:
            print('Error')
            continue
