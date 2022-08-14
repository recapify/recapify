import os

client_ID = ''
client_SECRET = ''
redirect_URI = 'http://127.0.0.1:5000/redirect'
SSK = os.urandom(12)
scope = "user-library-read", "user-top-read", "playlist-read-private", "user-read-recently-played"
