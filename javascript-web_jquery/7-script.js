$(document).ready(function() {
  const apiUrl = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

  $.ajax({
    url: apiUrl,
    dataType: 'json',
    success: function(data) {
      $('#character').text(data.name);
    }
  });
});
