#!/usr/bin/python3
""" 4 Text indentation"""


def text_indentation(text):
    """
    this indents text a distance
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    new_line = True

    for char in text:
        if char != ' ' or new_line is False:
            print(char, end='')
            new_line = False
        elif char != ' ':
            new_line = False

        if char in ['.', '?', ':']:
            print()
            print()
            new_line = True
