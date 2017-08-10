"""
Time: O(lg(n))
Space: O(1)

Implement pow(x, n).
"""


# recursive
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if not n:
            return 1
        if n < 0:
            return 1/self.myPow(x, -n)
        if n % 2:
            return x * self.myPow(x, n-1)
        return self.myPow(x*x, n//2)


# iterative
class Solution2(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n != 0:
            if n & 1:
                pow *= x  # operates this at the beginning if n is odd, and also when n == 1 no matter n is odd/even.
            x *= x
            n >>= 1
        return pow
