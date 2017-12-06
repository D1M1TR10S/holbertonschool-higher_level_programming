#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
print("Last digit of {:d} is".format(number), end=" ")
digit = number % 10
if number < 0:
    digit = (-1 * number) % 10 * -1
if digit > 5:
    print("{} and is greater than 5".format(digit))
elif digit == 0:
    print("{} and is 0".format(digit))
elif digit < 6 and digit != 0:
    print("{} and is less than 6 and not 0".format(digit))
