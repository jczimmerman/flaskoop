import pytest

def test_index(client, app):
    response = client.get('/')
    assert b'Dusty Trails' in response.data
    assert b'<a href="/tavern"' in response.data

    response = client.get('/death')
    assert b'You are dead!'

    #make sure the the redirects for users answers work
    #TAVERN REDIRECTS
    response = client.post('/tavern', data={"action": "1"}, follow_redirects=True)
    assert b'The bar in the tavern' in response.data
    response = client.post('/tavern', data={"action": "2"}, follow_redirects=True)
    assert b'Approaching the stranger' in response.data

    #BAR REDIRECTS
    response = client.post('/bar', data={"action": "1"}, follow_redirects=True)
    assert b'You are dead!' in response.data
    response = client.post('/bar', data={"action": "2"}, follow_redirects=True)
    assert b'The Blue Moon Tavern' in response.data

    #STRANGER REDIRECTS
    response = client.post('/stranger', data={"action": "1"}, follow_redirects=True)
    assert b"stranger - advice" in response.data
    response = client.post('/stranger', data={"action": "2"}, follow_redirects=True)
    assert b"The Blue Moon Tavern" in response.data
