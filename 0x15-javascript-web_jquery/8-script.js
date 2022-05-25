// Write a JavaScript script that fetches and lists the title for all movies by using this URL: https://swapi-api.hbtn.io/api/films/?format=json

// All movie titles must be list in the HTML tag UL#list_movies

$(function () {
    $.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
        $.each(data.results, function (i, movie) {
            $('#list_movies').append('<li>' + movie.title + '</li>');
        });
    });
});
