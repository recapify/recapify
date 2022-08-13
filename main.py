import spotipy
from spotipy.oauth2 import SpotifyOAuth
from creds import *

scope = "user-read-recently-played"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_ID,
                                               client_secret=client_SECRET,
                                               redirect_uri=redirect_URI,
                                               scope=scope))

def get_recently_played_song():
    results = sp.current_user_recently_played(limit=20)
    for idx, item in enumerate(results['items']):
        track = item['track']
        return idx, track['artists'][0]['name'], " – ", track['name']
