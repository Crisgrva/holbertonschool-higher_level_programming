// Script that fetch API and change text from data fetched
$(document).ready(function () {
  const URL = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
  $.get(URL, function (character) {
    $('DIV#character').text(character.name);
  });
});
