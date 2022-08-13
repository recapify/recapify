import spotipy


def get_saved_tracks(token):
    spotify = spotipy.Spotify(auth=token)
    saved_tracks = []
    limit = 50
    offset = 0
    while True:
        items = spotify.current_user_saved_tracks(limit=limit, offset=offset)['items']
        offset += limit
        saved_tracks.extend({
            'name': item['track']['name'],
            'artists': ', '.join(artist['name'] for artist in item['track']['artists']),
            'album': item['track']['album']['name'],
            'image': item['track']['album']['images'][0]['url'],
            'release_date': item['track']['album']['release_date'],
        } for item in items)
        if len(items) < 50:
            break
    return saved_tracks


def get_top_tracks(token):
    spotify = spotipy.Spotify(auth=token)
    items = spotify.current_user_top_tracks(limit=20, offset=0, time_range='medium_term')['items']
    top_tracks = [{
        'name': item['name'],
        'artists': ', '.join(artist['name'] for artist in item['artists']),
        'album': item['album']['name'],
        'image': item['album']['images'][0]['url'],
        'release_date': item['album']['release_date'],
    } for item in items]
    return top_tracks


def get_top_artists(token):
    spotify = spotipy.Spotify(auth=token)
    items = spotify.current_user_top_artists(limit=20, offset=0, time_range='medium_term')['items']
    top_artists = [{
        'name': item['name'],
        'image': item['images'][0]['url'],
        'genres': ', '.join(genre for genre in item['genres']),
        'followers': item['followers']['total'],
    } for item in items]
    print(top_artists)
    return top_artists


def get_playlists(token):
    spotify = spotipy.Spotify(auth=token)
    items = spotify.current_user_playlists(limit=50)['items']
    playlists = [{
        'name': item['name'],
        'image': item['images'][0]['url'],
        'owner': item['owner']['display_name'],
        'track_count': item['tracks']['total'],
        'description': item['description'],
    } for item in items]
    return playlists


def get_recently_played(token):
    spotify = spotipy.Spotify(auth=token)
    items = spotify.current_user_recently_played(limit=20)['items']
    print(items)
    recently_played = [{
        'name': item['track']['name'],
        'artists': ', '.join(artist['name'] for artist in item['track']['artists']),
        'album': item['track']['album']['name'],
        'image': item['track']['album']['images'][0]['url'],
        'release_date': item['track']['album']['release_date'],
    } for item in items]
    return recently_played
