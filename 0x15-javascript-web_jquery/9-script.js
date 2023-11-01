const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$('document').ready(function () {
  $.get(url, function (body) {
    $('DIV#hello').text(body.hello);
  });
});
