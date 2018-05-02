#!/usr/bin/node
let num = Number(process.argv[2]);
if (isNaN(num)) {
  console.log(1);
} else {
  let factorial = function (number) {
    if (number <= 0) {
      return 1;
    } else {
      return (number * factorial(number - 1));
    }
  };
  console.log(factorial(num));
}
