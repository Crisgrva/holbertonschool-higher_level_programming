// Script that fetch API and put fetched data
$(document).ready(function () {
  const URL = 'https://fourtonfish.com/hellosalut/?lang=fr';
  $.get(URL, function (data) {
    $('DIV#hello').text(data.hello);
  });
});
