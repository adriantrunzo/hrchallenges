# -*- coding: utf-8 -*-
'''

    permutation.py

    Solution to puzzle found at
    https://www.hackerrank.com/challenges/largest-permutation
'''

import heapq
import sys


if __name__ == '__main__':
    n, k = map(int, sys.stdin.readline().split())
    permutation = map(int, sys.stdin.readline().split())

    # If we can perform at least n - 1 swaps, just return the sorted list.
    if k >= (n - 1):
        print(*sorted(permutation, reverse=True), end='')
    else:
        table = {}
        permutation = list(permutation)
        for i in range(len(permutation)):
            table[permutation[i]] = i

        j = 0  # Counting backwards from n, so n-j each iteration.
        swaps = 0  # How many swaps have we performed?
        while swaps < k:
            temp_value = permutation[j]

            # Don't swap if the number is already in the correct spot.
            if temp_value != n-j:
                permutation[j] = n-j
                permutation[table[n-j]] = temp_value

                temp_index = table[n-j]
                table[n-j] = 0
                table[temp_value] = temp_index
                
                swaps += 1

            j += 1;

        print(*permutation, end='')
