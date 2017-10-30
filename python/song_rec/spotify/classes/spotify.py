import requests


class Track:
    """A Python object representing the JSON for a track.
    Docs for a Track: https://developer.spotify.com/web-api/get-track/

    *Added an audio_features key, a seperate call that is make when given a token.
    Docs for audio features: https://developer.spotify.com/web-api/get-audio-features/"""

    def __init__(self, track_json, auth_token=None):
        self.album = None
        self.artists = None
        self.available_markets = None
        self.disc_number = None
        self.duration_ms = None
        self.explicit = None
        self.external_ids = None
        self.external_urls = None
        self.href = None
        self.id = None
        self.is_playable = None
        self.linked_from = None
        self.restrictions = None
        self.name = None
        self.popularity = None
        self.preview_url = None
        self.track_number = None
        self.type = None
        self.uri = None
        self.audio_features = None

        self.__dict__ = track_json

        # Sets album to an Album object
        if 'album' in self.__dict__:
            self.__dict__['album'] = Album(self.__dict__['album'])

        # Sets artists to a list of Artist objects
        if 'artists' in self.__dict__:
            for i, artist in enumerate(self.__dict__['artists']):
                (self.__dict__['artists'])[i] = Artist(artist)

        # Sets audio_features if given an auth_token to make the call
        if auth_token is not None:
            header = {'Authorization': 'Bearer %s' % auth_token}
            url = 'https://api.spotify.com/v1/audio-features/' + self.__dict__['id']
            self.__dict__['audio_features'] = requests.get(url, headers=header).json()

        # Set each instance attributes to their values from __dict__
        for key, value in self.__dict__.items():
            setattr(self, key, value)


class Album:
    """A Python object representing the JSON for an album
    Spotify docs for an Album: https://developer.spotify.com/web-api/get-album/"""

    def __init__(self, album_json):
        self.album_type = None
        self.artists = None
        self.available_markets = None
        self.copyrights = None
        self.external_ids = None
        self.external_urls = None
        self.genres = None
        self.href = None
        self.id = None
        self.images = None
        self.label = None
        self.name = None
        self.name = None
        self.popularity = None
        self.release_date = None
        self.release_date_precision = None
        self.tracks = None
        self.type = None
        self.uri = None

        self.__dict__ = album_json

        # Sets artists to a list of Artist objects
        if 'artists' in self.__dict__:
            for i, artist in enumerate(self.__dict__['artists']):
                (self.__dict__['artists'])[i] = Artist(artist)

        # Sets tracks to a list of Track objects
        if 'tracks' in self.__dict__:
            for i, track in enumerate(self.__dict__['tracks']['items']):
                (self.__dict__['tracks']['items'])[i] = Track(track)

        # Set each instance attributes to their values from __dict__
        for key, value in self.__dict__.items():
            setattr(self, key, value)


class Artist:
    """A Python object representing the JSON for an album
    Spotify docs for an Artist: https://developer.spotify.com/web-api/get-artist/"""

    def __init__(self, artist_json):
        self.external_urls = None
        self.followers = None
        self.genres = None
        self.href = None
        self.id = None
        self.images = None
        self.name = None
        self.popularity = None
        self.type = None
        self.uri = None

        self.__dict__ = artist_json

        # Set each instance attributes to their values from __dict__
        for key, value in self.__dict__.items():
            setattr(self, key, value)
