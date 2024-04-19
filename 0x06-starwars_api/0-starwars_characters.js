#!/usr/bin/node

const request = require("request");
const idd = process.argv[2];

const findMovie = (idd) => {
  const url = `https://swapi-api.alx-tools.com/api/films/${idd}`;

  request(url, (error, response, body) => {
    if (error) {
      console.error("Error:", error);
      return;
    }
    const data = JSON.parse(body);
    const charactersLinks = data.characters;
    for (const link of charactersLinks) {
      request(link, (err, res, body) => {
        if (err) {
          console.error("Error:", err);
          return;
        }
        const characterData = JSON.parse(body);
        return characterData.name;
      });
    }
  });
};

findMovie(idd);
