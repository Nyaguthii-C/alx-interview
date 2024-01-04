#!/usr/bin/python3
"""determine if given data set represents a valid UTF-8 encoding"""


def validUTF8(data):
    """convert data to bytes and check if valid utf-8"""
    try:
        bytes(data).decode('utf-8')
        return True
    except (UnicodeDecodeError, ValueError):
        return False
