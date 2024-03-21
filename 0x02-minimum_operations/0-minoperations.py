#!/usr/bin/python3
"""This module defines the function minOperations"""


def minOperations(n):
    """This function takes as argument
        n: number of H characters that should be printed
        and returns the number of operations to achieve that"""
    if (not isinstance(n, int) or n <= 0):
        return 0
    copy = 1
    rep = 1
    op = 0
    while(rep < n):
        if (n % rep == 0):
            copy = rep
            rep *= 2
            op += 2
        else:
            rep += copy
            op += 1
    return op