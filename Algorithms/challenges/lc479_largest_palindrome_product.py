"""
Time: O(10^(2n))
Space: O(n)

Find the largest palindrome made from the product of two n-digit numbers.

Since the result could be very large, you should return the largest palindrome mod 1337.

Example:

Input: 2

Output: 987

Explanation: 99 x 91 = 9009, 9009 % 1337 = 987

Note:

The range of n is [1,8].
"""


# converted from a Java code. Time limit exceeded when n=8. Maybe Python is slow...
# https://discuss.leetcode.com/topic/74125/java-solution-using-assumed-max-palindrom/2
# https://discuss.leetcode.com/topic/74143/java-solution-with-explanation/2
class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if input is 1 then max is 9
        if n == 1:
            return 9

        # if n = 3 then upperBound = 999 and lowerBound = 99
        upper_bound = 10**n - 1
        lower_bound = 10**(n-1) - 1
        max_product = upper_bound * upper_bound

        # represents the first half of the maximum assumed palindrom.
        # e.g. if n = 3 then maxNumber = 999 x 999 = 998001 so firstHalf = 998
        first_half = max_product // 10**n

        while first_half > lower_bound:
            candidate = first_half * 10**n + int(str(first_half)[::-1])
            first_half -= 1
            if candidate > max_product:
                continue
            i = upper_bound
            while i > candidate // i:  # a little optimization
                # here i and palindrom/i form two factors of candidate
                # if candidate // i > upper_bound:
                #    break
                if candidate % i == 0:
                    return candidate % 1337
                i -= 1


# Using the simple fact that a palindrome with an even number of digits is a multiple of 11.
# https://discuss.leetcode.com/topic/75699/time-limit-exceeded-in-python/3
# Still time limit exceeded when n = 7.
class Solution2(object):
    def largestPalindrome(self, n):
        if (n == 1):
            return 9

        uBound = 10**n - 1
        lBound = uBound // 10
        Found = False
        firstHalf = int(uBound * uBound / (10 ** n))

        while not Found:
            secondHalf = int(str(firstHalf)[::-1])
            palindrom = firstHalf*10**n + secondHalf

            if len(str(palindrom)) % 2 == 0:
                for i in range(uBound // 11, (lBound+1) // 11, -1):
                    if (palindrom / (11*i) > uBound):
                        break
                    if ((palindrom % (11*i)) == 0):
                        Found = True
                        break
            else:
                for i in range(uBound, lBound + 1, -1):
                    if (palindrom / i > uBound or i * i < palindrom):
                        break
                    if (palindrom % i == 0):
                        Found = True
                        break
            firstHalf -= 1
        return palindrom % 1337
