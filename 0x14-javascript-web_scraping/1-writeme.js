#!/usr/bin/node

/**
 * This script writes a string to a file. It takes two arguments:
 * - The first argument is the file path where the string will be written.
 * - The second argument is the string to write.
 * The content of the file will be written in UTF-8 encoding.
 *
 * @example
 * node 1-writeme.js data.txt "Hello, world!"
 */

const { writeFile } = require('fs');

// Get the file path and the string to write from the command line arguments
const [filePath, writeData] = process.argv.slice(2);

// Define a handler function to log any errors that occur during the write operation
const handler = error => {
  if (error) {
    console.log(error);
  }
};

// Write the string to the file with UTF-8 encoding and call the handler function
writeFile(filePath, writeData, 'utf8', handler);
