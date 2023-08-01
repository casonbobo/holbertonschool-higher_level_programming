#!/usr/bin/node
exports.converter = function (base) {
  return function convertToBaseN (num) {
    return (num.toString(base));
  };
};
