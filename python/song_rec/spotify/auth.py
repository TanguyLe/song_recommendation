import requests
from spotify.constants import CLIENT_ID, CLIENT_SECRET, DATA_PARAMS, ACCOUNT_URL


def get_auth_token():
    response = requests.post(ACCOUNT_URL, data=DATA_PARAMS, auth=(CLIENT_ID, CLIENT_SECRET))
    return response.json()['access_token']
