#!/usr/bin/python3
"""this is a file to append other files"""


def write_file(filename="", text=""):
    """this is a function to append a file"""
    with open(filename, mode='a', encoding="utf-8") as f:
        return (f.write(text))
