#!/usr/bin/node

const size = parseInt(process.argv[2]);
if (size) {
  for (let j = 0; j < size; ++j) {
    console.log('X'.repeat(size));
  }
} else {
  console.log('Missing size');
}
