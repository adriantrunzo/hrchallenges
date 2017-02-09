#!/bin/python3

'''

    contacts.py

    Solution to puzzle found at
    https://www.hackerrank.com/challenges/ctci-contacts
'''

import sys


class TrieNode:

    def __init__(self, ch):
        self.data = ch

        # Static array of 26 None values, might be less space than a dict
        # in the end. The index corresponds to ord('ch') - 97
        self.children = [None] * 26

        # Number of of times this Node has been visited in the add function.
        # Thus, how many words used this Node.
        self.used = 0


class WordTrie:

    def __init__(self):
        self.root = TrieNode('*')

    def add(self, string):
        current = self.root

        for ch in string:
            code = ord(ch) - 97
            child = current.children[code]

            if child is None:
                child = TrieNode(ch)
                current.children[code] = child

            # Either way, this node was used in another word
            child.used += 1
            current = child

    def search(self, query):
        current = self.root

        for ch in query:
            code = ord(ch) - 97
            child = current.children[code]

            if child is None:
                return 0

            current = child

        # Whatever node we end up at, just print how many words used that node
        return current.used


if __name__ == '__main__':

    # n is number of operations
    n = int(sys.stdin.readline())

    names = WordTrie()

    for i in range(n):
        op, contact = sys.stdin.readline().split()

        if op == 'add':
            names.add(contact)
        else:
            print(names.search(contact))
