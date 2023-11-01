$(document).ready(function () {
  $('#btn_translate').click(function () {
    const languageCode = $('#language_code').val();
    const apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/';
    const url = `${apiUrl}?lang=${languageCode}`;

    $.get(url, function (data) {
      $('#hello').text(data.hello);
    });
  });
});
