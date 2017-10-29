import requests
from constants import CLIENT_ID, CLIENT_SECRET

DATA_PARAMS = {'grant_type': 'client_credentials'}
URL = 'https://accounts.spotify.com/api/token'


def getAuthToken():
    response = requests.post(URL, data=DATA_PARAMS, auth=(CLIENT_ID, CLIENT_SECRET))
    return response.json()['access_token']
