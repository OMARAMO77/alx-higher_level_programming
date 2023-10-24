#!/usr/bin/node
const request = require('request');
const apiurl = process.argv[2];
let jsonData;
let count = 0;
request(apiurl, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    jsonData = JSON.parse(body);
    jsonData.results.forEach(function (result) {
      result.characters.forEach(function (character) {
        const arr = character.split('/');
        if (arr[arr.length - 2] === '18') {
          count++;
        }
      });
    });
    console.log(count);
  }
});
