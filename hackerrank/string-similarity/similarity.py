# -*- coding: utf-8 -*-
"""
    similarity.py

    This file contains a solution to the string similarity challenge
    found at Hacker Rank.
"""

import sys


def process_input(src=sys.stdin):
    """Reads the test cases from the input source. The given source
    should be a file-like object, sys.stdin is the default.
    """

    strings = []
    num_strings = int(src.readline().strip())

    for i in xrange(num_strings):
        strings.append(src.readline().strip())

    return strings


def test_input():
    """Generates some random test data with size bounds."""

    import random

    tests = []
    for i in xrange(10):
        tests.append(''.join([chr(random.randint(97, 122))
                              for _ in range(100000)]))

    return tests


def similarity(s):

    result = 0
    length = len(s)
    chars = list(s)

    for i in xrange(length):
        j = 0
        while j < length - i and i + j < length:
            if chars[i + j] != chars[j]:
                break
            j += 1
        result += j

    return result


def print_similarities(strings):

    for i in xrange(len(strings)):
        print similarity(strings[i]),

        if i < len(strings) - 1:
            print


if __name__ == '__main__':
    #tests = test_input()
    tests = process_input()
    print_similarities(tests)
