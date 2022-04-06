#!/usr/bin/node

exports.converter = function (base) {
  return function (decimal) {
    return decimal * base;
  };
};
