# MelodyCapsule

MelodyCapsule is a web application that allows users to explore their Spotify music preferences in an interactive and visually appealing way. Users can log in with their Spotify accounts, granting the application access to their music library. MelodyCapsule provides insights into the user's top tracks, top artists, recently played tracks, playlists, and more.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Introduction

MelodyCapsule is an innovative web application designed for music enthusiasts and Spotify users seeking a deeper understanding of their musical preferences. In today's digital age, where streaming platforms offer vast libraries of songs, playlists, and artists, users often find it challenging to track and analyze their listening habits comprehensively. MelodyCapsule addresses this challenge by providing users with a centralized platform to explore and interpret their Spotify music data.

## Features

- Top Track Analysis: MelodyCapsule analyzes the user's top tracks based on different time ranges (short term, medium term, long term), providing detailed information such as track name, artist, album, and links to Spotify for further exploration.
- Top Artists Analysis:  Users can explore their favorite artists within specific time ranges, revealing artist names, external Spotify links, and artist images for a visually engaging experience.
- Recently Played Tracks: MelodyCapsule displays the user's recently played tracks, including track name, artist, album, played timestamp (formatted as M:D:Y HH:MM:SS), and external Spotify links for each track.
- User Playlists: Users can view their playlists, including playlist names, external Spotify links, and cover images (if available), allowing them to revisit their curated music collections.

## Getting Started

To run MelodyCapsule on your local machine, follow these steps:


## Prerequisites

Before you can run MelodyCapsule on your local machine, make sure you have the following software, libraries, and tools installed:

- **Python 3:** MelodyCapsule is a Python-based web application. Ensure you have Python 3.6 or higher installed on your system. You can download Python from the [official Python website](https://www.python.org/downloads/).

- **Spotify Account:** You need a Spotify account to log in and authenticate with the application. If you don't have one, you can create a Spotify account for free at [Spotify's website](https://www.spotify.com/).

- **Python Libraries:** Install the required Python packages by running the following command in your project directory:
  ```bash
  pip install -r requirements.txt
  

## Environment Variables

Create a file named `.env` in the root directory of your project. Add the following lines to the `.env` file, replacing the placeholders with your actual Spotify API credentials and Flask secret key:
    ```env
SPOTIPY_CLIENT_ID='your_spotify_client_id'
SPOTIFY_CLIENT_SECRET='your_spotify_client_secret'
SPOTIPY_REDIRECT_URI='http://127.0.0.1:5000/redirectPage'
FLASK_SECRET_KEY='your_flask_secret_key'

### Installation

Step-by-step guide on how to install your project.

1. Clone the repository: `git clone https://github.com/YassineAssim23/MelodyCapsule.git`
2. Change directory: `cd MelodyCapsule/src`
3. Install dependencies: `pip install -r requirements.txt`
4. Run Application: `flask run`


## Usage

MelodyCapsule allows you to explore your Spotify music data in various ways. Here's how you can use the different features of the application:
1. Logging In:

    When you access MelodyCapsule in your web browser (http://127.0.0.1:5000), you'll be prompted to log in with your Spotify account. Click on the "Login" button to authenticate.

2. Dashboard:

    After logging in, you'll be redirected to the dashboard. Here, you can view your user information, such as your display name, followers count, and the number of people you're following on Spotify.
    You can also see the devices connected to your Spotify account.

3. Top Tracks:

    Navigate to the "Top Tracks" section by clicking on the "Top Tracks" link in the navigation menu.
    Choose a time range (Short Term, Medium Term, Long Term) to view your top tracks during that period.
    MelodyCapsule will display a list of your top tracks, including the track name, artist, album, and a link to listen on Spotify.

4. Top Artists:

    Go to the "Top Artists" section by clicking on the "Top Artists" link in the navigation menu.
    Similar to top tracks, select a time range to view your top artists.
    MelodyCapsule will show a list of your top artists, along with their names and a link to their Spotify profiles.

5. Recently Played Tracks:

    Visit the "Recently Played Tracks" section by clicking on the "Recently Played" link in the navigation menu.
    You'll see a list of tracks you recently played on Spotify, including the track name, artist, album, and the time it was played.

6. Playlists:

    Explore your playlists by clicking on the "Playlists" link in the navigation menu.
    MelodyCapsule will display your playlists, showing the playlist name, and a link to view the playlist on Spotify.

7. Logging Out:

    To log out, click on the "Logout" link in the navigation menu. This will clear your session and redirect you to the homepage.

## Contributing

We welcome contributions from the community to enhance MelodyCapsule. If you would like to contribute, please follow these guidelines:
Reporting a Bug

If you encounter a bug while using MelodyCapsule, please create a detailed bug report. Include information such as the steps to reproduce the bug, the expected behavior, and the actual behavior you observed. You can open a new issue on the GitHub repository to report the bug.
Discussing the Code

If you want to discuss specific parts of the codebase, you can open a discussion on GitHub. Feel free to ask questions, propose ideas, or provide feedback.
Fork the Repository

To contribute to MelodyCapsule, you'll need to fork the repository. Click the "Fork" button at the top right corner of the GitHub repository page to create your own copy of the repository.


## License

MelodyCapsule is licensed under the MIT License. This means that you are free to use, modify, and distribute the project for both commercial and non-commercial purposes, subject to the conditions and limitations of the MIT License.

For the detailed terms and conditions, please refer to the LICENSE.md file in this repository. By using, modifying, or distributing MelodyCapsule, you agree to the terms and conditions outlined in the license file.

## Acknowledgements

We would like to express our gratitude to the following individuals and organizations for their contributions, inspiration, and resources that helped make MelodyCapsule possible:

    The developers and maintainers of the Flask web framework and Spotipy library, which were instrumental in building this application.
    The entire open-source community for creating an environment where knowledge sharing and collaboration thrive.
    Our users and contributors who provided valuable feedback and suggestions, helping us improve MelodyCapsule.
    Spotify for providing the Spotify Web API, enabling developers to access and interact with Spotify's vast music catalog.
    The creators of various Python libraries and tools that MelodyCapsule utilizes, making the development process more efficient and enjoyable.

Thank you for your support and contributions to the MelodyCapsule project!
