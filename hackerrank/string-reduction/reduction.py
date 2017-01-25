# -*- coding: utf-8 -*-
'''
    reduction.py

    This file contains a solution to the string reduction challenge
    found at Hacker Rank.
'''

import sys


def process_input(src=sys.stdin):
    '''Reads the test cases from the input source. The given source
    should be a file-like object, sys.stdin is the default.'''

    strings = []
    num_strings = int(src.readline().strip())

    for i in xrange(num_strings):
        strings.append(src.readline().strip())

    return strings


def test_input():
    '''Generates some random test data with size bounds.'''

    import random

    tests = []
    for i in xrange(100):
        tests.append(''.join([chr(random.randint(97, 99))
                              for _ in range(100)]))

    return tests


def minimal_reduction(s):
    '''Returns the length of the minimum reduction based on
    the counts of each character.'''

    counts = [s.count(chr_) for chr_ in 'abc']

    # If two characters don't appear, can't reduce
    if len(filter(lambda a: a != 0, counts)) == 1:
        return len(s)

    # If all counts are even or odd, can reduce to 2
    num_odd = sum(map(lambda a: a % 2, counts))
    if num_odd == len(counts) or num_odd == 0:
        return 2

    return 1


def print_reductions(strings):
    '''Prints the length of the reductions of the given strings.'''

    for i in xrange(len(strings)):
        print minimal_reduction(strings[i]),

        if i < len(strings) - 1:
            print


if __name__ == '__main__':
    #tests = test_input()
    tests = process_input()
    print_reductions(tests)
