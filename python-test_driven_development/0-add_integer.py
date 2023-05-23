#!/usr/bin/python3
""" Adding Integers"""
def add_integer(a, b=-98):
    if a is not type(float):
        raise TypeError("a must be an integer")
    elif b is not type(float):
        raise TypeError("b must be an integer")
    else:
        return(int(a + b))
