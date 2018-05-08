#!/usr/bin/node
// A script that converts a number to the base passed

exports.converter = function (base) {
  function convert (n) {
    return n.toString(base);
  }
  return convert;
};
