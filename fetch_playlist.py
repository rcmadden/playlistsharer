# convert a spotify playlist to apple playlist format
# convert apple playlist to spotify format
# allow shared playlists between apple and spotify users

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv(dotenv_path="./.env.local")

client_id = os.environ.get("client_id")
SPOTIPY_CLIENT_SECRET = os.environ.get("client_secret")
SPOTIPY_CLIENT_ID = os.environ.get("client_id")
REDIRECT_URI="http://localhost:8888/callback"

scope = "playlist-modify-public"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                            client_secret=SPOTIPY_CLIENT_SECRET,
                                            redirect_uri=REDIRECT_URI,
                                            scope=scope))

def fetch_playlist_id(playlist_name):
    """Fetches playlist id for playlist."""
    scope = "playlist-modify-public"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                                                client_secret=SPOTIPY_CLIENT_SECRET,
                                                redirect_uri=REDIRECT_URI,
                                                scope=scope))
    playlists = sp.current_user_playlists()
    for playlist in playlists['items']:
        if playlist['name'] == playlist_name:
            print(playlist['name'])
            return playlist['id']
    

print(fetch_playlist_id('Chillax'))

def fetch_playlists():
    """Fetches all users playlists."""

    playlists = sp.current_user_playlists()
    for playlist in playlists['items']:
        print(playlist['name'], playlist['id'], playlist['tracks'])


fetch_playlists()