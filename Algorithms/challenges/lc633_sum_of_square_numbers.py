"""
Time: O(sqrt(c)*lg(c))
Space: O(1)


Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:
Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
Example 2:
Input: 3
Output: False
"""


# binary search. Don't know why time limit exceeded.
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        i = 0
        while i * i <= c:
            n = c - i * i
            a, b = 0, n
            while a <= b:
                mid = (a+b) // 2
                midsqr = mid * mid
                if midsqr == n:
                    return True
                elif midsqr < n:
                    a = mid + 1
                else:
                    b = mid - 1
            i += 1
        return False


# Fermat theorem: Any positive number n is expressible as a sum of two squares
# if and only if the prime factorization of n, every prime of the form (4k+3)
# occurs an even number of times.
class Solution2(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        i = 2
        while i * i <= c:
            count = 0
            if c % i == 0:  # i is a factor of c
                while c % i == 0:
                    count += 1
                    c //= i
                if i % 4 == 3 and count % 2 != 0:
                    return False
            i += 1
        return c % 4 != 3
