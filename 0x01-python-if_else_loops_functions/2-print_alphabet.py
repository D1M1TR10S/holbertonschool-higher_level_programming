#!/usr/bin/python3
for i in range(ord('a'), ord('z')+1):
    if i < ord('z'):
        print (chr(i), end="")
    else:
        print (chr(i))
