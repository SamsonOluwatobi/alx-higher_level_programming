$(document).ready(function () {
  const URL = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
  const handler = function (data) {
    const translation = data.hello;
    $('DIV#hello').text(translation);
  };

  $.getJSON(URL, handler);
});
