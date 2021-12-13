#!/usr/bin/node
exports.addMeMaybe = function (a, b) {
  a += 1;
  b(a);
};
