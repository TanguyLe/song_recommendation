import requests
from auth import get_auth_token

from classes.spotify import Track, Album, Artist

TRACK_URL = 'https://api.spotify.com/v1/tracks/'
ALBUM_URL = 'https://api.spotify.com/v1/albums/'
ARTIST_URL = 'https://api.spotify.com/v1/artists/'
PLAYLIST_URL = 'https://api.spotify.com/v1/users/'


def get_track_dict(track_id):
    response = requests.get(TRACK_URL + track_id, headers={'Authorization': 'Bearer %s' % get_auth_token()})
    return response.json()


def get_album_dict(album_id):
    response = requests.get(ALBUM_URL + album_id, headers={'Authorization': 'Bearer %s' % get_auth_token()})
    return response.json()


def get_artist_dict(artist_id):
    response = requests.get(ALBUM_URL + artist_id, headers={'Authorization': 'Bearer %s' % get_auth_token()})
    return response.json()


def get_occurencies(character, str):
    return [index for index, elem in enumerate(str) if elem == character]


def get_playlist_dict(playlist_url):
    slash_occurencies = get_occurencies('/', playlist_url)
    username = playlist_url[(slash_occurencies[3] + 1):slash_occurencies[4]]
    playlist_id = playlist_url[(slash_occurencies[5] + 1):]
    return get_playlist_dict_from_id(username=username, playlist_id=playlist_id)


def get_playlist_dict_from_id(username, playlist_id):
    response = requests.get(PLAYLIST_URL + username + '/playlists/' + playlist_id + '/tracks',
                            headers={'Authorization': 'Bearer %s' % get_auth_token()})
    return response.json()


def get_track(track_id):
    return Track(get_track_dict(track_id))


def get_album(album_id):
    return Album(get_album(album_id))


def get_artist(artist_id):
    return Artist(get_artist_dict(artist_id))


def get_playlist(playlist_url):
    tracks_dict = get_playlist_dict(playlist_url=playlist_url)
    tracks_list = []
    for item in tracks_dict['items']:
        track_dict = item['track']
        track_object = Track(track_dict)
        tracks_list.append(track_object)
    return tracks_list


def get_playlist_from_id(username, playlist_id):
    tracks_dict = get_playlist_dict_from_id(username, playlist_id)
    tracks_list = []
    for item in tracks_dict['items']:
        track_dict = item['track']
        track_object = Track(track_dict)
        tracks_list.append(track_object)
    return tracks_list
