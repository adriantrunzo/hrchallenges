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

        # This is not optimal time-wise, but will save space
        self.children = []

        # Number of of times this Node has been visited in the add function.
        # Thus, how many words used this Node.
        self.used = 0

    def get_child(self, ch):
        for child in self.children:
            if child.data == ch:
                return child


class WordTrie:

    def __init__(self):
        self.root = TrieNode('*')

    def add(self, string):
        current = self.root

        for ch in string:
            child = current.get_child(ch)

            if child is None:
                child = TrieNode(ch)
                current.children.append(child)

            # Either way, this node was used in another word
            child.used += 1
            current = child

    def search(self, query):
        current = self.root

        for ch in query:
            child = current.get_child(ch)

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
