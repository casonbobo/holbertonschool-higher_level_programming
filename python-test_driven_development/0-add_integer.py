#!/usr/bin/python3
"""
Adding Integers
"""
def add_integer(a, b=-98):
    """
    a function that adds integers or casts 
    floats to integers and adds them
    """
    if a is None or type(a) not in [int, float] or abs(a) > float('inf'):
        raise TypeError("a must be an integer")
    if b is None or type(b) not in [int, float] or abs(b) > float('inf'):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
