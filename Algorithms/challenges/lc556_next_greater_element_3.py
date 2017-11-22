"""
Time: O(nlg(n))
Space: O(n)


Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has exactly the same digits existing in the integer n and is greater in value than n. If no such positive 32-bit integer exists, you need to return -1.

Example 1:
Input: 12
Output: 21
Example 2:
Input: 21
Output: -1
"""


class Solution:
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        dig = [int(d) for d in str(n)]
        N = len(dig)

        # find the least significant digit that has next greater element
        for i in reversed(range(N)):
            if i == 0:
                return -1
            if dig[i] > dig[i-1]:
                break

        # swap i with the SMALLEST next greater element
        for j in reversed(range(N)):
            if dig[j] > dig[i-1]:
                dig[i-1], dig[j] = dig[j], dig[i-1]
                break

        # sort dig[i:]
        dig_asc = dig[:i] + sorted(dig[i:])

        res = int(''.join(str(d) for d in dig_asc))
        return res if res < 2**31 else -1
