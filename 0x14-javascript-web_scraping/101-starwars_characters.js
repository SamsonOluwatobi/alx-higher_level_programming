#!/usr/bin/node
/**
 * Script that prints all characters of a Star Wars movie:
 *  - The first argument is the Movie ID - example: 3 = "Return of the Jedi"
 *  - Display one character name by line in the same order of the list "characters" in the /films/ response
 *  - Must use the Star wars API
 *  - Must use the module request
 *
 * How it works:
 *  - The movie ID is retrieved from the command line arguments
 *  - The URL of the movie is constructed using the movie ID
 *  - The "request" module is used to send an HTTP GET request to the movie URL
 *  - The response is parsed as JSON and the "characters" property is extracted
 *  - The characters are looped through and their names are printed to the console
 *  - If there is an error, it is logged to the console
 */

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;
const { get } = require('request');
const { promisify } = require('util');
const getCharacter = promisify(get);

async function printCharacterName (url) {
  try {
    const character = await getCharacter(url);
    console.log(JSON.parse(character.body).name);
  } catch (error) {
    console.log(error);
  }
}
const filmHandler = async (error, response, body) => {
  if (!error && response.statusCode === 200) {
    if (typeof body === 'string') {
      body = JSON.parse(body);
    }
    const characters = body.characters;
    for (const character of characters) {
      await printCharacterName(character);
    }
  }
};
get(url, filmHandler);
