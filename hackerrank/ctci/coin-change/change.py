#!/bin/python3

'''

    change.py

    Solution to puzzle found at
    https://www.hackerrank.com/challenges/ctci-coin-change
'''

import sys


def make_change(coins, total):
    '''Return the number of ways total can be changed with an ifinite supply
    of the given coins.

    To calculate the number of ways to make change for any value by adding
    one coin to the existing set of coins, we need to add the number of ways
    to make change without the coin and the number of ways to make change
    with the coin. The second part can be expressed as the number of ways to
    make change for (total - coin value), as we'd just be adding the coin.

    Instead of using a two-dimensional array to store the intermediate values,
    we can use a one-dimensional array with index representing value. When we
    add a new coin to the coin set, for each value, the number of ways to make
    change excluding the new coin is the same as the final values for the
    previous set of coins. Thus, we would just be copying values.

    A second shortcut is to realize that the results array will only change for
    values that are greater than or equal to the new coin value.
    '''

    changed = [0 for _ in range(total + 1)]

    # Base case: With an imaginary 0 coin, we can make change for 0 one way.
    changed[0] = 1

    for coin in coins:
        # We only need to update values >= coin
        for i in range(coin, len(changed)):
            changed[i] += changed[i - coin]

    return changed[total]


if __name__ == '__main__':

    # t is total, n is number of coins
    (t, n) = map(int, sys.stdin.readline().split())
    coins = [int(c) for c in sys.stdin.readline().split()]

    print(make_change(coins, t))
