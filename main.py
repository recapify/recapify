import spotipy
from spotipy.oauth2 import SpotifyOAuth
import creds

# scope ="user-read-recently-played"
scope = 'user-top-read'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=creds.client_ID,
                                               client_secret=creds.client_SECRET,
                                               redirect_uri=creds.redirect_URI,
                                               scope=scope))

# add what you want to do here to make the wrapped
# results = sp.current_user_recently_played()
# for idx, item in enumerate(results['items']):
#     track = item['track']
#     print(idx, track['artists'][0]['name'], " – ", track['name'])

ranges = ['short_term', 'medium_term', 'long_term']


for sp_range in ['short_term', 'medium_term', 'long_term']:
    print("range:", sp_range)

    results = sp.current_user_top_artists(time_range=sp_range, limit=5)

    for i, item in enumerate(results['items']):
        print(i, item['name'])
    print()