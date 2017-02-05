#!/bin/python3

'''

    triplets.py

    Solution to puzzle found at
    https://www.hackerrank.com/challenges/compare-the-triplets
'''

import sys


if __name__ == '__main__':

    triplet_a = map(int, sys.stdin.readline().split())
    triplet_b = map(int ,sys.stdin.readline().split())

    score_a = 0
    score_b = 0

    for a,b in zip(triplet_a, triplet_b):
        if a > b:
            score_a += 1
        elif b > a:
            score_b += 1

    print(score_a, score_b, sep=' ')
