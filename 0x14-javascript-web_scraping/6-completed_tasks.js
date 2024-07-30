#!/usr/bin/node
/*
  This script counts the number of completed tasks per user.
  - The first argument is the URL of the JSONPlaceholder API todos endpoint.
  - It uses the request module to send an HTTP GET request to the API.
  - The response body contains an array of todo objects, each with a "completed"
    property and a "userId" property.
  - The script filters the todo array to only include completed todos.
  - It then counts the number of completed todos per userId and logs the result.
*/

const url = process.argv[2];
const { get } = require('request');

const handler = (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    if (typeof body === 'string') {
      body = JSON.parse(body);
    }
    // Filter the todo array to only include completed todos.
    const completedTodos = body.filter((todo) => todo.completed);
    // Count the number of completed todos per userId.
    const tasksCompleted = completedTodos.reduce((count, todo) => {
      const key = todo.userId;
      if (key in count) {
        count[key] += 1;
      } else {
        count[key] = 1;
      }
      return count;
    }, {});
    console.log(tasksCompleted);
  }
};

get(url, handler);

