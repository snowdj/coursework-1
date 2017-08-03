"""
Time: O(lg(dividend/divisor))
Space: O(1)

Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
"""


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        m, n = abs(dividend), abs(divisor)
        if m < n:
            return 0

        res = 0
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        while m >= n:
            t = n; p = 1
            while m > (t << 1):
                t <<= 1; p <<= 1  # fast increase t by 2^n
            m -= t; res += p
        res *= sign
        return 2**31-1 if res > 2**31-1 else res
