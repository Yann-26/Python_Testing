import pytest
from server import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    return app.test_client()

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200

def test_showsummary_valid_email(client):
    data = {'email': 'admin@irontemple.com'}
    response = client.post('/showSummary', data=data)
    assert response.status_code == 200
    assert b'Welcome to GUDLFT Registration' in response.data

def test_showsummary_invalid_email(client):
    data = {'email': 'invalid_email@example.com'}
    response = client.post('/showSummary', data=data)
    assert response.status_code == 200
    assert b'Error - Email not found.' in response.data

def test_book_valid(client):
    competition = 'SpringFestival'
    club = 'IronTemple'
    response = client.get(f'/book/{competition}/{club}')
    assert response.status_code == 200

def test_book_invalid(client):
    competition = 'InvalidCompetition'
    club = 'InvalidClub'
    response = client.get(f'/book/{competition}/{club}')
    assert response.status_code == 200
    assert b"Something went wrong-please try again" in response.data

def test_purchaseplaces_invalid_competition(client):
    data = {'competition': 'InvalidCompetition', 'club': 'SomeClub', 'places': '2'}
    response = client.post('/purchasePlaces', data=data)
    assert response.status_code == 200
    assert b'Error - Competition or club not found!' in response.data

def test_purchaseplaces_invalid_places(client):
    data = {'competition': 'SpringFestival', 'club': 'IronTemple', 'places': '20'}
    response = client.post('/purchasePlaces', data=data)
    assert response.status_code == 200
    assert b'Error - Invalid number of places requested!' in response.data

def test_purchaseplaces_max_limit(client):
    data = {'competition': 'SpringFestival', 'club': 'IronTemple', 'places': '12'}
    response = client.post('/purchasePlaces', data=data)
    assert response.status_code == 200
    assert b'Info - You cannot buy more than 12 places!' in response.data
