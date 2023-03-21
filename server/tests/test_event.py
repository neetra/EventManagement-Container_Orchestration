import requests;
import json;
import tests.settings as settings;
#import settings
ENDPOINT = settings.baseurl
EVENTURL = settings.baseurl + "/event"
global EventId
import pytest

def pytest_namespace():
    return {'EventId': 0}

def test_ping_event():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200
   

def test_all_events():
    allEventsUrl = ENDPOINT + "/event/events"
    response = requests.get(allEventsUrl)   
    assert response.status_code == 200

def create_an_event():
    # Setup
    allEventsUrl = ENDPOINT + "/event"
    data = {
    "eventName" : "Integration Test Event",
    "eventDescription" : "description",
    "eventHostBy" : "host By"
    }
    # when
    response = requests.post(allEventsUrl, json=data)  

    # then 
    responseData = response.json()
    assert response.status_code == 200
    assert responseData['Name'] == "Integration Test Event"
    assert responseData['description'] == "description"
    pytest.EventId = responseData['id']
   

def get_an_event():
        # Setup
        eventsUrl = ENDPOINT + "/event?eventId=" + (pytest.EventId)
    
        # when
        response = requests.get(eventsUrl)  

        # then 
        responseData = response.json()
        assert response.status_code == 200
        assert responseData['id'] == pytest.EventId
        assert responseData['Name'] == "Integration Test Event"
        assert responseData['description'] == 'description'
      
def delete_an_event():
        # Setup
        eventsUrl = ENDPOINT + "/event?eventId=" + (pytest.EventId)
    
        # when
        response = requests.delete(eventsUrl)  

        # then 
        assert response.status_code == 200