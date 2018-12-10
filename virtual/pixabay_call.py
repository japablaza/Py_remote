import os
import json
import requests


PIXABAY_KEY = os.environ.get('OPEN_PIXABAY')

def photos(city):
    url_pixabay = 'https://pixabay.com/api/?key='
    url_pixabay_key = str(PIXABAY_KEY)
    url_pixabay_city = '&q=' + city + '+city&image_type=photo&pretty=true'
    url_photos = url_pixabay + url_pixabay_key + url_pixabay_city
    return url_photos

def photos_JSON(city):
    photos_api = requests.get(photos(city))
    photos_data = photos_api.json()
    return photos_data


# print(photos('Chicago'))
# print(photos_JSON('Chicago')['hits'][1]['largeImageURL'])
# print(photos_JSON('New York'))
# print(photos_JSON("New York"))
