#!/bin/python3

'''

    difference.py

    Solution to puzzle found at
    https://www.hackerrank.com/challenges/diagonal-difference
'''

import sys


if __name__ == '__main__':

    # Read N, the size of the N x N matrix
    size = int(sys.stdin.readline())

    primary = 0
    secondary = 0

    for i in range(size):
        row = [int(e) for e in sys.stdin.readline().split()]

        primary += row[i]
        secondary += row[size - i - 1]

    print(abs(primary - secondary))
