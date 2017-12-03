from get_track import *
from auth import get_auth_token


def get_playlists():
	category_id_list = []
	categories = requests.get("https://api.spotify.com/v1/browse/categories", 
		headers={'Authorization': 'Bearer %s' % get_auth_token()})
	categories = categories.json()
	categories = categories['categories']
	for category in categories['items']:
		category_id_list.append(category['id'])

	playlist_results = []
	for category in category_id_list:
		response = requests.get("https://api.spotify.com/v1/browse/categories/" + category + "/playlists", 
			headers={'Authorization': 'Bearer %s' % get_auth_token()})
		response = response.json()
		playlists = response['playlists']
		for item in playlists['items']:
			href = item['href'].split("/")
			playlist_id = href[len(href) - 1]
			user = item["owner"]['id']
			playlist_results.append(get_playlist_from_id(user, playlist_id))
	return playlists

