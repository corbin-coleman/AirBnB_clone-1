#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from os import getenv
app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    storage.close()

@app.route('/cities_by_states')
def cities_by_states():
    return render_template('8-cities_by_states.html',
                           states=storage.all('State').values())

if __name__ == '__main__':
    app.run('0.0.0.0')
