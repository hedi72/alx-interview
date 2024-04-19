#!/usr/bin/node
const request = require("request");

const filmId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${filmId}/`;

const getCharacters = () => {
  return new Promise((resolve, reject) => {
    request(url, (err, res, body) => {
      if (err) {
        console.error("error:", err);
        reject(err);
      } else {
        const response = JSON.parse(body);
        const characters = response.characters;
        resolve(characters);
      }
    });
  });
};

const getNames = async () => {
  const characters = await getCharacters(filmId);

  for (const charUrl of characters) {
    const character = await new Promise((resolve, reject) => {
      request(charUrl, (err, res, body) => {
        if (err) {
          console.error("error:", err);
          reject(err);
        } else {
          const response = JSON.parse(body);
          resolve(response);
        }
      });
    });
    console.log(character.name);
  }
};

getNames();
