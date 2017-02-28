#!/bin/python3

'''

    bubble.py

    Solution to puzzle found at
    https://www.hackerrank.com/challenges/ctci-bubble-sort
'''

import sys


def bubble_sort(a):
    '''Copy of bubble sort algorithm from java problem desctiption.'''

    # Record all swaps
    total_swaps = 0

    for i in range(len(a)):
        # Track number of elements swapped during a single array traversal
        number_of_swaps = 0

        for j in range(len(a) - 1):
            # Swap adjacent elements if they are in decreasing order
            if (a[j] > a[j + 1]):
                a[j], a[j + 1] = a[j + 1], a[j]
                number_of_swaps += 1

        total_swaps += number_of_swaps

        # If no elements were swapped during a traversal, array is sorted
        if number_of_swaps == 0:
            break

    return total_swaps


if __name__ == '__main__':

    # n is number of array elements
    n = int(sys.stdin.readline())
    array = [int(a) for a in sys.stdin.readline().split()]

    count = bubble_sort(array)
    print('Array is sorted in {} swaps.'.format(count))
    print('First Element: {}'.format(array[0]))
    print('Last Element: {}'.format(array[-1]))
