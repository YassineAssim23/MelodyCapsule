from flask import Flask, request, session, redirect, url_for, render_template
from spotify_utils import get_user_top_tracks, get_user_top_artists, get_user_info, get_recently_played, get_user_devices, get_user_playlists
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()

CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

# Define TOKEN_INFO constant
TOKEN_INFO = 'token_info'

def create_spotify_oauth():
    return SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri="http://127.0.0.1:5000/redirectPage", 
        scope="user-top-read user-library-read user-read-recently-played user-read-playback-state"
    )

app = Flask(__name__)

app.secret_key = os.getenv("FLASK_SECRET_KEY")

@app.route('/')
def homepage():
    return render_template('index.html', title='Welcome to MelodyCapsule!')

@app.route('/dashboard')
def dashboard():
    user_token = get_token()
    if user_token:
        # Get user information and devices separately
        user_info = get_user_info(user_token)
        devices = get_user_devices(user_token)

        if user_info is not None and devices is not None:
            # If both user information and devices are retrieved successfully, pass them to the template
            return render_template('dashboard.html', title='Welcome to MelodyCapsule!', user_info=user_info, devices=devices)
        else:
            # Handle the case when either user information or devices retrieval fails
            error_message = "Error retrieving user information or devices. Please try again later."
            return render_template('error.html', error_message=error_message)
    else:
        # Handle the case when the user is not authenticated
        return render_template('error.html', error_message="User not authenticated. Please login first.")



@app.route('/login')
def login():
    sp_oauth = SpotifyOAuth(
        client_id = CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri="http://127.0.0.1:5000/redirectPage",
        scope="user-top-read user-library-read user-read-recently-played user-read-playback-state"
    )
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)


@app.route('/redirectPage')
def redirectPage():
    code = request.args.get('code')
    sp_oauth = SpotifyOAuth(
        client_id = CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri="http://127.0.0.1:5000/redirectPage",
        scope="user-top-read user-library-read user-read-recently-played user-read-playback-state"
    )
    token_info = sp_oauth.get_access_token(code)
    session[TOKEN_INFO] = token_info
    return redirect(url_for("dashboard"))

def get_token():
    token_info = session.get(TOKEN_INFO, None)
    return token_info

# Assuming you have a 'dashboard' route defined like this
@app.route('/toptracks')
def toptracks():
    user_token = get_token()
    if user_token:
        tracks_info = get_user_top_tracks(user_token)
        if tracks_info:
            return render_template('toptracks.html', title='Welcome to MelodyCapsule!', tracks_info=tracks_info)
        else:
            error_message = "Error retrieving top tracks. Please try again later."
            return render_template('error.html', error_message=error_message)
    else:
        error_message = "User not authenticated. Please login first."
        return render_template('error.html', error_message=error_message)
    
# Assuming you have a 'dashboard' route defined like this
@app.route('/topartists')
def topartists():
    user_token = get_token()
    if user_token:
        artists_info = get_user_top_artists(user_token)
        if artists_info:
            return render_template('topartists.html', title='Welcome to MelodyCapsule!', artists_info=artists_info)
        else:
            error_message = "Error retrieving top tracks. Please try again later."
            return render_template('error.html', error_message=error_message)
    else:
        error_message = "User not authenticated. Please login first."
        return render_template('error.html', error_message=error_message)


# Assuming you have a 'dashboard' route defined like this
@app.route('/recentlyplayed')
def recentlyplayed():
    user_token = get_token()
    if user_token:
        recentlyplayed = get_recently_played(user_token)
        if recentlyplayed:
            return render_template('recentlyplayed.html', title='Welcome to MelodyCapsule!', recentlyplayed=recentlyplayed)
        else:
            error_message = "Error retrieving top tracks. Please try again later."
            return render_template('error.html', error_message=error_message)
    else:
        error_message = "User not authenticated. Please login first."
        return render_template('error.html', error_message=error_message)


@app.route('/playlist')
def playlists():
    user_token = get_token()
    if user_token:
        playlists_info = get_user_playlists(user_token)
        if playlists_info:
            return render_template('playlist.html', title='User Playlists', playlists_info=playlists_info)
        else:
            error_message = "Error retrieving user playlists. Please try again later."
            return render_template('error.html', error_message=error_message)
    else:
        error_message = "User not authenticated. Please login first."
        return render_template('error.html', error_message=error_message)



