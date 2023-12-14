#!/usr/bin/python3
"""
Find minimum operations,copy n paste, to rep character given times
Return 0 if 'n' is impossible to achieve
"""


def minOperations(n):
    """check and replicate a character a given number of times"""
    if n == 1:
        """No operations needed, character already there"""
        return 0

    # Start with one character already in the file
    operations = 0
    clipboard = 0
    numberOf_H = 1

    while numberOf_H < n:
        """If 'n' multiple of current 'H', copy all and paste repeatedly"""
        if n % numberOf_H == 0:
            clipboard = numberOf_H
            operations += 1
        numberOf_H += clipboard  # Paste the content of the clipboard
        operations += 1

    return operations if numberOf_H == n else 0
