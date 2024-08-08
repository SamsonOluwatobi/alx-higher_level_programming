$(document).ready(function () {
  const URL = 'https://www.fourtonfish.com/hellosalut/hello/';
  $('INPUT#btn_translate').click(function () {
    const language = $('INPUT#language_code').val();
    const handler = function (data) {
      const translation = data.hello;
      $('DIV#hello').text(translation);
    };
    $.getJSON(URL, { lang: language }, handler);
  });
});
