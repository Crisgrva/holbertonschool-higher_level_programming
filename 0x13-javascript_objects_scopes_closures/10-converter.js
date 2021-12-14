#!/usr/bin/node
exports.converter = function (base) {
  function baseConvert (number) {
    return number.toString(base);
  }
  return baseConvert;
};
