import requests

from download_picture import download_picture


def fetch_nasa_apod(token, count=5, download=True):
    params = {'api_key': token, 'count': count}
    response = requests.get(
        'https://api.nasa.gov/planetary/apod',
        params=params)
    result_links = []
    for picture in response.json():
        try:
            result_links.append(picture['hdurl'])
            if download:
                download_picture(picture['hdurl'], './images/NASA/')
        except:
            continue
    return result_links


def fetch_nasa_epic(token, count=5, download=True):
    params = {'api_key': token}
    response = requests.get(
        'https://epic.gsfc.nasa.gov/api/natural',
        params=params)
    result_links = []
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
            result_links.append(url)
        else:
            break
    return result_links
