#!/usr/bin/node
exports.converter = function converter (base) {
  return a => a.toString(base);
};
