from engine.algo import black_box_ml
from million_songs.get_million_songs import get_df_from_csv
from spotify.get_track import get_playlist


def get_recommendation(playlist_url):

    million_songs = get_df_from_csv()
    playlist_songs = get_playlist(playlist_url=playlist_url)

    new_song = black_box_ml(songs_data=million_songs, playlist=playlist_songs)

    return new_song
