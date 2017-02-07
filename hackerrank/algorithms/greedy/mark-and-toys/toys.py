# -*- coding: utf-8 -*-
'''

    toys.py

    Solution to puzzle found at
    https://www.hackerrank.com/challenges/mark-and-toys
'''

import sys


if __name__ == '__main__':
    num_toys, funds = map(int, sys.stdin.readline().split())
    prices = sorted(map(int, sys.stdin.readline().split()))

    if len(prices) != num_toys:
        print('Invalid number of prices read!')
        exit(1)

    spent = 0
    toys_bought = 0
    for price in prices:
        if (price + spent) <= funds:
            spent += price
            toys_bought += 1
        else:
            break

    print(toys_bought)
