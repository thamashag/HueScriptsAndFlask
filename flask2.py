from flask import Flask
from flask import render_template
import script1
import script2

import requests
import time

app = Flask(__name__)


@app.route('/')
def index():
    return script1.sumTwo()

@app.route('/stark')
def index2():
    return script2.sumThree()


if __name__ == '__main__':
    app.run(host= '0.0.0.0')