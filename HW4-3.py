#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This is my attempt at coding the last question of the last homework assignment
for my algorithms class at Portland State University.
"""

__author__ = 'Mike Lane (http://www.github.com/mikelane/'
__copyright__ = 'Copyright (c) 2015 Mike Lane'
__license__ = 'GPLv3'

import heapq
import random

class Widget:
    def __init__(self, X, Y, Z):
        self.ww = (X, Y, Z)
        self.m = {}
        self.conglomerations = {'A' : (1, 0, 0),
                                'B' : (0, 1, 0),
                                'C' : (0, 0, 1),
                                'D' : (3, 3, 1),
                                'E' : (0, 2, 5),
                                'F' : (6, 0, 2),
                                'G' : (2, 6, 1),
                                'H' : (0, 1, 2)}

    def get_min(self, allowWaste=False):
        return self._get_min(self.ww, allowWaste)

    def _get_min(self, leftover, allowWaste=False):
        done = True
        cHeap = []
        # Determine if any element in the leftover is still remaining.
        for element in leftover:
            if element > 0:
                done = False
                continue

        # If nothing still remains to be subtracted, return the tuple.
        if done:
            return []

        # Base case is handled, now it's time to make the recursive calls
        for key, value in self.conglomerations.items():
            conglomeratesList = [key]
            makeRecursiveCall = True
            # subtract out the amount of each conglomeration from the leftover
            # If allowWaste is False, then don't recurse if any are negative.
            c = tuple(x-y for x, y in zip(leftover, value))
            if not allowWaste:
                for i in c:
                    if i < 0:
                        makeRecursiveCall = False
            else: # this doesn't work. If some recursive call never takes
                  # only ever goes negative, this doesn't make it stop.
                c = list(c)
                d = [x if x >= 0 else 0 for x in c]
                c = tuple(d)

            # If we haven't reached the base case...
            if makeRecursiveCall:
                if c in self.m: # Check to see if we already know the answer
                    conglomeratesList += self.m[c] # if so concatenate it
                else: # Otherwise, determine the answer and concatenate it
                    conglomeratesList += self._get_min(c, allowWaste)
                # Push the concatenated list on the heap sorted by length of the list
                heapq.heappush(cHeap, (len(conglomeratesList), conglomeratesList))

        # Now that we've made all the recursive calls that we're going to make,
        # pop the smallest from the heap, extract the list, and return it
        smallest = heapq.heappop(cHeap)
        # Find the list
        for data in smallest:
            if type(data) is list:
                smallest = data
        # hash the smallest using the passed in tuple as the key
        self.m[leftover] = smallest
        return smallest # return the smallest to the caller

# Testing and pretty print. Make 10 random conglomerations, get the min and print the
# min values out to the screen.
for i in range(10):
    X = random.randrange(20)
    Y = random.randrange(20)
    Z = random.randrange(20)
    print("X: {}, Y: {}, Z: {}".format(X, Y, Z))
    widget = Widget(X, Y, Z)
    min = widget.get_min()
    result = {'A' : min.count('A'),
              'B' : min.count('B'),
              'C' : min.count('C'),
              'D' : min.count('D'),
              'E' : min.count('E'),
              'F' : min.count('F'),
              'G' : min.count('G'),
              'H' : min.count('H'),
              'len' : len(min)}
    print("len: {}".format(result['len']), end=": [")
    for key, value in result.items():
        if value != 0 and key != 'len':
            print("{}: {}".format(key, value), end=" ")
    print("]\n")