# Space Pictures телеграм-бот

Скрипт предназначен для регулярного размещения в Telegram фотографий с сервисов NASA и SpaceX.

В текущей версии скрипта публикуются случайные [Astronomy Picture of the Day](https://apod.nasa.gov/apod/astropix.html). Но в коде также реализованы функции получения фотографий NASA [EPIC](https://epic.gsfc.nasa.gov/) и запусков SpaceX (фотографии запусков с Flickr).

## Установка

Python3 должен быть уже установлен. Затем используйте pip (или pip3, есть есть конфликт с Python2) для установки зависимостей:

`pip install -r requirements.txt`

## Настройка параметров

Для работы скрипта необходимо в папке с ним создать файл `.env`, в котором указать следующие переменные:

1. `NASA_TOKEN =` API-токен сервиса NASA (получить [здесь](https://api.nasa.gov/))
2. `TG_TOKEN =`  API-токен чат-бота Telegram ([как создать чат-бота](https://tlgrm.ru/docs/bots#kak-sozdat-bota)) 
3. `POST_PERIOD = 86400` период публикации в секундах
4. `CHAT_ID =` имя канала или чата, в который будут публиковаться фото

## Запуск

`$ main.py`

```
>>>main.py
Опубликовано фото https://apod.nasa.gov/apod/image/1801/c2016_r2_2018_01_07dpjjc.jpg
Опубликовано фото https://apod.nasa.gov/apod/image/2009/Orion3Ddavison.png
Опубликовано фото https://apod.nasa.gov/apod/image/0201/taurus_orman_lab.jpg
Опубликовано фото https://apod.nasa.gov/apod/image/0903/5hOHPsanterne.jpg
Опубликовано фото https://apod.nasa.gov/apod/image/1801/Helix_CFHT_2000.jpg
Скрипт завершил работу
```
