#!/usr/bin/node
const request = require('request');
const movieID = process.argv[2];
const api_url = 'https://swapi-api.hbtn.io/api/films/' + movieID;
let data;

request(api_url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    json_data = JSON.parse(body);
    console.log(json_data.title);
  }
});
