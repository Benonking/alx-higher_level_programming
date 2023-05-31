$(function () {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (res, status) {
    if (status === 'success') {
      const films = res.results;
      for (const idx in films) {
        $('#list_movies').append('<li>' + films[idx].title + '</li>');
      }
    }
  });
});
