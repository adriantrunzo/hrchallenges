#!/bin/python3

'''

    sum.py

    Solution to puzzle found at
    https://www.hackerrank.com/challenges/a-very-big-sum
'''

import sys


if __name__ == '__main__':

    # For python we really don't need the first line of input
    size = int(sys.stdin.readline())
    elements = map(int, sys.stdin.readline().split())

    print(sum(elements))
