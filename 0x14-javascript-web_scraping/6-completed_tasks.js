#!/usr/bin/node
const request = require('request');
const apiurl = process.argv[2];
let jsonData;
const dictionary = {};

request(apiurl, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    jsonData = JSON.parse(body);
    jsonData.forEach(function (result) {
      if (result.completed === true) {
        const userid = result.userId;
        if (!(userid in dictionary)) {
          dictionary[userid] = 0;
        }
        dictionary[userid] += 1;
      }
    });
    console.log(dictionary);
  }
});
