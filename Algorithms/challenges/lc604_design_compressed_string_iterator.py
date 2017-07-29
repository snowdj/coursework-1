"""
Time:
Space:

Design and implement a data structure for a compressed string iterator. It
should support the following operations: next and hasNext.

The given compressed string will be in the form of each letter followed by a
positive integer representing the number of this letter existing in the
original uncompressed string.

next() - if the original string still has uncompressed characters, return the
next letter; Otherwise return a white space.  hasNext() - Judge whether there
is any letter needs to be uncompressed.

Note: Please remember to RESET your class variables declared in StringIterator,
as static/class variables are persisted across multiple test cases. Please see
here for more details.

Example:

StringIterator iterator = new StringIterator("L1e2t1C1o1d1e1");

iterator.next(); // return 'L'
iterator.next(); // return 'e'
iterator.next(); // return 'e'
iterator.next(); // return 't'
iterator.next(); // return 'C'
iterator.next(); // return 'o'
iterator.next(); // return 'd'
iterator.hasNext(); // return true
iterator.next(); // return 'e'
iterator.hasNext(); // return false
iterator.next(); // return ' '
"""


class StringIterator(object):
    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self._s = compressedString
        self._n = len(compressedString)
        self._i = self._cnt = 0
        self._c = ' '

    def next(self):
        """
        :rtype: str
        """
        if self.hasNext():
            self.check_count()
            self._cnt -= 1
            return self._c
        return ' '

    def hasNext(self):
        """
        :rtype: bool
        """
        return self._i < self._n

    def check_count(self):
        if self._cnt == 0:
            self._c = self._s[self._i]
            self._i += 1
            while self._i < self._n and ord('0') <= ord(self._s[self._i]) <= ord('9'):
                self._cnt = self._cnt * 10 + int(self._s[self._i])
                self._i += 1


# https://discuss.leetcode.com/topic/92159/short-solution-of-c-using-stringstream-python-using-re/2
import re


class StringIterator2(object):

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.__data = re.findall(r"([a-zA-Z])(\d+)", compressedString)
        self.__index, self.__count = -1, 0

    def next(self):
        """
        :rtype: str
        """
        if self.hasNext():
            self.__count -= 1
            return self.__data[self.__index][0]
        else:
            return ' '

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.__count == 0 and self.__index + 1 < len(self.__data):
            self.__index += 1
            self.__count = int(self.__data[self.__index][1])
        return self.__count > 0
