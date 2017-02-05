#!/bin/python3

'''

    sum.py

    Solution to puzzle found at
    https://www.hackerrank.com/challenges/simple-array-sum
'''

import sys


if __name__ == '__main__':

    # For python we really don't need the first line of input
    size = int(sys.stdin.readline())
    elements = [int(e) for e in sys.stdin.readline().split()]

    print(sum(elements))
