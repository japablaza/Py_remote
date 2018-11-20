from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hola():
    nombre = 'Jose'
    apellido = 'Apablaza'
    lol = ':: and it is working ::'
    return render_template('hola.html', **locals())


if __name__ == '__main__':
    app.run()
