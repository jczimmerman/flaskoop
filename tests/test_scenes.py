import pytest

def test_index(client, app):
    response = client.get('/')
    assert b'Dusty Trails' in response.data
    assert b'<a href="/tavern"' in response.data
