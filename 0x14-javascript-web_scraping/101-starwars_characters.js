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

function printCharacters (characters, index) {
  request(characters[index], function (error, response, content) {
    if (!error) {
      console.log(JSON.parse(content).name);
      if (index + 1 < characters.length) {
        printCharacters(characters, index + 1);
      }
    }
  });
}
