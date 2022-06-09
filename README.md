# SetLister
Creates a list of songs for the most likely set list for an artist

## Functionality:
Web App where you search an artist, and it provideds the most recent set list. Then allows you to make a playlist on Spotify.

## WorkFlow:
Home Page Has Search Bar, which return results of Artists
Selecting an artists will then display the most recent setlist from setlist.fm, which is done by making an api call to api.setlist.fm
There will be two buttons at the bottom: Spotify
Clicking on will pop-up authorization window for Spotify Login.
After completing authoiztion, an input field for the playlist's title will a appear as well as a button create and populate the playlist with the songs.
Show loading box, then result screen.

## Architechture:
Terraform for IaC

### Database:
To be built on:
SQLlite
(this will be backup by the snapshot of the server)

  Data we'll need
  List of Artist available on api.setlist.fm (~275,000 artists)

### Frontend:
AWS Amplify

### Backend:
Amazon Elastic Container Registry + Amazon Elastic Container Service
Docker: continuumio/miniconda3

## Code Stack:
### Frontend:
- Vue.js
- Vuetify
- typescript

### Backend:
- Python:
  - Flask
  - sqlite3
  - pandas + numpy
  - requests
  - repertorio
  - spotipy

# Development:
## Frontend UI:
- Title
- Search Bar
- Search Button
- Results List
- On-Click Result, Modal:
  - Setlist
  - Spotify Auth Launcher Button
  - Playlist Name
  - Make Playlist Button
  - Results Text
- About Page

## Backend:
- Artist List Scrapper
- SQLite Database Builder/Updater (If Does Not Exist)
- Artist Cursor (Artist Query)
- Setlist Retriever
- Spotify: Playlist Creater
- Spotify: Search Song
- Spotify: Add Song To Playlist
- Report Result
- Flask Endpoint

## Frontend UX:
- Artist List Search Request
- Artist Setlist Requester
- Spotify Authentication Launcher
- Spotify Request Playlist Creation
