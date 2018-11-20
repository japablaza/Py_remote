from flask import Flask, render_template

my_app = Flask(__name__)


@my_app.route('/')
def hola():
    return 'Hola mundo'


@my_app.route('/<string:page_name>/')
def render_static(page_name):
    return render_template('%s.html' % page_name)


if __name__ == '__main__':
        my_app.run()
