from datetime import datetime
import requests
from flask import render_template
from program import app


@app.route('/')
@app.route('/index')
def index():
    timenow = str(datetime.now())
    return render_template('index.html', title='Template Demo', time=timenow)


@app.route('/100Days')
def p100days():
    return render_template('100Days.html')


def get_chuck_joke():
    r = requests.get('https://api.chucknorris.io/jokes/random')
    data = r.json()
    return data['value']


@app.route('/chuck')
def chuck():
    return render_template('chuck.html', joke=get_chuck_joke())
