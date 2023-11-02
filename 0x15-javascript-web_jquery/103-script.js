$(document).ready(function () {
  $('#btn_translate, #language_code').on('click keypress', function (event) {
    if (event.type === 'click' || (event.type === 'keypress' && event.key === 'Enter')) {
      const languageCode = $('#language_code').val();
      const apiUrl = `https://www.fourtonfish.com/hellosalut/hello/?lang=${languageCode}`;

      $.get(apiUrl, function (data) {
        $('#hello').text(data.hello);
      });
    }
  });
});
