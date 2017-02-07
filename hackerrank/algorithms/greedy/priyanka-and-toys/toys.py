# -*- coding: utf-8 -*-
'''

    toys.py

    Solution to puzzle found at
    https://www.hackerrank.com/challenges/priyanka-and-toys
'''

import sys


if __name__ == '__main__':
    num_toys = int(sys.stdin.readline())
    weights = sorted(map(int, sys.stdin.readline().split()))

    if len(weights) != num_toys:
        print('Invalid number of weights!.')
        exit(1)

    threshold = weights[0] + 4
    purchased = 1
    for w in weights:
        if w > threshold:
            purchased += 1
            threshold = w + 4

    print(purchased)
