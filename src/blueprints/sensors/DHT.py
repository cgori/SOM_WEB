from flask import Blueprint, render_template
import requests
import os
from dotenv import load_dotenv
from flask_table import Table, Col
import time
import json
# Declare your table


class ItemTable(Table):
    name = Col('Name')
    description = Col('Description')


load_dotenv('../.dotenv')
DHT_URL = os.getenv('URL')+'/DHT'
headers = {'Content-Type': 'application/json',
           'token': os.getenv("TOKEN")}

DHT_BLUEPRINT = Blueprint('DHT_BLUEPRINT', __name__)


@DHT_BLUEPRINT.route('/')
def index():
    r = requests.get(DHT_URL, headers=headers)
    # Prepare the data for displaying
    print(r.json())
    data = r.json()["results"]
    for val in data:
        print(val["submitted"])
        for d in val["results"]:

            d["recorded"] = time.strftime(
                '%Y-%m-%d %H:%M:%S', time.localtime(d["recorded"]))

    return render_template('dht_table.html', x=data)


@DHT_BLUEPRINT.route('/elements')
def elements():

    return render_template('elements.html')
