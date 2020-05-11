from flask import Blueprint, render_template
import requests
import os
from dotenv import load_dotenv
from flask_table import Table, Col
import time
import json

load_dotenv('../.dotenv')
status_url = os.getenv('URL')+'status'
headers = {'Content-Type': 'application/json',
           'token': os.getenv("TOKEN")}

STATUS_BLUEPRINT = Blueprint('STATUS_BLUEPRINT', __name__)
@STATUS_BLUEPRINT.route('/status')
def index():
    r = requests.get(status_url, headers=headers)
    # Prepare the data for displaying

    data = r.json()["results"]

    return render_template('status.html', x=data)
