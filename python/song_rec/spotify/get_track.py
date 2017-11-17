import requests

from spotify.auth import get_auth_token
from spotify.constants import TRACK_URL, ALBUM_URL, ARTIST_URL, PLAYLIST_URL
from spotify.classes.spotify import Track, Album, Artist


def get_track_dict(track_id):
    """Builds a dictionary of a track, given a track id, from a call to Spotify API"""

    response = requests.get('%s%s' % (TRACK_URL, track_id), headers={'Authorization': 'Bearer %s' % get_auth_token()})
    return response.json()


def get_album_dict(album_id):
    """Builds a dictionary of an album, given an album id, from a call to Spotify API"""

    response = requests.get('%s%s' % (ALBUM_URL, album_id), headers={'Authorization': 'Bearer %s' % get_auth_token()})
    return response.json()


def get_artist_dict(artist_id):
    """Builds a dictionary of an artist, given an artist id from a call to Spotify API"""

    response = requests.get('%s%s' % (ARTIST_URL, artist_id), headers={'Authorization': 'Bearer %s' % get_auth_token()})
    return response.json()


def get_occurrences(character, str):
    """Gets occurrences of a character in a given string"""

    return [index for index, elem in enumerate(str) if elem == character]


def get_playlist_dict(playlist_url):
    """Builds a dictionary of a playlist, given a playlist url, from a call to Spotify API"""

    slash_occurrences = get_occurrences('/', playlist_url)
    username = playlist_url[(slash_occurrences[3] + 1):slash_occurrences[4]]
    playlist_id = playlist_url[(slash_occurrences[5] + 1):]
    return get_playlist_dict_from_id(username=username, playlist_id=playlist_id)


def get_playlist_dict_from_id(username, playlist_id):
    """Builds a dictionary of a playlist, given a playlist id, from a call to Spotify API"""

    response = requests.get('%s%s/playlists/%s/tracks' % (PLAYLIST_URL, username, playlist_id),
                            headers={'Authorization': 'Bearer %s' % get_auth_token()})
    return response.json()


def get_track(track_id):
    """Builds a Track object, given a track id, from a call to Spotify API"""

    return Track(get_track_dict(track_id=track_id))


def get_album(album_id):
    """Builds an Album object, given an album id, from a call to Spotify API"""

    return Album(get_album(album_id=album_id))


def get_artist(artist_id):
    """Builds an Artist object, given an artist id, from a call to Spotify API"""

    return Artist(get_artist_dict(artist_id=artist_id))


def get_playlist(playlist_url):
    """Builds a dictionary of a playlist, given a playlist url, filled with Track objects"""

    tracks_dict = get_playlist_dict(playlist_url=playlist_url)
    tracks_list = []
    for item in tracks_dict['items']:
        track_dict = item['track']
        track_object = Track(track_dict)
        tracks_list.append(track_object)
    return tracks_list


def get_playlist_from_id(username, playlist_id):
    """Builds a dictionary of a playlist, given a playlist id, filled with Track objects"""

    tracks_dict = get_playlist_dict_from_id(username=username, playlist_id=playlist_id)
    tracks_list = []
    for item in tracks_dict['items']:
        track_dict = item['track']
        track_object = Track(track_dict)
        tracks_list.append(track_object)
    return tracks_list
