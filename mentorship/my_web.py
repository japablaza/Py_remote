from flask import Flask, render_template
import requests
# https://api.openweathermap.org/data/2.5/weather?id=7533255&appid=7a2d438e1e09ea12a9d4c1a12ff46f58

url_weather = ''
api_key = '7a2d438e1e09ea12a9d4c1a12ff46f58'

my_app = Flask(__name__)


@my_app.route('/')
def hola():
    return 'Hola mundo'


@my_app.route('/<string:page_name>/')
def render_static(page_name):
    return render_template('%s.html' % page_name)


if __name__ == '__main__':
        my_app.run()
