$(document).ready(function () {
  const URL = 'https://swapi-api.alx-tools.com/api/films/?format=json';
  const handler = function (data) {
    const movies = data.results;
    for (const movie of movies) {
      $('UL#list_movies').append(`<li>${movie.title}</li>`);
    }
  };

  $.getJSON(URL, handler);
});
