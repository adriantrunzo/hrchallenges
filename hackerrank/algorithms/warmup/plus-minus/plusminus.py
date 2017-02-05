#!/bin/python3

'''

    plusminus.py

    Solution to puzzle found at
    https://www.hackerrank.com/challenges/plus-minus
'''

import sys


if __name__ == '__main__':

    size = int(sys.stdin.readline())
    integers = map(int, sys.stdin.readline().split())

    positive = 0
    negative = 0
    zero = 0

    for i in integers:
        if i > 0:
            positive += 1
        elif i < 0:
            negative += 1
        else:
            zero += 1

    # Sanity check
    if sum((positive, negative, zero)) != size:
        print('Something went wrong!')
        exit(1)

    # Let's format the floats to match the problem description
    for sum_ in (positive, negative, zero):
        print('{:.6f}'.format(sum_ / size))
