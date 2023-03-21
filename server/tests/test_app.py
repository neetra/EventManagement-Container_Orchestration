# for running python test_app.py uncomment2 and comment 4
# from app import app

import requests;
import json;

ENDPOINT= "http://127.0.0.1:5003/"

def test_ping():
    response = requests.get(ENDPOINT)
    data = (response.json())
    assert response.status_code == 200
    message = data['message']
    assert message == "Hello, World!"

def test_answer():
    assert 5 == 5
    

