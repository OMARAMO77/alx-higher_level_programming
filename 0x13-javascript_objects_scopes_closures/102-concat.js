#!/usr/bin/node
const file = require('fs');
const line1 = file.readFileSync(process.argv[2]);
const line2 = file.readFileSync(process.argv[3]);
file.writeFileSync(process.argv[4], line1 + line2);
