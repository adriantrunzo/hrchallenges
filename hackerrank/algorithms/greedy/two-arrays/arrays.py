# -*- coding: utf-8 -*-
'''

    arrays.py

    Solution to puzzle found at
    https://www.hackerrank.com/challenges/two-arrays
'''

import sys


def process_arrays(length, k, src=sys.stdin):
    '''Determine if reverse-sorted permutations of two arrays of length
    satisfy A[i] + B[i] >= k for i 0...length-1.'''

    arr_a = sorted(map(int, src.readline().split()))
    arr_b = sorted(map(int, src.readline().split()), reverse=True)

    comparison = sum(map(int,
                         [arr_a[i] + arr_b[i] >= k for i in range(length)]))

    if comparison == length:
        return 'YES'

    return 'NO'

if __name__ == '__main__':
    num_tests = int(sys.stdin.readline())

    for t in range(num_tests):
        print(process_arrays(*list(map(int, sys.stdin.readline().split()))))
