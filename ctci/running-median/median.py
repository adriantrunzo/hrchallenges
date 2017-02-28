#!/bin/python3

'''

    median.py

    Solution to puzzle found at
    https://www.hackerrank.com/challenges/ctci-find-the-running-median
'''

import abc
import sys


class IllegalStateError(Exception):

    def __init__(self, message):
        self.message = message


class Heap(metaclass=abc.ABCMeta):
    '''Generic representation of a heap.'''

    def __init__(self):
        self.heap = []
        self.size = 0

    def get_left_child_index(self, pindex):
        return 2 * pindex + 1

    def get_right_child_index(self, pindex):
        return 2 * pindex + 2

    def get_parent_index(self, cindex):
        return (cindex - 1) // 2

    def has_left_child(self, pindex):
        return self.get_left_child_index(pindex) < self.size

    def has_right_child(self, pindex):
        return self.get_right_child_index(pindex) < self.size

    def has_parent(self, cindex):
        return self.get_parent_index(cindex) >= 0

    def get_left_child(self, pindex):
        return self.heap[self.get_left_child_index(pindex)]

    def get_right_child(self, pindex):
        return self.heap[self.get_right_child_index(pindex)]

    def get_parent(self, cindex):
        return self.heap[self.get_parent_index(cindex)]

    def swap(self, ia, ib):
        self.heap[ia], self.heap[ib] = self.heap[ib], self.heap[ia]

    def peek(self):
        if self.size > 0:
            return self.heap[0]
        else:
            raise IllegalStateError('Nothing to peek at!')

    def poll(self):
        if self.size > 0:
            item = self.heap[0]
            self.heap[0] = self.heap[self.size - 1]
            self.size -= 1
            self.heapify_down()
            return item
        else:
            raise IllegalStateError('Nothing to poll!')

    def add(self, item):
        self.heap.insert(self.size, item)
        self.size += 1

        self.heapify_up()

    @abc.abstractmethod
    def heapify_down(self):
        pass

    @abc.abstractmethod
    def heapify_up(self):
        pass

class MaxHeap(Heap):
    '''Implementation of a max-heap.'''

    def heapify_down(self):
        index = 0

        while self.has_left_child(index):
            larger_child_index = self.get_left_child_index(index)

            if (self.has_right_child(index) and
                self.get_right_child(index) > self.get_left_child(index)):

                larger_child_index = self.get_right_child_index(index)

            if self.heap[index] < self.heap[larger_child_index]:
                self.swap(index, larger_child_index)
            else:
                break

            index = larger_child_index

    def heapify_up(self):
        index = self.size - 1

        while (self.has_parent(index) and
               self.get_parent(index) < self.heap[index]):

            pindex = self.get_parent_index(index)
            self.swap(pindex, index)
            index = pindex


class MinHeap(Heap):
    '''Implementation of a min-heap.'''

    def heapify_down(self):
        index = 0

        while self.has_left_child(index):
            smaller_child_index = self.get_left_child_index(index)

            if (self.has_right_child(index) and
                self.get_right_child(index) < self.get_left_child(index)):

                smaller_child_index = self.get_right_child_index(index)

            if self.heap[index] > self.heap[smaller_child_index]:
                self.swap(index, smaller_child_index)
            else:
                break

            index = smaller_child_index

    def heapify_up(self):
        index = self.size - 1

        while (self.has_parent(index) and
               self.get_parent(index) > self.heap[index]):

            pindex = self.get_parent_index(index)
            self.swap(pindex, index)
            index = pindex


class MedianHeaper:
    '''This class wraps two heaps, a min heap and a max heap. The min heap
    will represent all values greater than the median and the max heap will
    represent all values less than the median. Thus, we can just look at the
    root element of each heap to determine the median in constant time.'''

    def __init__(self):
        self.lt_median = MaxHeap()
        self.gt_median = MinHeap()

    def get_median(self):

        # There is an even number of integers
        if self.lt_median.size == self.gt_median.size:
            try:
                return (self.lt_median.peek() + self.gt_median.peek()) / 2
            except IllegalStateError:
                return 0

        # There is an odd number of integers
        elif self.lt_median.size > self.gt_median.size:
            return self.lt_median.peek()
        else:
            return self.gt_median.peek()

    def add(self, item):
        '''Add the item into the appropriate heap based on comparing the value
        to the current median. If one heap ends up with two more elements,
        move the top to the other heap.'''

        median = self.get_median()

        if item > median:
            self.gt_median.add(item)

            if (self.gt_median.size - self.lt_median.size) > 1:
                self.lt_median.add(self.gt_median.poll())
        else:
            self.lt_median.add(item)

            if (self.lt_median.size - self.gt_median.size) > 1:
                self.gt_median.add(self.lt_median.poll())


if __name__ == '__main__':

    # n is number of integers
    n = int(sys.stdin.readline())

    medianizer = MedianHeaper()

    for i in range(n):
        medianizer.add(int(sys.stdin.readline()))
        print('{:.1f}'.format(medianizer.get_median()))
