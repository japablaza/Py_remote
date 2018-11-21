from flask import Flask, render_template

# import requests
import os
import json
import requests
import datetime

# Getting Environ Key for Weather API
WEATHER_KEY = os.environ.get('OPEN_WEATHER')

# Open json file with over 200,000 cities!
# with open ('current.city.list.min.json') as file:
with open ('city.list.json') as file:
    lista =json.load(file) # This is almost 29MB file

# Simple way to get the city ID from JSON file
lista_simple = lista[22]
id_simple = lista_simple.get('id')
country_simple = lista_simple.get('country')
city_simple = lista_simple.get('name')
coord_simple = lista_simple.get('coord')
lon_simple = coord_simple.get('lon')
lat_simple = coord_simple.get('lat')

# Searching for specific city inside the JSON file
for N in range(0, len(lista) -1):
    if lista[N]['country'] == 'US' and lista[N]['name'] == 'Chicago':
        country_search = lista[N]['country']
        id_search = lista[N]['id']
        city_search = lista[N]['name']
        lon_search = lista[N]['coord']['lon']
        lat_search = lista[N]['coord']['lat']

# Building the Endpoint URL API for N city
# http://api.openweathermap.org/data/2.5/weather?id=2951825&units=metric&appid=7a2d438e1e09ea12a9d4c1a12ff46f58
# url_epm: For temperature in Celsius use units=metric
# url_epi: For temperature in Fahrenheit use units=imperial

url_http = 'http://api.openweathermap.org/data/2.5/weather?'
url_id = 'id=' + str(id_search) + '&'
url_metric = 'units=metric&'
url_imperial = 'units=imperial&'
url_key = 'appid=' + str(WEATHER_KEY)
url_epm = url_http + url_id + url_metric + url_key
url_epi = url_http + url_id + url_imperial + url_key

# Get the response from the API endpoint

city_api = requests.get(url_epi) # requests.models.Response
city_data = city_api.json() # dict


current_temp = city_data['main']['temp']
temp_min = city_data['main']['temp_min']
temp_max = city_data['main']['temp_max']
current_time_epoch = city_data['dt']
current_time_local = datetime.datetime.fromtimestamp(current_time_epoch)#.strftime('%a, %d %b %Y %H:%M:%S')


app = Flask(__name__)

@app.route('/')
def hola():
    nombre = 'Jose'
    apellido = 'Apablaza'
    lol = ':: and it is working ::'
    return render_template('hola.html', **locals())


@app.route('/weather')
def weather():
    all_data = [current_temp,
                temp_min,
                temp_max,
                current_time_local,
                city_search,
                lon_search,
                lat_search,
                ]
    return render_template('clima.html', ** locals())

# @app.route('/weather/<ciudad>')
# def weather(ciudad):
#     pass #create this function

if __name__ == '__main__':
    app.run()
