#!/usr/bin/node
/*
  This script counts the number of movies in which the character
  "Wedge Antilles" (character ID 18) appears. The first argument is the
  URL of the Star Wars API's films endpoint.
*/

const url = process.argv[2];
const wedgeId = '18';
const { get } = require('request');

// Define a handler function that logs the number of movies where
// "Wedge Antilles" appears
const handler = (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    if (typeof body === 'string') {
      body = JSON.parse(body);
    }
    let count = 0;
    const movies = body.results;
    for (const movie of movies) {
      const characterCount = movie.characters.filter((data) => {
        return data.includes(wedgeId);
      });
      count += characterCount.length;
    }
    console.log(count);
  }
};

// Send a GET request to the URL and pass the handler function as the callback
get(url, handler);
