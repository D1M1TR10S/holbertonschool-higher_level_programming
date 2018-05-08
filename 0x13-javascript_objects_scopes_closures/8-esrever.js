#!/usr/bin/node
exports.esrever = function (list) {
  var res = new Array;
  for(var i = list.length-1; i >= 0; i--) {
      res.push(list[i]);
  }
  return res; 
};
