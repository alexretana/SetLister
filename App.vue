<template>
  <div>
    <div>
      <label for="search-bar">Search for an artist:</label>
      <input id="search-bar" v-model="searchTerm" @input="searchArtists" />
    </div>
    <div v-if="searchResults.length > 0">
      <ul>
        <li v-for="artist in searchResults" :key="artist.mbid">
          <a @click="getSetlist(artist.mbid)">{{ artist.name }}</a>
        </li>
      </ul>
    </div>
    <div v-if="setlist.length > 0">
      <h2>{{ selectedArtist }}</h2>
      <ul>
        <li v-for="song in setlist" :key="song">
          {{ song}}
        </li>
      </ul>
    </div>
    <div>
      <button @click="loginWithSpotify">Login with Spotify</button>
    </div>
    <div v-if="isLoggedIn">
      <label for="playlist-title">Enter a title for your playlist:</label>
      <input id="playlist-title" v-model="playlistTitle" />
      <button @click="createPlaylist">Create Playlist</button>
      <div v-if="isLoading">
        Loading...
      </div>
      <div v-if="playlistId">
        Playlist created with id: {{playlistId}}
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      searchTerm: "",
      searchResults: [],
      selectedArtist: "",
      setlist: [],
      isLoggedIn: false,
      playlistTitle: "",
      isLoading: false,
      playlistId: ""
    };
  },
  methods: {
    searchArtists() {
      axios
        .get(`https://api.setlist.fm/rest/1.0/search/artists?artistName=${this.searchTerm}`)
        .then(response => {
          this.searchResults = response.data.artist;
        });
    },
    getSetlist(mbid) {
      axios
        .get(`https://api.setlist.fm/rest/1.0/artist/${mbid}/setlists`)
        .then(response => {
          this.selectedArtist = response.data.setlist[0].artist.name;
          this.setlist = response.data.setlist[0].sets.set[0].song;
        });
    },
    loginWithSpotify() {
      // Add code to open Spotify login window and handle authorization
    },
    createPlaylist() {
      this.isLoading = true;
      // Code to create a playlist on Spotify using the Spotify Web API
      // and the title specified in the input field
      // Example code for creating a playlist:
      // axios
      //
