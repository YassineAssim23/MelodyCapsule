from flask import Flask, request, send_from_directory, session, redirect, url_for, render_template
import spotify_utils
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()

# Load client ID and client secret from environment variables
CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

# Define TOKEN_INFO constant for session storage
TOKEN_INFO = 'token_info'

# Function to create Spotify OAuth object
def create_spotify_oauth():
    return SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        redirect_uri="http://127.0.0.1:5000/redirectPage", 
        scope="user-top-read user-library-read user-read-recently-played user-read-playback-state user-read-private user-read-email user-follow-read"
    )

app = Flask(__name__)

# Static files route for custom fonts
@app.route('/fonts/<path:filename>')
def custom_static(filename):
    root_dir = os.path.dirname(os.getcwd())  # Get the parent directory of your Flask app
    return send_from_directory(os.path.join(root_dir, 'src', 'templates', 'fonts'), filename)

# Disable caching for all responses
@app.after_request
def add_header(response):
    response.cache_control.no_store = True
    return response

# Set Flask secret key for session management
app.secret_key = os.getenv("FLASK_SECRET_KEY")

# Homepage route
@app.route('/')
def homepage():
    return render_template('index.html', title='Welcome to MelodyCapsule!')

# Dashboard route for user information and devices
@app.route('/dashboard')
def dashboard():
    user_token = get_token()
    
    if user_token:
        # Get user information and devices separately
        user_info = spotify_utils.get_user_info(user_token)
        followers_count = spotify_utils.get_user_followers(user_token)
        following_count = spotify_utils.get_user_following(user_token)
        devices = spotify_utils.get_user_devices(user_token)

        if user_info is not None and devices is not None:
            # If both user information and devices are retrieved successfully, pass them to the template
            return render_template('dashboard.html', title='Welcome to MelodyCapsule!', user_info=user_info, followers_count=followers_count, following_count=following_count, devices=devices)
        else:
            # Handle the case when either user information or devices retrieval fails
            error_message = "Error retrieving user information or devices. Please try again later."
            return render_template('error.html', error_message=error_message)
    else:
        # Handle the case when the user is not authenticated
        return render_template('error.html', error_message="User not authenticated. Please login first.")
        
# Login route, redirects to Spotify authorization page
@app.route('/login')
def login():
    sp_oauth = create_spotify_oauth()
    auth_url = sp_oauth.get_authorize_url()
    return redirect(auth_url)

# Logout route, clears session data
@app.route('/logout')
def logout():
    # Clear the session data (token information)
    session.pop(TOKEN_INFO, None)
    # Redirect the user to the homepage after logout
    return redirect(url_for('homepage'))

# Redirect route after Spotify authorization
@app.route('/redirectPage')
def redirectPage():
    code = request.args.get('code')
    sp_oauth = create_spotify_oauth()
    token_info = sp_oauth.get_access_token(code)
    session[TOKEN_INFO] = token_info
    return redirect(url_for("dashboard"))

# Function to retrieve user token from session
def get_token():
    token_info = session.get(TOKEN_INFO, None)
    return token_info

# Route to display user's top tracks
@app.route('/toptracks')
def toptracks():
    user_token = get_token()
    time_range = request.args.get('time-range', default='medium_term', type=str)
    
    if time_range not in ['short_term', 'medium_term', 'long_term']:
        # Handle invalid time_range parameter
        return render_template('error.html', error_message="Invalid time_range parameter.")
    
    if user_token:
        tracks_info = spotify_utils.get_user_top_tracks(user_token, time_range=time_range)
        
        if tracks_info:
            return render_template('toptracks.html', title='Welcome to MelodyCapsule!', tracks_info=tracks_info, selected_time_range=time_range)
        else:
            error_message = "Error retrieving top tracks. Please try again later."
            return render_template('error.html', error_message=error_message)
    else:
        error_message = "User not authenticated. Please login first."
        return render_template('error.html', error_message=error_message)

# Route to display user's top artists
@app.route('/topartists')
def topartists():
    user_token = get_token()
    selected_time_range = request.args.get('time_range', default='short_term', type=str)
    if user_token:
        artists_info = spotify_utils.get_user_top_artists(user_token)
        if artists_info:
            return render_template('topartists.html', title='Welcome to MelodyCapsule!', artists_info=artists_info, selected_time_range=selected_time_range)
        else:
            error_message = "Error retrieving top tracks. Please try again later."
            return render_template('error.html', error_message=error_message)
    else:
        error_message = "User not authenticated. Please login first."
        return render_template('error.html', error_message=error_message)

# Route to display user's recently played tracks
@app.route('/recentlyplayed')
def recentlyplayed():
    user_token = get_token()
    if user_token:
        recentlyplayed = spotify_utils.get_recently_played(user_token)
        if recentlyplayed:
            return render_template('recentlyplayed.html', title='Welcome to MelodyCapsule!', recentlyplayed=recentlyplayed)
        else:
            error_message = "Error retrieving top tracks. Please try again later."
            return render_template('error.html', error_message=error_message)
    else:
        error_message = "User not authenticated. Please login first."
        return render_template('error.html', error_message=error_message)

# Route to display user's playlists
@app.route('/playlist')
def playlists():
    user_token = get_token()
    if user_token:
        playlists_info = spotify_utils.get_user_playlists(user_token)
        if playlists_info:
            return render_template('playlist.html', title='User Playlists', playlists_info=playlists_info)
        else:
            error_message = "Error retrieving user playlists. Please try again later."
            return render_template('error.html', error_message=error_message)
    else:
        error_message = "User not authenticated. Please login first."
        return render_template('error.html', error_message=error_message)
