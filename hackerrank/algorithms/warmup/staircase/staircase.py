#!/bin/python3

'''

    staircase.py

    Solution to puzzle found at
    https://www.hackerrank.com/challenges/staircase
'''

import sys


if __name__ == '__main__':

    size = int(sys.stdin.readline())

    for i in range(1, size + 1):
        print('{: >{length}}'.format('#' * i, length=size))
