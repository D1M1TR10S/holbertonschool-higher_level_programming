#!/usr/bin/node
exports.callMeMoby = function (times, func) {
  i = 0;
  for (i; i < times; i++) {
    func();
  }
};
