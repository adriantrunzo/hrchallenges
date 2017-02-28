# -*- coding: utf-8 -*-
'''

    max-min.py

    Solution to puzzle found at
    https://www.hackerrank.com/challenges/angry-children.py
'''

import sys


if __name__ == '__main__':
    n = int(sys.stdin.readline())
    k = int(sys.stdin.readline())

    numbers = []
    for i in range(n):
        numbers.append(int(sys.stdin.readline()))
    numbers = sorted(numbers)

    # Define a sliding window size k and start with largest difference
    difference = numbers[n - 1] - numbers[0]
    left = 0
    right = k - 1

    while right <= (n - 1):
        local_difference = numbers[right] - numbers[left]
        if local_difference < difference:
            difference = local_difference

        left += 1
        right += 1

    print(difference)
