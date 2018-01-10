#!/usr/bin/python3
def magic_string():
    magic_string.c += 1; return ", ".join(["Holberton" for i in range(0, magic_string.c)])
magic_string.c = 0
