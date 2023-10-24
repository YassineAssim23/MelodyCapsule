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









