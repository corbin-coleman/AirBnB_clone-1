#!/usr/bin/python3
from flask import Flask, abort
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, HBNB!'

@app.route('/hbnb')
def hbnb():
    return 'HBNB'

@app.route('/c/<text>')
def c_is(text):
    return 'C {}'.format(text.replace('_', ' '))

@app.route('/python/')
@app.route('/python/<text>')
def python_is(text='is cool'):
    return 'Python {}'.format(text.replace('_', ' '))

@app.route('/number/<n>')
def is_number(n):
    if n.isdigit():
        return '{} is a number'.format(n)
    abort(404)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
