from flask import Flask, render_template, session, request, redirect
from creds import *
import spotipy
import time

app = Flask(__name__)
app.secret_key = SSK

api_base = 'https://accounts.spotify.com'

SCOPE = "user-read-recently-played"


# logs the user in and authorises access to scope
@app.get("/")
def verify():
    sp_oauth = spotipy.oauth2.SpotifyOAuth(client_id=client_ID, client_secret=client_SECRET, redirect_uri=redirect_URI, scope=SCOPE)
    auth_url = sp_oauth.get_authorize_url()
    print(auth_url)
    return redirect(auth_url)


@app.get("/index")
def index():
    return render_template("index.html")


# Spotify returns access and refresh tokens
@app.get("/api_callback")
def api_callback():
    sp_oauth = spotipy.oauth2.SpotifyOAuth(client_id=client_ID, client_secret=client_SECRET, redirect_uri=redirect_URI, scope=SCOPE)
    session.clear()
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code)

    # Saving the access token along with all other token related info
    session["token_info"] = token_info

    return redirect("index")


# Spotify returns requested data
@app.get("/go")
def go():
    session['token_info'], authorised = get_token(session)
    session.modified = True
    if not authorised:
        return redirect('/')
    data = request.form
    sp = spotipy.Spotify(auth=session.get('token_info').get('access_token'))
    response = sp.current_user_top_tracks()

    return render_template("results.html", data=response)


# Checks to see if token is valid and gets a new token if not
def get_token(session):
    token_valid = False
    token_info = session.get("token_info", {})

    # Checking if the session already has a token stored
    if not (session.get('token_info', False)):
        token_valid = False
        return token_info, token_valid

    # Checking if token has expired
    now = int(time.time())
    is_token_expired = session.get('token_info').get('expires_at') - now < 60

    # Refreshing token if it has expired
    if is_token_expired:
        sp_oauth = spotipy.oauth2.SpotifyOAuth(client_id=client_ID, client_secret=client_SECRET, redirect_uri=redirect_URI, scope=SCOPE)
        token_info = sp_oauth.refresh_access_token(session.get('token_info').get('refresh_token'))

    token_valid = True
    return token_info, token_valid

# more methods here for the wrapped

if __name__ == "__main__":
    app.run(debug=True)