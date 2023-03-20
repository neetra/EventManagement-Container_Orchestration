from app.app import app;
import json
def test_ping_event():
    response = app.test_client().get('/event')    
    assert response.status_code == 200
    message = json.loads(response.data )['message']
    assert message == "hello from event"

def test_events():
    response = app.test_client().get('/event/events')    
    assert response.status_code == 200