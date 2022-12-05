# Shows a user's playlists

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv

from pprint import pprint

load_dotenv(dotenv_path="./.env.local")

# scope = 'playlist-read-private'
scope = "playlist-modify-public"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

results = sp.current_user_playlists(limit=1)
for i, item in enumerate(results['items']):
    print('**************************')
    print("%d %s" % (i, item['name']),'id: ', item['uri'],'url: ', item['external_urls']['spotify'])
    print('**************************')
    pprint(item)
    offset = 0
    # print tracks for each playlist
    while True:
        response = sp.playlist_items(item['uri'],
                                    offset=offset,
                                    fields='items.track.id,total',
                                    additional_types=['track'])
        
        if len(response['items']) == 0:
            break
        
        pprint(response['items'])
        offset = offset + len(response['items'])
        print(offset, "/", response['total'])
