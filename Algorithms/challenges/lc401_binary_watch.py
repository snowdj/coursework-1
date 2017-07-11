"""
Time: O(1)
Space: O(1)

A binary watch has 4 LEDs on the top which represent the hours (0-11), and the
6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.


For example, the above binary watch reads "3:25".

Given a non-negative integer n which represents the number of LEDs that are
currently on, return all possible times the watch could represent.

Example:

Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
Note:
1. The order of output does not matter.
2. The hour must not contain a leading zero, for example "01:00" is not valid,
it should be "1:00".
3. The minute must be consist of two digits and may contain a leading zero, for
example "10:2" is not valid, it should be "10:02".
"""


import itertools


class MySolution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        h = [2**i for i in range(4)]
        m = [2**i for i in range(6)]
        res = []
        for n_h in range(max(0, num-6), min(4+1, num+1)):
                n_m = num - n_h
                hours = [sum(t) for t in itertools.combinations(h, n_h)
                         if sum(t) < 12]
                mins = [sum(t) for t in itertools.combinations(m, n_m)
                        if sum(t) < 60]
                res += ['{0}:{1:02d}'.format(th, tm)
                        for th in hours for tm in mins]
        return res


class BestSolution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        return ['%d:%02d' % (h, m)
                for h in range(12) for m in range(60)
                if (bin(h) + bin(m)).count('1') == num]
