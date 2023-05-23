#!/usr/bin/python3
"""
Adding Integers
"""
def add_integer(a, b=-98):
    """
    a function that adds integers or casts 
    floats to integers and adds them
    """
    if a is not type(float):
        raise TypeError("a must be an integer")
    elif b is not type(float):
        raise TypeError("b must be an integer")
    else:
        return(int(a + b))
