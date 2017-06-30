"""
Time: O(n)
Space: O(1)

Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.
"""


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {'M': 1000, 'D': 500, 'C': 100,
                 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        n = 0
        for i in range(len(s)):
            val = roman[s[i]]
            if (i == len(s) - 1) or val >= roman[s[i+1]]:
                n += val
            else:
                n -= val
        return n
