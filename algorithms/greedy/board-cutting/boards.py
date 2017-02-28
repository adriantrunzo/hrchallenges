# -*- coding: utf-8 -*-
'''

    boards.py

    Solution to puzzle found at
    https://www.hackerrank.com/challenges/board-cutting.py
'''

import sys


def process_board(m, n, ycosts, xcosts):
    '''Process a board of size MxN with associated costs. Prioritize cuts
    in order of highest cost, with equal costs being cut on the major
    axis (more lines) first. Returns the minimum cost to cut the board.'''

    board = {
        'y': sorted(ycosts),
        'x': sorted(xcosts)
    }

    cuts = {
        'y': 0,
        'x': 0
    }

    total = [0]  # This is a list for scoping in subroutine "cut".
    major = 'y' if m >= n else 'x'
    minor = 'x' if major == 'y' else 'y'

    def cut(axis, other):
        cost = board[axis].pop()
        total[0] += cost * (cuts[other] + 1)
        cuts[axis] += 1

    while board[major] or board[minor]:

        if board[major] and board[minor]:
            if board[major][-1] >= board[minor][-1]:
                cut(major, minor)
            else:
                cut(minor, major)

        elif board[major] and not board[minor]:
            cut(major, minor)

        else:
            cut(minor, major)

    return total[0]


if __name__ == '__main__':
    num_tests = int(sys.stdin.readline())
    modulo = 10**9 + 7

    # M is horizontal corresponding to y_i costs
    for i in range(num_tests):
        m, n = map(int, sys.stdin.readline().split())
        ycosts = map(int, sys.stdin.readline().split())
        xcosts = map(int, sys.stdin.readline().split())

        print(process_board(m, n, ycosts, xcosts) % modulo)
