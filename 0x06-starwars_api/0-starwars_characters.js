const request = require("request");

const movieId = process.argv[2];

const SWAPI_URL = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request.get(SWAPI_URL, (error, response, body) => {
  if (error) {
    console.error("Error:", error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error("Status:", response.statusCode);
    return;
  }

  const film = JSON.parse(body);
  console.log(film.characters);
  const charactersUrls = film.characters;

  // Fetch characters' names
  charactersUrls.forEach((characterUrl) => {
    request.get(characterUrl, (error, response, body) => {
      if (error) {
        console.error("Error:", error);
        return;
      }

      if (response.statusCode !== 200) {
        console.error("Status:", response.statusCode);
        return;
      }

      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
});
