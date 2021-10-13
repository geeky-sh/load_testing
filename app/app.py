import time
from flask import Flask
from flask import json
from flask.json import jsonify
from werkzeug.wrappers import response

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify(working=True)

@app.route("/timed")
def timed_api():
    time.sleep(1)
    return jsonify(working=True)