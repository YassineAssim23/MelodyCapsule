from flask import request
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
from datetime import datetime

# Load Spotify API credentials from environment variables
load_dotenv()

# Get Spotify API credentials from environment variables
CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")
REDIRECT_URI = "http://127.0.0.1:5000/redirectPage"


# Function to create a Spotify client using token information
def create_spotify_client(token_info):
    return spotipy.Spotify(auth=token_info["access_token"])


# Function to get the user's top tracks for a specific time range
def get_user_top_tracks(token_info, limit=50, time_range="medium_term"):
    # Create a Spotify client using token information
    sp = create_spotify_client(token_info)
    try:
        # Get the user's top tracks based on the specified time range
        top_tracks = sp.current_user_top_tracks(limit=limit, time_range=time_range)
        tracks_info = []
        for track in top_tracks["items"]:
            # Extract track information
            track_name = track["name"]
            artist_name = track["artists"][0]["name"]
            album_name = track["album"]["name"]
            album_link = track["album"]["external_urls"]["spotify"]
            track_link = track["external_urls"]["spotify"]
            image_url = (
                track["album"]["images"][0]["url"] if track["album"]["images"] else None
            )
            # Add track information to the list
            tracks_info.append(
                {
                    "album_name": album_name,
                    "album_link": album_link,
                    "track_name": track_name,
                    "artist_name": artist_name,
                    "track_link": track_link,
                    "image_url": image_url,
                }
            )
        # Return the list of top tracks
        return tracks_info
    except Exception as e:
        print(f"Error getting top tracks: {e}")
        return None


# Function to get the user's top artists for a specific time range
def get_user_top_artists(token_info, limit=50):
    # Get the selected time range from the URL parameters
    selected_time_range = request.args.get(
        "time_range", default="medium_term", type=str
    )
    # Create a Spotify client using token information
    sp = create_spotify_client(token_info)
    try:
        # Get the user's top artists based on the specified time range
        top_artists = sp.current_user_top_artists(
            limit=limit, time_range=selected_time_range
        )
        artists_info = []
        for artist in top_artists["items"]:
            # Extract artist information
            artist_name = artist["name"]
            artist_link = artist["external_urls"]["spotify"]
            image_url = artist["images"][0]["url"] if artist["images"] else None
            # Add artist information to the list
            artists_info.append(
                {
                    "artist_name": artist_name,
                    "artist_link": artist_link,
                    "image_url": image_url,
                }
            )
        # Return the list of top artists
        return artists_info
    except Exception as e:
        print(f"Error getting top artists: {e}")
        return None


# Function to get the user's information
def get_user_info(token_info):
    # Create a Spotify client using token information
    sp = create_spotify_client(token_info)
    try:
        # Get the user's information
        user_info = sp.current_user()
        # Return the user's information
        return user_info
    except Exception as e:
        print(f"Error getting user information: {e}")
        return None


# Function to get the user's available devices
def get_user_devices(token_info):
    # Create a Spotify client using token information
    sp = create_spotify_client(token_info)
    try:
        # Get the user's available devices
        devices = sp.devices()
        return devices.get("devices", [])
    except Exception as e:
        print(f"Error getting user devices: {e}")
        return None


# Function to get the user's recently played tracks
def get_recently_played(token_info):
    # Create a Spotify client using token information
    sp = create_spotify_client(token_info)
    try:
        # Get the user's recently played tracks
        recently_played = sp.current_user_recently_played(
            limit=50, after=None, before=None
        )

        if "items" in recently_played:
            tracks_info = []
            for track in recently_played["items"]:
                # Extract recently played track information
                track_name = track["track"]["name"]
                artist_name = track["track"]["artists"][0]["name"]
                album_name = track["track"]["album"]["name"]
                # Convert the timestamp to the desired format (M:D:Y) (HH:MM:SS)
                played_at = datetime.strptime(
                    track["played_at"], "%Y-%m-%dT%H:%M:%S.%fZ"
                ).strftime("%m/%d/%Y %H:%M:%S")
                track_link = track["track"]["external_urls"]["spotify"]
                image_url = (
                    track["track"]["album"]["images"][0]["url"]
                    if track["track"]["album"]["images"]
                    else None
                )
                # Add recently played track information to the list
                tracks_info.append(
                    {
                        "name": track_name,
                        "artist": artist_name,
                        "album": album_name,
                        "played_at": played_at,
                        "track_link": track_link,
                        "image_url": image_url,
                    }
                )
            # Return the list of recently played tracks
            return tracks_info
        else:
            print("Unexpected response format from Spotify API:", recently_played)
            return None

    except Exception as e:
        print(f"Error getting recently played tracks: {e}")
        return None


# Function to get the user's playlists
def get_user_playlists(token_info, limit=50, offset=0):
    # Create a Spotify client using token information
    sp = create_spotify_client(token_info)
    try:
        # Get the user's playlists
        playlists = sp.current_user_playlists(limit=limit, offset=offset)
        playlists_info = []
        for playlist in playlists["items"]:
            # Extract playlist information
            playlist_name = playlist["name"]
            playlist_link = playlist["external_urls"]["spotify"]
            image_url = playlist["images"][0]["url"] if playlist["images"] else None
            # Add playlist information to the list
            playlists_info.append(
                {"name": playlist_name, "link": playlist_link, "image_url": image_url}
            )
        # Return the list of user playlists
        return playlists_info
    except Exception as e:
        print(f"Error getting user playlists: {e}")
        return None


# Function to get the user's followers
def get_user_followers(token_info):
    # Create a Spotify client using token information
    sp = create_spotify_client(token_info)
    try:
        # Get the user's followers
        user_info = sp.current_user()
        followers_count = user_info["followers"]["total"]
        return followers_count
    except Exception as e:
        print(f"Error getting user followers: {e}")
        return None


# Function to get the user's following (people they follow)
def get_user_following(token_info):
    # Create a Spotify client using token information
    sp = create_spotify_client(token_info)
    try:
        # Get the user's followed artists
        followed_artists = sp.current_user_followed_artists()
        following_count = followed_artists["artists"]["total"]
        return following_count
    except Exception as e:
        print(f"Error getting user following: {e}")
        return None
