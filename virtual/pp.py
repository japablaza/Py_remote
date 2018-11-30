from flask import Flask, render_template

from virtual.api_call import *

app = Flask(__name__)

@app.route('/')
def hola():
    nombre = 'Jose'
    apellido = 'Apablaza'
    lol = ':: and it is working ::'
    chicago = city_func('Chicago', 'US')['id']
    return render_template('hola.html', **locals())

@app.route('/test_dict')
def testing():
    city_dict = city_func('Chicago', 'US')['id']
    return render_template('test_dict.html', **locals())

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
    return render_template('weather.html', ** locals())

@app.route('/clima')
def clima():
    clima_dict = api_call_func_to_JSON('New York', 'US')
    foto_link = type(photos_jason('Chicago'))
    return render_template('clima.html', **locals())

#
# if __name__ == '__main__':
#     app.run()
