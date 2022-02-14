// Script that fetch API and add element for each element in fetched data
$(document).ready(function () {
  const URL = 'https://swapi-api.hbtn.io/api/films/?format=json';
  $.get(URL, function (movies) {
    for (const movie of movies.results) {
      $('UL#list_movies').append('<li>' + movie.title + '</li>');
    }
  });
});
