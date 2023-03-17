# for running python test_app.py uncomment2 and comment 4
# from app import app

from app.app import app

import json;

def test_ping():
    response = app.test_client().get('/')    
    assert response.status_code == 200
    message = json.loads(response.data )['message']
    assert message == "Hello, World!"

def test_answer():
    assert 5 == 5
    

