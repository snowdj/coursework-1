"""
Time: O(sqrt(n))
Space: O(1)

We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.
Example:
Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14
Note: The input number n will not exceed 100,000,000. (1e8)
"""


# brute force
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return False
        s, i = 1, 2
        while i * i <= num:  # loop from 2 to sqrt(num)
            if (num % i) == 0:
                s += i + num // i
            if i * i == num:
                s -= i
            if s > num:
                return False
            i += 1
        return s == num


# Euclid-Euler Theorem
class Solution2(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        primes = [2, 3, 5, 7, 13, 17, 19, 31]
        for p in primes:
            if num == (1 << (p - 1)) * ((1 << p) - 1):
                return True
        return False


# shame...
class Solution3(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num == 6 or num == 28 or num == 496 or num == 8128 or num == 33550336
