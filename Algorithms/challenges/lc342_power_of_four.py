"""
Time: O(1)
Space: O(1)

Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?
"""


from math import log


class Answer(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False
        a = log(num, 4)
        return a - int(a) == 0


class Solution1(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        while num and num % 4 == 0:
            num /= 4
        return num == 1


class Solution2(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bo
        """
        return num > 0 and (num & (num - 1)) == 0\
            and (num & 0x55555555) == num  # odd bits positions are 1


class Solution3(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bo
        """
        return num > 0 and (num & (num - 1)) == 0\
            and (num - 1) % 3 == 0
