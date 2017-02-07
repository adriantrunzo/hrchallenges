#!/bin/python3

'''

    anagrams.py

    Solution to puzzle found at
    https://www.hackerrank.com/challenges/ctci-making-anagrams
'''

import sys


def get_frequency_table(string):
    '''Return a dictionary representing the frequency of each character in
    the given string.'''

    table = {}

    for ch in string:
        table[ch] = table.setdefault(ch, 0) + 1

    return table


if __name__ == '__main__':

    string_a = sys.stdin.readline().strip()
    string_b = sys.stdin.readline().strip()

    table_a = get_frequency_table(string_a)
    table_b = get_frequency_table(string_b)

    deletions = 0
    allch = set.union(set(), table_a.keys(), table_b.keys())

    # If a character is only in a or b, just add it's number of occurences
    # to the number of deletions. Otherwise, add the absolute value of the
    # frequency difference.
    for ch in allch:
        if ch in table_a and ch in table_b:
            deletions += abs(table_a[ch] - table_b[ch])
        elif ch in table_a:
            deletions += table_a[ch]
        else:
            deletions += table_b[ch]

    print(deletions)
