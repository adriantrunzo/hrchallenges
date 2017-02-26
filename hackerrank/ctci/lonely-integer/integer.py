#!/bin/python3

'''

    integer.py

    Solution to puzzle found at
    https://www.hackerrank.com/challenges/ctci-lonely-integer
'''

import sys


def find_unique(array):
    '''Find the unique integer by xoring all. All non-unique bits are
    effectively zeroed out.'''
    unique = 0

    for a in array:
        unique ^= a

    return unique


if __name__ == '__main__':

    # n is number of integers
    n = int(sys.stdin.readline())
    array = [int(a) for a in sys.stdin.readline().split()]

    print(find_unique(array))
