import spotipy


class Track:

    def __init__(self, name, artists, album, image, release_date):
        self.name = name
        self.artists = artists
        self.album = album
        self.image = image
        self.release_date = release_date


class Artist:

    def __init__(self, name, image, genres, followers):
        self.name = name
        self.image = image
        self.genres = genres
        self.followers = followers


class Playlist:

    def __init__(self, name, image, owner, track_count, description):
        self.name = name
        self.image = image
        self.owner = owner
        self.track_count = track_count
        self.description = description


def get_home_images(token):
    spotify = spotipy.Spotify(auth=token)
    saved_track_image = spotify.current_user_saved_tracks(limit=1)['items'][0]['track']['album']['images'][0]['url']
    top_track_image = spotify.current_user_top_tracks(limit=1, time_range='medium_term')['items'][0]['album']['images'][0]['url']
    top_artist_image = spotify.current_user_top_artists(limit=1, time_range='medium_term')['items'][0]['images'][0]['url']
    playlist_image = spotify.current_user_playlists(limit=1)['items'][0]['images'][0]['url']
    recently_played_image = spotify.current_user_recently_played(limit=1)['items'][0]['track']['album']['images'][0]['url']
    return {
        'saved_track_image': saved_track_image,
        'top_track_image': top_track_image,
        'top_artist_image': top_artist_image,
        'playlist_image': playlist_image,
        'recently_played_image': recently_played_image,
    }


def get_saved_tracks(token):
    spotify = spotipy.Spotify(auth=token)
    saved_tracks = []
    limit = 50
    offset = 0
    while True:
        items = spotify.current_user_saved_tracks(limit=limit, offset=offset)['items']
        offset += limit
        saved_tracks.extend(Track(
            name=item['track']['name'],
            artists=', '.join(artist['name'] for artist in item['track']['artists']),
            album=item['track']['album']['name'],
            image=item['track']['album']['images'][0]['url'],
            release_date=item['track']['album']['release_date'],
        ) for item in items)
        if len(items) < 50:
            break
    return saved_tracks


def get_top_tracks(token):
    spotify = spotipy.Spotify(auth=token)
    items = spotify.current_user_top_tracks(limit=20, time_range='medium_term')['items']
    top_tracks = [Track(
        name=item['name'],
        artists=', '.join(artist['name'] for artist in item['artists']),
        album=item['album']['name'],
        image=item['album']['images'][0]['url'],
        release_date=item['album']['release_date'],
    ) for item in items]
    return top_tracks


def get_top_artists(token):
    spotify = spotipy.Spotify(auth=token)
    items = spotify.current_user_top_artists(limit=20, time_range='medium_term')['items']
    top_artists = [Artist(
        name=item['name'],
        image=item['images'][0]['url'],
        genres=', '.join(genre for genre in item['genres']),
        followers=item['followers']['total'],
    ) for item in items]
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
    recently_played = [Track(
        name=item['track']['name'],
        artists=', '.join(artist['name'] for artist in item['track']['artists']),
        album=item['track']['album']['name'],
        image=item['track']['album']['images'][0]['url'],
        release_date=item['track']['album']['release_date'],
    ) for item in items]
    return recently_played