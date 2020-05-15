$(function(){
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data, status) {
    if (status === 'success') {
      let movies = data.results;
      for (let eaMovie of movies) {
        $('ul#list_movies').append('<li>' + eaMovie.title + '</li>');
      }
    }
  });
});
