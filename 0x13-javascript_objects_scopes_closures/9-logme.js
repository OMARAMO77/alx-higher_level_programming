#!/usr/bin/node
exports.logMe = function logMe (item) {
  if (!logMe.count) {
    logMe.count = 0;
  }
  console.log(logMe.count + ': ' + item);
  logMe.count++;
};
