"""
Time: O(1)
Space: O(1)

Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).

For example, the 32-bit integer ’11' has binary representation 00000000000000000000000000001011, so the function should return 3.
"""


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = 0
        while n > 0:
            s += n & 1
            n >>= 1
        return s


class Solution2(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = 0
        while n > 0:
            s += 1
            n &= n-1
        return s
