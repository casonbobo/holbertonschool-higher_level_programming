#!/usr/bin/python3
def no_c(my_string):
    new_string = ""
    for c in my_string:
        if c != "c" or "C":
            new_string += c
    return new_string
