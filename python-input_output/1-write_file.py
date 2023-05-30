#!/usr/bin/python3
"""this is a file to write other files"""


def write_file(filename="", text=""):
    """this is a function to write a file"""
    with open(filename, mode='w', encoding="utf-8") as f:
        return (f.write(text)) 
