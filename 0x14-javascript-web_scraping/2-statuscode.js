#!/usr/bin/node
/*
  This script displays the status code of a GET request to a given URL.
  It takes one argument: the URL to request (GET).
  The status code is printed in the format "code: <status code>".
*/

const url = process.argv[2];
const { get } = require('request');

// Define a handler function that logs the status code of the response
const handler = (error, response) => {
  if (!error) {
    console.log(`code: ${response.statusCode}`);
  }
};

// Send a GET request to the URL and pass the handler function as the callback
get(url, handler);

