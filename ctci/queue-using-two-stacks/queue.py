#!/bin/python3

'''

    queue.py

    Solution to puzzle found at
    https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks
'''

import sys


class MyQueue(object):

    def __init__(self):
        self.enqueue = []
        self.dequeue = []

    def fill_dequeue_if_necessary(self):
        if not self.dequeue:
            while self.enqueue:
                self.dequeue.append(self.enqueue.pop())

    def peek(self):
        self.fill_dequeue_if_necessary()

        return self.dequeue[-1]

    def pop(self):
        self.fill_dequeue_if_necessary()

        return self.dequeue.pop()

    def put(self, value):
        self.enqueue.append(value)


if __name__ == '__main__':

    # q is number of queries
    q = int(sys.stdin.readline())

    queue = MyQueue()

    for query in range(q):
        values = [int(v) for v in sys.stdin.readline().split()]
        if values[0] == 1:
            queue.put(values[1])
        elif values[0] == 2:
            queue.pop()
        else:
            print(queue.peek())
