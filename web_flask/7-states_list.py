#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/states_list/')
def state_list():
    return render_template('7-states_list.html',
                           states=storage.all('State').values())


@app.teardown_appcontext
def teardown(exception):
    storage.close()

if __name__ == '__main__':
    app.run('0.0.0.0')
