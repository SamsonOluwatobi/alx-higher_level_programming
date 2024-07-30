#!/usr/bin/node
/*
  This script gets the contents of a webpage and stores it in a file.
  - The first argument is the URL to request.
  - The second argument is the file path to store the body response.
  - The file must be UTF-8 encoded.
*/

// Import the functions to read from the file system and make HTTP requests
const { writeFile } = require('fs');
const { get } = require('request');

// Get the URL and file path from the command line arguments
const [url, filePath] = process.argv.slice(2);

// Define a function to handle any errors that occur during the HTTP request
const responseHandler = error => {
  if (error) console.log(error);
};

// Define a function to handle the HTTP response
const requestHandler = (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    // Write the body of the response to the file with UTF-8 encoding
    // and call the responseHandler function when done
    writeFile(filePath, body, 'utf8', responseHandler);
  }
};

// Send an HTTP GET request to the URL and pass the requestHandler function
// as the callback to handle the response
get(url, requestHandler);
