#!/bin/python3

'''

    brackets.py

    Solution to puzzle found at
    https://www.hackerrank.com/challenges/ctci-balanced-brackets
'''

import sys


def is_balanced(string):
    '''Determines whether a string of brackets is balanced.'''

    # Map closing brackets to opening brackets for comparison
    brackets = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    stack = []

    for ch in string:

        # An opening bracket, push to stack
        if ch not in brackets:
            stack.append(ch)
        # Make sure there is a value on the stack and it corresponds
        else:
            try:
                previous = stack.pop()
                if previous != brackets[ch]:
                    return 'NO'
            except IndexError:
                return 'NO'

    if len(stack) == 0:
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':

    # n is number of strings
    n = int(sys.stdin.readline())

    for i in range(n):
        print(is_balanced(sys.stdin.readline().strip()))
