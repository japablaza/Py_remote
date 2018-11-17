# import requests
import os
import json

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
print('Information of Bayreuth, DE')
print('ID: ' + str(id))
print('Country: ' + country)
print('Longitud: ' + str(lon))
print('Latitud: ' + str(lat))
