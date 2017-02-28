#!/bin/python3

'''

    rotation.py

    Solution to puzzle found at
    https://www.hackerrank.com/challenges/circular-array-rotation
'''

import sys


if __name__ == '__main__':

    # n = length of array
    # k = number of right circular rotations
    # q = number of queries
    n, k, q = map(int, sys.stdin.readline().split())
    elements = [int(e) for e in sys.stdin.readline().split()]

    if len(elements) != n:
        print('Invalid number of elements received!')
        exit(1)

    # An array of n rotated n times is exactly the same
    k = k % n

    for i in range(q):
        query = int(sys.stdin.readline())
        print(elements[query - k])
