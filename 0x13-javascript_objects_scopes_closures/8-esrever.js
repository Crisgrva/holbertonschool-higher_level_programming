#!/usr/bin/node
exports.esrever = function (list) {
  let newArray = [];
  for (let i = list.length - 1; i >= 0; i--) {
    newArray.push(list[i]);
  }
  return newArray;
};
