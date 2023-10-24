#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const apiurl = process.argv[2];
const file = process.argv[3];

request(apiurl, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    fs.writeFile(file, body, 'utf8', function (error, data) {
      if (error) {
        console.error(error);
      }
    });
  }
});
