#!/usr/bin/node
/*
  This script prints the names of all characters from a specific Star Wars movie.

  The first argument is the Movie ID - example: 3 = "Return of the Jedi"

  It makes use of the Star Wars API to fetch the characters of the selected movie.
  The module 'request' is used to send HTTP GET requests to the API.

  The names of the characters are printed one by one, each on a new line.
*/

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
const { get } = require('request');

// Function to handle the character response
const characterHandler = (error, response, body) => {
  if (error) console.log(error);
  console.log(JSON.parse(body).name);
};

// Function to handle the film response
const filmHandler = (error, response, body) => {
  if (!error && response.statusCode === 200) {
    if (typeof body === 'string') {
      body = JSON.parse(body);
    }
    const characters = body.characters;
    for (const character of characters) {
      get(character, characterHandler);
    }
  }
};

// Send a GET request to the URL and pass the filmHandler function as the callback
get(url, filmHandler);

