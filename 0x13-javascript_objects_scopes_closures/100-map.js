#!/usr/bin/node
const array = require('./100-data').list;
const newArray = array.map((x, idx) => x * idx);
console.log(array);
console.log(newArray);
