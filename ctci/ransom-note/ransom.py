#!/bin/python3

'''

    ransom.py

    Solution to puzzle found at
    https://www.hackerrank.com/challenges/ctci-ransom-notes
'''

import sys


def get_frequency_table(words):
    '''Return a dictionary representing the frequency of each word in
    the given string.'''

    table = {}

    for w in words:
        table[w] = table.setdefault(w, 0) + 1

    return table


if __name__ == '__main__':

    m, n = [int(i) for i in sys.stdin.readline().split()]
    magazine = sys.stdin.readline().strip()
    note = sys.stdin.readline().strip()

    table_m = get_frequency_table(magazine.split())
    table_n = get_frequency_table(note.split())

    contained = 'Yes'

    for word, count_n in table_n.items():
        count_m = table_m.get(word, 0)
        if count_m < count_n:
            contained = 'No'
            break

    print(contained)
