$(document).ready(function () {
  const URL = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
  $.getJSON(URL, (data) => $('DIV#character').text(data.name));
});
