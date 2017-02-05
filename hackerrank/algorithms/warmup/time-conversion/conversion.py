#!/bin/python3

'''

    conversion.py

    Solution to puzzle found at
    https://www.hackerrank.com/challenges/time-conversion
'''

import sys
import time


if __name__ == '__main__':

    format_12 = '%I:%M:%S%p'
    format_24 = '%H:%M:%S'

    input_time = sys.stdin.readline().strip()

    print(time.strftime(format_24, time.strptime(input_time, format_12)))
