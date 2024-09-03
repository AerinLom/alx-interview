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
  characters.forEach(characterUrl => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error('Error:', error);
        return;
      }
      const characterInfo = JSON.parse(body);
      console.log(characterInfo.name);
    });
  });
});
