import requests

from spotify.get_track import get_playlist_from_id
from spotify.auth import get_auth_token
from spotify.constants import CATEGORIES_URL


def get_playlists():
    category_id_list = []
    categories = requests.get(CATEGORIES_URL, headers={'Authorization': 'Bearer %s' % get_auth_token()})
    categories = categories.json()
    categories = categories['categories']
    for category in categories['items']:
        category_id_list.append(category['id'])

    playlist_results = []

    for category in category_id_list:
        response = requests.get(CATEGORIES_URL + category + "/playlists",
                                headers={'Authorization': 'Bearer %s' % get_auth_token()})
        response = response.json()
        playlists = response['playlists']

        for item in playlists['items']:
            href = item['href'].split("/")
            playlist_id = href[len(href) - 1]
            user = item["owner"]['id']

            playlist_results.append(get_playlist_from_id(user, playlist_id))

    return playlist_results
