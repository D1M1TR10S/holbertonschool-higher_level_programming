$(function()
{
  $.get("https://swapi.co/api/films/?format=json", function(data)
  {
    for (let name of data.results) {
      $("#list_movies").append('<li>' + name.title + '</li>')
    }
  });
});
