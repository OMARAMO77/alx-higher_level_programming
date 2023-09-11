#!/usr/bin/node
function factorial (num) {
  if (num === 0 || isNaN(num)) {
    return (1);
  }
  return (factorial(num - 1) * num);
}

const num = parseInt(process.argv[2]);
console.log(factorial(num));
