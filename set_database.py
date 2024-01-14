import json
import requests
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

mydb = mysql.connector.connect(
  host=os.getenv('HOST'),
  user=os.getenv('USER'),
  password=os.getenv('PASSWORD'),
  database=os.getenv('DATABASE')
)

cursor = mydb.cursor()

for id in range(10062, 10221):
  json_file = open(f'JSON/{id}.json')

  data = json.load(json_file)

  name = data['name']
  img_url = data['sprites']['other']['official-artwork']['front_default']
  type01 = data['types'][0]['type']['name']
  type02 = None

  if len(data['types']) > 1:
    type02 = data['types'][1]['type']['name']

  img_data = requests.get(img_url).content
  img_path = f'static/Images/{id}.png'
  img_file = open(img_path, 'wb')
  img_file.write(img_data)

  img_file.close()
  json_file.close()

  add_pokemon = ("INSERT INTO pokemon (id, name, img_path, type01, type02) VALUES (%s, %s, %s, %s, %s)")
  data_pokemon = (id, name, img_path, type01, type02)
  cursor.execute(add_pokemon, data_pokemon)
  mydb.commit()

cursor.close()
mydb.close()


# Save on database: [id, name, img_path, type01, type02]




