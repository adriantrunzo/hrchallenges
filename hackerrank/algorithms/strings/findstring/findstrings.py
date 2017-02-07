# -*- coding: utf-8 -*-
'''
    findstrings.py

    This file contains a solution to the find strings
    puzzle found at HackerRank. Makes use of a suffix array
    structure to quickly find the appropriate substring.
'''

import sys


def process_input(src=sys.stdin):
    '''Reads the strings and queries from the input source. The given source
    should be a file-like object, sys.stdin is the default.'''

    strings = []
    num_strings = int(src.readline().strip())

    for i in xrange(num_strings):
        strings.append(src.readline().strip())

    queries = []
    num_queries = int(src.readline().strip())

    for i in xrange(num_queries):
        queries.append(int(src.readline().strip()))

    return strings, queries


def test_input():
    '''Generates some random test data with size bounds.'''

    import random

    words = []
    for i in xrange(50):
        words.append(''.join([chr(random.randint(97, 122))
                              for _ in range(2000)]))

    queries = []
    for i in range(500):
        queries.append(random.randint(1, 1000000000))

    return words, queries


def count_common(sa, sb):
    '''Counts the length of the common prefix of the given strings.'''

    count = 0

    length = min(len(sa), len(sb))
    for i in xrange(length):
        if sa[i] == sb[i]:
            count += 1
        else:
            break

    return count


def get_all_suffixes(strings):
    '''Returns a list of all of the suffixes of the given list of strings.
    To save memory, each suffix is represented by two integers, one containing
    the array index of the original string and the other the starting index
    of the suffix. The suffixes are sorted by lexicographic order.'''

    suffixes = []
    for i in xrange(len(strings)):
        for j in xrange(len(strings[i])):
            suffixes.append((i, j))

    # Sort by grabbing the actual string for each tuple
    suffixes.sort(key=lambda s: strings[s[0]][s[1]:])

    return suffixes


def create_index(strings, suffixes):
    '''Generates a searchable index for the given list of suffixes. The index
    is a list of tuples, each of which has three items: the number of unique
    substrings contained in the index up to this point (including the current
    entry), the index of the suffix, and the offset for the suffix.'''

    # Initialize index for first suffix
    first_count = len(strings[suffixes[0][0]][suffixes[0][1]:])
    index = [(first_count, 0, 1)]

    for i in xrange(1, len(suffixes)):

        this_string = strings[suffixes[i][0]][suffixes[i][1]:]
        prev_string = strings[suffixes[i - 1][0]][suffixes[i - 1][1]:]

        # Ignore duplicates for indexing
        if this_string == prev_string:
            continue

        in_common = count_common(this_string, prev_string)
        prev_count = index[-1][0]
        this_count = prev_count + len(this_string) - in_common

        index.append((this_count, i, in_common + 1))

    return index


def kth_substring(query, strings, suffixes, index):
    '''Finds the kth substring from the indexed suffixes. Uses a binary
    search to find the right suffix. Returns INVALID if the query is
    bad.'''

    low = 0
    high = len(index) - 1

    while low <= high:
        mid = (low + high) / 2
        if query > index[mid][0]:
            low = mid + 1
        elif mid > 0 and query <= index[mid - 1][0]:
            high = mid - 1
        else:
            prev_count = 0 if mid == 0 else index[mid - 1][0]
            k = query - prev_count - 1
            offset = index[mid][2]
            string =  strings[suffixes[index[mid][1]][0]][suffixes[index[mid][1]][1]:]
            return string[0:offset + k]

    return 'INVALID'


def answer_queries(strings, suffixes, index, queries):
    '''Prints the results of the queries, one per line.'''

    for i in xrange(len(queries)):
        query = queries[i]
        result = kth_substring(query, strings, suffixes, index)
        print result,

        if i < len(queries) - 1:
            print


if __name__ == '__main__':
    strings, queries = process_input()
    #strings, queries = test_input()
    suffixes = get_all_suffixes(strings)
    index = create_index(strings, suffixes)
    answer_queries(strings, suffixes, index, queries)
