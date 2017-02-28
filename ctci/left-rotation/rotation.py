#!/bin/python3

'''

    rotation.py

    Solution to puzzle found at
    https://www.hackerrank.com/challenges/ctci-array-left-rotation
'''

import sys


if __name__ == '__main__':

    # n = length of array
    # d = number of left rotations
    n, d = map(int, sys.stdin.readline().split())
    elements = [int(e) for e in sys.stdin.readline().split()]

    if len(elements) != n:
        print('Invalid number of elements received!')
        exit(1)

    # An array of n rotated n times is exactly the same
    d = d % n

    # We don't actually need to create a new array to print the rotated
    # version. Rotating left is the same as starting the printing from an
    # index to the right. We'll just print from that index and then cirle
    # back to the start.

    print(*elements[d:], sep=' ', end=' ')
    print(*elements[:d], sep=' ')
