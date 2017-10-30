from flask import Flask, request

from recommendation import get_recommendation


app = Flask(__name__)


@app.route('/')
def index():
    return "Welcome to the Song_Recommendation Project"


# Route is /get_recommendation?url="https://blabla.com"
@app.route('/get_recommendation', methods=['GET'])
def recommend():
    playlist_url = request.args.get('playlist_url')

    new_song = get_recommendation(playlist_url=playlist_url)
    return new_song


if __name__ == '__main__':
    app.run()
