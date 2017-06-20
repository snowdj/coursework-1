"""
Time: O(n)
Space: O(n)

Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
"""


class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str

        Pythonic version.
        """
        return s[::-1]


class Solution2(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str

        Recursive version.
        """
        k = len(s) // 2
        if k == 0:
            return s
        return self.reverseString(s[k:]) + self.reverseString(s[:k])
