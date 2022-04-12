import os
import time

import telegram
from dotenv import load_dotenv
from urllib.parse import urlparse

from fetch_spacex import fetch_spacex_last_launch
from fetch_nasa import fetch_nasa_apod, fetch_nasa_epic 
          

def file_extension_check(url):
    return os.path.splitext(urlparse(url).path)[1]

    
if __name__ == '__main__':
    load_dotenv()
    nasa_token = os.getenv('NASA_TOKEN')
    telegram_token = os.getenv('TG_TOKEN')
    delay = int(os.getenv('POST_PERIOD'))
    chat_id = os.getenv('CHAT_ID')
    tbot = telegram.Bot(token=telegram_token)
    post_list = fetch_nasa_apod(nasa_token, count=1, download=False)
    for picture in post_list:
        try:
            tbot.send_photo(photo=picture, chat_id=chat_id)
            time.sleep(delay)
        except:
            continue
