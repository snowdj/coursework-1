"""
Time: O(1)
Space: O(1)

Given an integer, write a function to determine if it is a power of three.
"""


from math import log10


class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        # has to be base 10, other wise roundoff error when n=243
        # https://discuss.leetcode.com/topic/33536/a-summary-of-all-solutions-new-method-included-at-15-30pm-jan-8th/2
        a = log10(n)/log10(3)
        return (a - int(a)) == 0


class Solution2(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n and n % 3 == 0:
            n /= 3
        return n == 1
