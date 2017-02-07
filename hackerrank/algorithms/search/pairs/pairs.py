# -*- coding: utf-8 -*-
'''
    pairs.py

    This file contains a solution to the pairs challenge found at HackerRank.
'''

import sys


def pairs(integers, k):
    '''Counts the total pairs of integers that have a difference of k.'''

    subtracted = set(map(lambda a: a - k, integers))

    return len(integers & subtracted)


def process_input(src=sys.stdin):
    '''Reads in n, k, and the integers from the input source. The source
    should be a file-like object, sys.stdin is the default.'''

    n, k = (int(i) for i in src.readline().strip().split())
    integers = {int(j) for j in src.readline().strip().split()}

    return integers, k


def test_input():
    '''Generates some random test data with size bounds.'''

    import random

    n = 10 ** 5
    k = random.randint(0, 10 ** 9)
    integers = set()

    for i in range(n):
        integers.add(random.randint(0, 10 ** 9))

    print 'k:', k
    print 'n:', len(integers)

    return integers, k


if __name__ == '__main__':
    integers, k = process_input()
    #integers, k = test_input()
    print pairs(integers, k),
