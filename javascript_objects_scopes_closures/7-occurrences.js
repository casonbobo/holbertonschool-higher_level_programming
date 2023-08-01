#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  const occurrences = {};
  for (const item of list) {
    occurrences[item] = occurrences[item] ? occurrences[item] + 1 : 1;
  }
  return occurrences;
};
