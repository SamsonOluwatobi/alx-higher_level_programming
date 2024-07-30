#!/usr/bin/node
/*
  This script reads and prints the content of a file.
  The first argument is the path to the file to be read.
  The content of the file is read in utf-8 encoding.
*/

const { readFile } = require('fs');
const filePath = process.argv[2];

// The handler function is a callback that is called when the file is read.
// It logs an error if there is one, otherwise it logs the content of the file.
const handler = (err, data) => {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
};

// Read the file and pass the handler function to be called when done.
readFile(filePath, 'utf8', handler);
