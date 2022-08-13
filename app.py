from flask import Flask, request, url_for, session, redirect, render_template, jsonify
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import time
from creds import *


app = Flask(__name__)


# signs the session cookie
app.secret_key = "aaiurhpUSDHqo837xron"
app.config['SESSION_COOKIE_NAME'] = "Lydia's Cookie" # session allows you to log in during the same session
TOKEN_INFO = "token_info"


@app.route('/')
def login():
    sp_oauth = create_spotify_oauth()
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)


@app.route('/redirect')
def redirect_page():
    sp_oauth = create_spotify_oauth()
    session.clear()
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code)
    # saving token info in the session
    session[TOKEN_INFO] = token_info
    return redirect("getTracks")


@app.route('/getTracks')
def get_tracks():
    try:
        token_info = get_token()
    except:
        print("user not logged in")
        return redirect("/")
    sp = spotipy.Spotify(auth=token_info['access_token'])
    all_songs = []
    iter = 0
    while True:
        items = sp.current_user_saved_tracks(limit=50, offset=iter * 50)['items']
        iter += 1
        all_songs += items
        if len(items) < 50:
            break
    return f"Your total number of saved tracks is {str(len(all_songs))}!"


@app.route('/getArtists')
def get_artist():
    try:
        token_info = get_token()
    except:
        print("user not logged in")
        return redirect("/")
    scope = "user-top-read"
    sp = spotipy.Spotify(auth=token_info['access_token'])
    results = sp.current_user_top_artists(limit=20, offset=0, time_range='medium_term')
    for items in results['items']:
        return str(items['name'])


@app.route('/getTopTracks')
def get_top_tracks():
    try:
        token_info = get_token()
    except:
        print("user not logged in")
        return redirect("/")
    sp = spotipy.Spotify(auth=token_info['access_token'])
    results = sp.current_user_top_tracks(limit=20, offset=0, time_range='medium_term')
    for items in results['items']:
        return str(items['name'])


@app.route('/getRecentlyPlayed')
def get_recently_played():
    try:
        token_info = get_token()
    except:
        print("user not logged in")
        return redirect("/")
    sp = spotipy.Spotify(auth=token_info['access_token'])
    results = sp.current_user_recently_played(limit=20)
    for idx, item in enumerate(results['items']):
        track = item['track']
        return jsonify(idx, track['artists'][0]['name'], " – ", track['name'])

@app.route('/getPlaylists')
def get_playlists():
    try:
        token_info = get_token()
    except:
        print("user not logged in")
        return redirect("/")
    sp = spotipy.Spotify(auth=token_info['access_token'])
    results = sp.current_user_playlists(limit=50)
    for i, item in enumerate(results['items']):
        return jsonify("%d %s" % (i, item['name']))


def get_token():
    token_info = session.get(TOKEN_INFO, None)
    if not token_info:
        raise "exception"
    now = int(time.time())
    is_expired = token_info['expires_at'] - now < 60
    if (is_expired):
        sp_oauth = create_spotify_oauth()
        token_info = sp_oauth.refresh_access_token(token_info['refresh_token'])
    return token_info


def create_spotify_oauth():
    return SpotifyOAuth(
            client_id=client_ID,
            client_secret=client_SECRET,
            redirect_uri=url_for('redirect_page', _external=True),
            scope=scope)


if __name__ == "__main__":
    app.run(debug=True)