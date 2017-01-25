# -*- coding: utf-8 -*-
'''

    grid.py

    Solution to puzzle found at
    https://www.hackerrank.com/challenges/grid-challenge
'''

import sys


def process_grid(grid_size, src=sys.stdin):
    '''Process one test case with the specified grid size. We only need to
    compare two rows at a time -- as soon as two rows don't order on the
    columns lexicographically, we can't stop. Instead of reading all of the
    grid into memory, just read one line at a time. Return YES or NO.'''

    top = []
    bottom = sorted(list(src.readline().strip()))

    for i in range(1, grid_size):
        top = bottom
        bottom = sorted(list(src.readline().strip()))

        comparison = sum(map(int,
                             [bottom[j] >= top[j] for j in range(grid_size)]))

        if comparison != grid_size:
            # Be sure to read remaining lines.
            for k in range(grid_size - (i + 1)):
                src.readline()
            return 'NO'

    return 'YES'

if __name__ == '__main__':
    num_tests = int(sys.stdin.readline())

    for t in range(num_tests):
        print(process_grid(int(sys.stdin.readline())))
