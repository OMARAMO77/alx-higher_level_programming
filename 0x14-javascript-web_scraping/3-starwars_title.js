#!/usr/bin/node
const request = require('request');
const movieID = process.argv[2];
const apiurl = 'https://swapi-api.hbtn.io/api/films/' + movieID;
let jsonData;

request(apiurl, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    jsonData = JSON.parse(body);
    console.log(jsonData.title);
  }
});
