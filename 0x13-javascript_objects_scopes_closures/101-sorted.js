#!/usr/bin/node

/**
 * Script that imports a dictionary of occurrences by user ID and
 * computes a dictionary of user IDs by occurrence.
 *
 * In the new dictionary:
 * - A key is a number of occurrences
 * - A value is the list of user IDs
 */

const data = require('./101-data.js').dict;
const ocurrences = {};
for (const key in data) {
  const index = data[key];
  if (ocurrences[index] === undefined) {
    ocurrences[index] = [];
  }
  ocurrences[index].push(key);
}

console.log(ocurrences);
