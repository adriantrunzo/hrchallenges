# -*- coding: utf-8 -*-
'''

    flowers.py

    Solution to puzzle found at
    https://www.hackerrank.com/challenges/flowers.py
'''

import sys


def weighted_sum(prices):
    '''Each flower increases in cost based on previous amount purchased.'''

    purchased = 0
    total = 0

    for price in prices:
        total += (purchased + 1) * price
        purchased += 1

    return total


if __name__ == '__main__':
    num_flowers, num_friends = map(int, sys.stdin.readline().split())
    prices = sorted(map(int, sys.stdin.readline().split()), reverse=True)

    if len(prices) != num_flowers:
        print('Invalid number of prices!.')
        exit(1)

    friend = 0
    ascending = True
    purchases = {k: [] for k in range(num_friends)}

    # Distribute the flowers by traversing friends from bottom to top, then
    # top to bottom.
    for p in prices:
        if friend == -1:
            ascending = True
            friend = 0
        elif friend == (num_friends):
            ascending = False
            friend = num_friends - 1

        purchases[friend].append(p)

        if ascending:
            friend += 1
        else:
            friend -= 1

    print(sum(map(weighted_sum, purchases.values())))
