"""
Time: O(lg(x))
Space: O(1)

Implement int sqrt(int x).

Compute and return the square root of x.
"""


class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        t = x
        while t * t > x:
            t //= 2
        lo, hi = t, t * 2 + 1
        while lo < hi:
            mid = (lo + hi) // 2
            if mid**2 <= x and x < (mid+1)**2:
                return mid
            elif x > mid**2:
                lo = mid + 1
            else:
                hi = mid


# Same as above using bisect, but time limit exceeded.
class Solution2(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        t = x
        while t * t > x:
            t //= 2
        lo, hi = t, t * 2 + 1
        tsqr = [i**2 for i in range(lo, hi+1)]
        return lo + bisect.bisect(tsqr, x) - 1


# Newton iteration
class Solution3(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        pre, xi = 0, 1
        while pre != xi:
            pre = xi
            xi = (xi + float(x)/xi) / 2
        return int(xi)


# Integer Newton Iteration
class Solution4(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = x
        while r * r > x:
            r = (r + x // r) // 2
        return r
