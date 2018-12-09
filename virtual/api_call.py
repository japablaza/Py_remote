# import requests
import os
import json
import requests
import datetime
import random

# Getting Environ Key for Weather API
WEATHER_KEY = os.environ.get('OPEN_WEATHER')

# Open json file with over 200,000 cities!
# with open ('current.city.list.min.json') as file:
with open ('city.list.json') as file:
    lista =json.load(file) # This is almost 29MB file

# Searching for specific city inside the JSON file
def city_func(city_func, country_func):
    for dict_in in lista:
        dict_values = dict_in.values()
        for value in dict_values:
            if value == city_func:
                if dict_in['country'] == country_func:
                    return dict_in

# Building the Endpoint URL API for N city
# http://api.openweathermap.org/data/2.5/weather?id=2951825&units=metric&appid=7a2d438e1e09ea12a9d4c1a12ff46f58
# url_epm: For temperature in Celsius use units=metric
# url_epi: For temperature in Fahrenheit use units=imperial

def api_call_func(city, country):
    url_http = 'http://api.openweathermap.org/data/2.5/weather?'
    url_id = 'id=' + str(city_func(city, country)['id']) + '&'
    url_metric = 'units=metric&'
    url_imperial = 'units=imperial&'
    url_key = 'appid=' + str(WEATHER_KEY)
    url_epm = url_http + url_id + url_metric + url_key
    url_epi = url_http + url_id + url_imperial + url_key
    return url_epi

# Get the response from the API endpoint

def api_call_func_to_JSON(city, country):
    city_api = requests.get(api_call_func(city, country)) # requests.models.Response
    city_data = city_api.json() # dict
    return city_data

# current_temp = city_data['main']['temp']
# temp_min = city_data['main']['temp_min']
# temp_max = city_data['main']['temp_max']
# current_time_epoch = city_data['dt']
# current_time_local = datetime.datetime.fromtimestamp(current_time_epoch)#.strftime('%a, %d %b %Y %H:%M:%S')

# Adding free photos api endpoint functions

PIXABAY_KEY = os.environ.get('OPEN_PIXABAY')

def photos(city):
    url_pixabay = 'https://pixabay.com/api/?key='
    url_pixabay_key = str(PIXABAY_KEY)
    url_pixabay_city = '&q=' + city + '+city&image_type=photo&pretty=true'
    url_photos = url_pixabay + url_pixabay_key + url_pixabay_city
    return url_photos

def photos_jason(city):
    photos_api = requests.get(photos(city))
    photos_data = photos_api.json()
    return photos_data

def random_photo(city):
    # totalHits = photos_jason(city)['totalHits']
    numR = random.randint(0,15)
    random_foto = photos_jason(city)['hits'][numR]['largeImageURL']
    return random_foto
