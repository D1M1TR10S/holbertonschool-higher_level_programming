#!/usr/bin/python3
"""
This is the text_indentation module.
It supplies one function, text_indentation
"""
def text_indentation(text):
    """
    prints a string with two new lines after every ".", "?", ":"
    """
    new_string = ""
    if type(text) != str:
        raise TypeError('text must be a string')
    for i in range(len(text)):
        if i > 0:
            if text[i] == ' ' and text[i - 1] in ['.', '?', ':']:
                continue
        if text[i] != '.' and text[i] != '?' and text[i] != ':':
            new_string += text[i]
        else:
            new_string += text[i] + "\n\n"
    if new_string != "":
        print(new_string, end="")
    else:
        print()
