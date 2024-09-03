#!/usr/bin/node

const request = require('request');
const specifiedMovieId = process.argv[2];
const url = `https://swapi.dev/api/films/${specifiedMovieId}/`;

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  const movieInfo = JSON.parse(body);
  const characters = movieInfo.characters;

  const characterPromises = characters.map(characterUrl => {
    return new Promise((resolve, reject) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          reject(error);
        } else {
          const characterInfo = JSON.parse(body);
          resolve(characterInfo.name);
        }
      });
    });
  });

  Promise.all(characterPromises)
    .then(characterNames => {
      characterNames.forEach(name => console.log(name));
    })
    .catch(error => console.error('Error:', error));
});
