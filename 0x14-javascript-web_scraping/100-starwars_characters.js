#!/usr/bin/node
const request = require('request');
const movieID = process.argv[2];
const apiurl = 'https://swapi-api.hbtn.io/api/films/' + movieID;
request(apiurl, function (err, response, body) {
  if (err) {
    console.error(err);
  }
  const jsonData = JSON.parse(body).characters;
  for (const character of jsonData) {
    request(character, function (error, response, content) {
      if (error) {
        console.log(error);
      }
      const data = JSON.parse(content);
      console.log(data.name);
    });
  }
});
