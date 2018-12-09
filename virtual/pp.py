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

@app.route('/clima/<city>')
def clima(city=None):
    clima_dict = api_call_func_to_JSON(city, 'US')
    foto_link = random_photo(city)
    return render_template('clima.html', **locals())


if __name__ == '__main__':
    app.run()
