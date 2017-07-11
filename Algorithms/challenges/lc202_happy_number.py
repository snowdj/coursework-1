"""
Solution 1:
Time: O(K)  K: # of loops to reach 1 or itself.
Space: O(K)

Solution 2:
Time: O(K)  K: # of loops to reach 1 or 4.
Space: O(1)

Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any
positive integer, replace the number by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay), or it
loops endlessly in a cycle which does not include 1. Those numbers for which
this process ends in 1 are happy numbers.

Example: 19 is a happy number

12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""


def num2dig(n):
    while n:
        d = n % 10
        n //= 10
        yield d


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = set()
        while n != 1:
            n = sum(d**2 for d in num2dig(n))
            if n in s:
                return False
            else:
                s.add(n)
        return True


# Math proof: any unhappy number must loop over 4.
class Solution2(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n != 1 and n != 4:
            n = sum(d**2 for d in num2dig(n))
        return n == 1
