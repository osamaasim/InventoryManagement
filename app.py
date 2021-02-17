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

def init_database():
    db = sqlite3.connect(DATABASE_NAME)
    cursor= db.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products(prod_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    prod_name TEXT UNIQUE NOT NULL,
                    prod_quantity INTEGER NOT NULL,
                    unallocated_quantity INTEGER);
    """)
    db.commit()

@app.route("/")
def home():
    return "Hello, Flask!"