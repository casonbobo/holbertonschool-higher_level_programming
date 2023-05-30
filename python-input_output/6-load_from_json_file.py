#!/usr/bin/python3
"""this is a file to write other json"""
import json


def load_from_json_file(filename):
    """this is a function to append to a json"""
    with open(filename, mode='r', encoding="utf-8") as f:
        return json.load(f)
