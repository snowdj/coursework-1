"""
Time: O(n)
Space: O(1)

You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
"""


# Same as Fibonacci with DP
# Bottom-up
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        c0, c1 = 1, 1
        for _ in range(2, n+1):
            c1, c0 = c0 + c1, c1
        return c1
