__author__ = 'Mike'

import heapq

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
            if makeRecursiveCall:
                if c in self.m:
                    conglomeratesList += self.m[c]
                else:
                    conglomeratesList += self._get_min(c)
                # Push the concatenated list on the heap sorted by length of the list
                heapq.heappush(cHeap, (len(conglomeratesList), conglomeratesList))

        # Now that we've made all the recursive calls that we're going to make,
        # pop the smallest from the heap, extract the list, and return it
        smallest = heapq.heappop(cHeap)
        for data in smallest:
            if type(data) is list:
                smallest = data
        self.m[leftover] = smallest
        return smallest

test = Widget(6, 1, 2)
min = test.get_min()
print(min)
print("\n")