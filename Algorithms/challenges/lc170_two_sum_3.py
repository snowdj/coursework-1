"""
Time:
Space:

Design and implement a TwoSum class. It should support the following operations:add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

For example,
add(1); add(3); add(5);
find(4) -> true
find(7) -> false
"""


import bisect
import collections


# O(n)/O(n)
class TwoSum:
    def __init__(self):  # O(n)
        self._data = []

    def add(self, number):  # O(n)
        bisect.insort(self._data, number)  # insort is O(n) because list moving

    def find(self, value):  # O(n)
        i, j = 0, len(self._data)-1
        while i < j:
            s = self._data[i] + self._data[j]
            if s == value:
                return True
            elif s > value:
                j -= 1
            else:
                i += 1
        return False


# add O(1), find O(n), space O(n)
class TwoSum2:
    def __init__(self):  # O(n)
        self.ctr = collections.defaultdict(int)  # defaultdict is faster than Counter.

    def add(self, number):  # O(1)
        self.ctr[number] += 1

    def find(self, value):  # O(n)
        ctr = self.ctr
        return any(value - num in ctr and (value - num != num or ctr[num] > 1)
                   for num in ctr)


# Stefan claims this is faster than defaultdict, by a constant scale maybe.
class TwoSum3:
    def __init__(self):
        self.ctr = {}  # plain dict is faster than defaultdict.

    def add(self, number):
        if number in self.ctr:
            self.ctr[number] += 1
        else:
            self.ctr[number] = 1

    def find(self, value):
        ctr = self.ctr  # make faster without looking up attributes
        for num in ctr:
            if value - num in ctr and (value - num != num or ctr[num] > 1):
                return True
        return False
