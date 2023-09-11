#!/usr/bin/node

const argLen = process.argv.length;
if (argLen > 3) {
  console.log('Arguments found');
} else if (argLen === 3) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
