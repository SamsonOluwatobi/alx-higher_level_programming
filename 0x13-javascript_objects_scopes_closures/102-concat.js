#!/usr/bin/node

// Script that concatenates two files.
// The first argument is the path of the first source file.
// The second argument is the path of the second source file.
// The third argument is the path of the destination file.

const { readFile, appendFileSync } = require('fs');
const [fileA, fileB, outputFile] = process.argv.slice(2);

readFile(fileA, (err, data) => {
  if (err) throw err;
  appendFileSync(outputFile, data);
});

readFile(fileB, (err, data) => {
  if (err) throw err;
  appendFileSync(outputFile, data);
});
