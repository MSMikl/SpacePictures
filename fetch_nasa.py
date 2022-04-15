import datetime
import requests

from download_picture import download_picture


def fetch_nasa_apod(token, count=5, download=True):
    params = {'api_key': token, 'count': count}
    response = requests.get(
        'https://api.nasa.gov/planetary/apod',
        params=params)
    result_links = []
    for picture in response.json():
        if picture['hdurl']:
            if download:
                try:
                    download_picture(picture['hdurl'], './images/NASA/')
                except requests.exceptions.ConnectionError:
                    print('Невозможно скачать картинку по ссылке', picture['hdurl'])
                    continue
                except requests.exceptions.MissingSchema:
                    print(picture['hdurl'], 'не является ссылкой')
                    continue
            result_links.append(picture['hdurl'])
    return result_links


def fetch_nasa_epic(token, count=5, download=True):
    params = {'api_key': token}
    response = requests.get(
        'https://epic.gsfc.nasa.gov/api/natural',
        params=params)
    result_links = []
    for picture in response.json():
        if count:
            date = datetime.datetime.strptime(picture['identifier'], '%Y%m%d%f')
            url = 'https://epic.gsfc.nasa.gov/archive/natural/{}/{:02d}/{:02d}/png/{}.png'.format(
                date.year,
                date.month,
                date.day,
                picture['image'])
            if download:
                download_picture(url, './images/NASA/EPIC/')
            count -= 1
            result_links.append(url)
        else:
            break
    return result_links
