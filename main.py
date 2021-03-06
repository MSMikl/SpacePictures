import logging
import os
import time

import telegram
from dotenv import load_dotenv
from urllib.parse import urlparse

from fetch_spacex import fetch_spacex_last_launch
from fetch_nasa import fetch_nasa_apod, fetch_nasa_epic


def get_file_extension(url):
    return os.path.splitext(urlparse(url).path)[1]


if __name__ == '__main__':
    logging.basicConfig(filename="work.log", level=logging.INFO)
    load_dotenv()
    nasa_token = os.getenv('NASA_TOKEN')
    telegram_token = os.getenv('TG_TOKEN')
    delay = int(os.getenv('POST_PERIOD'))
    chat_id = os.getenv('CHAT_ID')
    tbot = telegram.Bot(token=telegram_token)
    post_links = fetch_nasa_apod(nasa_token, count=5, download=False)
    for picture_link in post_links:
        try:
            tbot.send_photo(photo=picture_link, chat_id=chat_id)
        except telegram.error.BadRequest:
            logging.error('{} : Некорректная ссылка {}',format(
                str(time.ctime()),
                picture_link
                )
            )
            continue
        logging.info('{}: Опубликовано фото {}'.format(
            str(time.ctime()),
            picture_link
            )
        )
        time.sleep(delay)
    logging.info('{}: Скрипт завершил работу'.format(str(time.ctime())))
