# -*- coding: utf-8 -*-
'''

    burger.py

    Solution to puzzle found at
    https://www.hackerrank.com/challenges/jim-and-the-orders
'''

import heapq
import sys


def process_orders(num_orders, src=sys.stdin):
    '''Process num_orders from the input source and sort them by completion
    time. Return a min-heap with all of the orders in tuples of the form:
    (completion_time, order_number).'''

    orders = []

    for i in range(1, num_orders + 1):
        finish_time = sum(map(int, src.readline().split()))
        heapq.heappush(orders, (finish_time, i))

    return orders

if __name__ == '__main__':
    orders = process_orders(int(sys.stdin.readline()))
    print(' '.join([str(heapq.heappop(orders)[1])
                    for i in range(len(orders))]))
