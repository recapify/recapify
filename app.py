from flask import Flask, request, url_for, session, redirect, render_template, jsonify
from spotipy.oauth2 import SpotifyOAuth
from spotify_api import get_home_images, get_saved_tracks, get_top_tracks, get_top_artists, get_playlists, get_recently_played
from creds import *
import time


app = Flask(__name__)


# signs the session cookie
app.secret_key = SSK
app.config['SESSION_COOKIE_NAME'] = "Lydia's Cookie"  # session allows you to log in during the same session


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
    session["token_info"] = token_info
    return redirect(url_for('home'))


@app.route('/token')
def get_token_for_testing():
    try:
        token_info = get_token()
    except TimeoutError:
        return redirect("/")
    return jsonify({'token': token_info['access_token']})

@app.route('/home')
def home():
    try:
        token_info = get_token()
    except TimeoutError:
        return redirect("/")
    images = get_home_images(token_info['access_token'])
    return render_template("home.html", images=images)


@app.route('/saved-tracks')
def view_saved_tracks():
    try:
        token_info = get_token()
    except TimeoutError:
        return redirect("/")
    saved_tracks = get_saved_tracks(token_info['access_token'])
    return render_template("saved_tracks.html", saved_tracks=saved_tracks)


@app.route('/top-tracks')
def view_top_tracks():
    try:
        token_info = get_token()
    except TimeoutError:
        return redirect("/")
    top_tracks = get_top_tracks(token_info['access_token'])
    return render_template("top_tracks.html", top_tracks=top_tracks)


@app.route('/top-artists')
def view_top_artists():
    try:
        token_info = get_token()
    except TimeoutError:
        return redirect("/")
    top_artists = get_top_artists(token_info['access_token'])
    return render_template("top_artists.html", top_artists=top_artists)


@app.route('/playlists')
def view_playlists():
    try:
        token_info = get_token()
    except TimeoutError:
        return redirect("/")
    playlists = get_playlists(token_info['access_token'])
    return render_template("playlists.html", playlists=playlists)


@app.route('/recently-played')
def view_recently_played():
    try:
        token_info = get_token()
    except TimeoutError:
        return redirect("/")
    recently_played = get_recently_played(token_info['access_token'])
    return render_template("recently_played.html", recently_played=recently_played)


def get_token():
    token_info = session.get("token_info")
    if not token_info:
        raise TimeoutError
    now = int(time.time())
    is_expired = token_info['expires_at'] - now < 60
    if is_expired:
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
    app.run()
