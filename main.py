import spotipy
from spotipy.oauth2 import SpotifyOAuth
from creds import *

scope = "user-read-recently-played"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_ID,
                                               client_secret=client_SECRET,
                                               redirect_uri=redirect_URI,
                                               scope=scope))

# add what you want to do here to make the wrapped
results = sp.current_user_recently_played()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])
