#!/usr/bin/python3
def no_c(my_string):
    new_string = []
    for i in range(len(my_string)):
        if my_string[i] is not "c" and my_string[i] is not "C":
            new_string.append(my_string[i])
    return (''.join(new_string))
