#!/usr/bin/node
const request = require('request');
const movieID = process.argv[2];
const apiurl = 'https://swapi-api.alx-tools.com/api/films/' + movieID;
request(apiurl, function (err, response, body) {
  if (!err) {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  }
});

function printCharacters (characters, idx) {
  request(characters[idx], function (error, response, content) {
    if (!error) {
      console.log(JSON.parse(content).name);
      if (idx + 1 < characters.length) {
        printCharacters(characters, idx + 1);
      }
    }
  });
}
