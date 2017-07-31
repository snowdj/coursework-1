"""
Time: O(lg(n)), or O(sqrt(n)), or O(1)
Space: O(1)

Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Returns: True
Example 2:

Input: 14
Returns: False
"""


# O(lg(n))
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        x = num
        while x * x > num:
            x /= 2
        for m in range(x, x*2):
            if m * m == num:
                return True
        return False


# O(lg(n))
class Solution2(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        x = num
        while x * x > num:
            x = (x + num/x)//2  # Newton iteration
        return x * x == num


# O(sqrt(n))
# 1 + 3 + 5 + (2m-1) = (1 + 2m -1) * m /2 = m*m
class Solution3(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i = 1
        while num > 0:
            num -= i
            i += 2
        return num == 0


# O(1)
# https://discuss.leetcode.com/topic/49339/o-1-time-c-solution-inspired-by-q_rsqrt
# wiki: Fast inverse square root
