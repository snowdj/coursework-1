"""
Time: O(n)
Space: O(1)

Determine whether an integer is a palindrome. Do this without extra space.

Some hints:
Could negative integers be palindromes? (ie, -1)

If you are thinking of converting the integer to string, note the restriction of using extra space.

You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?

There is a more generic way of solving this problem.
"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        div = 1
        while x // div >= 10:
            div *= 10
        while x > 0:
            if x // div != x % 10:  # compare most and least significant digits
                return False
            x = (x % div) // 10  # remove most and least significant digits
            div //= 100
        return True


# compare the first half and the last half reversed
class Solution2(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        rev = 0
        while x > rev:  # stop after the middle digit is moved to rev
            rev = rev * 10 + x % 10
            x //= 10
        return x == rev or x == rev // 10  # even or odd number of digits
