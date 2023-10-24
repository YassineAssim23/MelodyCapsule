import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

# Spotify API credentials
load_dotenv()

CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
REDIRECT_URI = "http://127.0.0.1:5000/redirectPage"

def create_spotify_client(token_info):
    return spotipy.Spotify(auth=token_info['access_token'])

def get_user_top_tracks(token_info, limit=10, time_range="medium_term"):
    sp = create_spotify_client(token_info)
    try:
        top_tracks = sp.current_user_top_tracks(limit=limit, time_range=time_range)
        tracks_info = []
        for track in top_tracks['items']:
            track_name = track['name']
            artist_name = track['artists'][0]['name']
            track_link = track['external_urls']['spotify']
            image_url = track['album']['images'][0]['url'] if track['album']['images'] else None
            tracks_info.append({
                'track_name': track_name,
                'artist_name': artist_name,
                'track_link': track_link,
                'image_url': image_url
            })
        return tracks_info
    except Exception as e:
        print(f"Error getting top tracks: {e}")
        return None
    

def get_user_top_artists(token_info, limit=10, time_range="medium_term"):
    sp = create_spotify_client(token_info)
    try:
        top_artists = sp.current_user_top_artists(limit=limit, time_range=time_range)
        artists_info = []
        for artist in top_artists['items']:
            artist_name = artist['name']
            artist_link = artist['external_urls']['spotify']
            image_url = artist['images'][0]['url'] if artist['images'] else None
            artists_info.append({
                'artist_name': artist_name,
                'track_link': artist_link,
                'image_url': image_url
            })
        return artists_info
    except Exception as e:
        print(f"Error getting top tracks: {e}")
        return None


def get_user_info(token_info):
    sp = create_spotify_client(token_info)
    try:
        user_info = sp.current_user()
        return user_info
    except Exception as e:
        print(f"Error getting user information: {e}")
        return None
    

def get_user_devices(token_info):
    sp = create_spotify_client(token_info)
    try:
        devices = sp.devices()
        return devices.get('devices', [])
    except Exception as e:
        print(f"Error getting user devices: {e}")
        return None

def get_recently_played(token_info):
    sp = create_spotify_client(token_info)
    try:
        recently_played = sp.current_user_recently_played(limit=50, after=None, before=None)
        
        if 'items' in recently_played:
            tracks_info = []
            for track in recently_played['items']:
                track_name = track['track']['name']
                artist_name = track['track']['artists'][0]['name']
                album_name = track['track']['album']['name']
                played_at = track['played_at']
                track_link = track['track']['external_urls']['spotify']
                image_url = track['track']['album']['images'][0]['url'] if track['track']['album']['images'] else None
                tracks_info.append({
                    'name': track_name,
                    'artist': artist_name,
                    'album': album_name,
                    'played_at': played_at,
                    'track_link': track_link,
                    'image_url': image_url
                })
            return tracks_info
        else:
            print("Unexpected response format from Spotify API:", recently_played)
            return None
    except Exception as e:
        print(f"Error getting recently played tracks: {e}")
        return None


# Update get_user_playlists function in spotify_utils.py
def get_user_playlists(token_info, limit=50, offset=0):
    sp = create_spotify_client(token_info)
    try:
        playlists = sp.current_user_playlists(limit=limit, offset=offset)
        playlists_info = []
        for playlist in playlists['items']:
            playlist_name = playlist['name']
            playlist_link = playlist['external_urls']['spotify']
            image_url = playlist['images'][0]['url'] if playlist['images'] else None
            playlists_info.append({
                'name': playlist_name,
                'link': playlist_link,
                'image_url': image_url
            })
        return playlists_info
    except Exception as e:
        print(f"Error getting user playlists: {e}")
        return None





