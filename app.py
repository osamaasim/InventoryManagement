# imports - standard imports
import os
import json
import sqlite3

from flask import Flask, url_for, request, redirect
from flask import render_template as render

# global constants
DATABASE_NAME = 'inventory.sqlite'

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='dev',
    DATABASE=os.path.join(app.instance_path, 'database', DATABASE_NAME),
)


@app.route("/")
def home():
    return "Hello, Flask!"