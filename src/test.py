import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()

CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri="http://127.0.0.1:5000/redirectPage",
    scope="user-top-read user-library-read"
))

# Get the current user's top tracks
top_artists = sp.current_user_top_(limit=10, time_range="medium_term")

# Print the dictionary to explore its structure
print(top_artists)
