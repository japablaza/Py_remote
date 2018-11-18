# import requests
import os
import json
import requests
import datetime

# Getting Environ Key for Weather API
WEATHER_KEY = os.environ.get('OPEN_WEATHER')

# Open json file with over 200,000 cities!
with open ('current.city.list.min.json') as file:
    lista =json.load(file) # This is almos 9MB file

# Testing how to get the information from one city
lista0 = lista[14009] #I know it is a city in Germany because I open the file in Firefox :)
id = lista0.get('id')
country = lista0.get('country')
coord = lista0.get('coord')
lon = coord.get('lon')
lat = coord.get('lat')

# Building the Endpoint URL API for N city
# http://api.openweathermap.org/data/2.5/weather?id=2951825&units=metric&appid=7a2d438e1e09ea12a9d4c1a12ff46f58
# url_epm: For temperature in Celsius use units=metric
# url_epi: For temperature in Fahrenheit use units=imperial

url_http = 'http://api.openweathermap.org/data/2.5/weather?'
url_id = 'id=' + str(id) + '&'
url_metric = 'units=metric&'
url_imperial = 'units=imperial&'
url_key = 'appid=' + str(WEATHER_KEY)
url_epm = url_http + url_id + url_metric + url_key
url_epi = url_http + url_id + url_imperial + url_key

# Get the response from the API endpoint

city_api = requests.get(url_epm) # requests.models.Response
city_data = city_api.json() # dict

current_temp = city_data['main']['temp']
temp_min = city_data['main']['temp_min']
temp_max = city_data['main']['temp_max']
current_time_epoch = city_data['dt']
current_time_local = datetime.datetime.fromtimestamp(current_time_epoch).strftime('%c')

# The print section
print('Information from city Bayreuth, DE')
print('ID: ' + str(id))
print('Country: ' + country)
print('Longitud: ' + str(lon))
print('Latitud: ' + str(lat))
print('Current temperature: ' + str(current_temp))
print('Current time: ' + str(current_time_local))
print('Temperature minima: ' + str(temp_min))
print('Temperature maxima: ' + str(temp_max))

# Searching for specific city inside the JSON file

listN = []
for N in range(0, len(lista) -1):
    if lista[N]['country'] == 'US' and lista[N]['name'] == 'New York':
        print(lista[N]['country'])
