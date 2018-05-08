#!/usr/bin/node
exports.esrever = function (list) {
  last = list.length - 1;
  return list.map((element, idx) => list[last - idx]);
};
