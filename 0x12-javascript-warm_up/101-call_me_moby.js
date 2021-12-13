#!/usr/bin/node
exports.callMeMoby = function (a, b) {
  for (let times = 0; times < a; times++) {
    b();
  }
};
