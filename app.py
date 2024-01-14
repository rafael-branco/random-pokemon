import flask
import random
import os
import mysql.connector
from dotenv import load_dotenv
import json

app = flask.Flask(__name__)

load_dotenv()

@app.route('/')
def index(name=None):
    return flask.render_template('index.html', name=name)

@app.route('/get-random-pokemon')
def get_random_pokemon():

    mydb = mysql.connector.connect(
        host=os.getenv('HOST'),
        user=os.getenv('USER'),
        password=os.getenv('PASSWORD'),
        database=os.getenv('DATABASE')
    )

    cursor = mydb.cursor()

    pokemon_img = random.choice(os.listdir('static/Images'))
    id = pokemon_img.split('.')[0]
    query = ("SELECT name, img_path, type01, type02 FROM pokemon WHERE id = %s")
    cursor.execute(query, (id, ))
    result = cursor.fetchone()
    result = json.dumps(result)
    return result

