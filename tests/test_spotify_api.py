import unittest
import spotify_api
import creds


class TestSpotifyApi(unittest.TestCase):
    """
    Tests for the functions in spotify_api.py
    Requires signing in to a dummy Spotify account with the following setup:
    - Ensure that the track Demi Moore by Phoebe Bridgers is saved
    - Ensure that the track Space by Biffy Clyro has been listened to in the last 6 months
    - Ensure that the playlist Discover Weekly by Spotify has been subscribed to
    Obtain the session token using the app's /token endpoint and save it to the testing_token variable in creds.py
    """

    def test_get_saved_tracks(self):
        token = creds.testing_token
        saved_tracks = spotify_api.get_saved_tracks(token)
        # Assert that there is at least one saved track
        self.assertGreater(len(saved_tracks), 0)
        # Save the track Demi Moore by Phoebe Bridgers and assert that it appears
        try:
            next(filter(lambda track: track.name == 'Demi Moore'
                                  and track.artists == 'Phoebe Bridgers'
                                  and track.release_date == '2017-09-22'
                                  and track.album == 'Stranger in the Alps', saved_tracks))
        except StopIteration:
            self.fail('Example saved track not present')

    def test_get_top_tracks(self):
        token = creds.testing_token
        top_tracks = spotify_api.get_top_tracks(token)
        # Assert that there is at least 1 top track
        self.assertGreater(len(top_tracks), 0)
        # Assert that there are no more than 20 top tracks shown
        self.assertLessEqual(len(top_tracks), 20)

    def test_get_top_artists(self):
        token = creds.testing_token
        top_artists = spotify_api.get_top_artists(token)
        # Assert that there is at least 1 top artist
        self.assertGreater(len(top_artists), 0)
        # Assert that there are no more than 20 top artists shown
        self.assertLessEqual(len(top_artists), 20)

    def test_get_playlists(self):
        token = creds.testing_token
        playlists = spotify_api.get_playlists(token)
        # Assert that there is at least 1 playlist
        self.assertGreater(len(playlists), 0)
        # Assert that there are no more than 50 playlists shown
        self.assertLessEqual(len(playlists), 50)
        # Add playlist Discover Weekly by Spotify and assert that it appears
        try:
            next(filter(lambda playlist: playlist.name == 'Discover Weekly'
                                     and playlist.owner == 'Spotify', playlists))
        except StopIteration:
            self.fail('Example playlist not present')

    def test_recently_played(self):
        token = creds.testing_token
        recently_played = spotify_api.get_recently_played(token)
        # Assert that there are 20 recently played songs
        self.assertEqual(len(recently_played), 20)
        # Listen to the track Space by Biffy Clyro and assert that it appears
        try:
            next(filter(lambda track: track.name == 'Space'
                                  and track.artists == 'Biffy Clyro'
                                  and track.release_date == '2020-08-14'
                                  and track.album == 'A Celebration Of Endings', recently_played))
        except StopIteration:
            self.fail('Example recently played track not present')


if __name__ == "__main__":
    unittest.main()
