"""
Time: O(n)
Space: O(1)

Given a positive integer, return its corresponding column title as appear in
an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
"""


class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = ''
        while n:
            s += chr((n - 1) % 26 + ord('A'))
            n = (n - 1) // 26
        return s[::-1]


class Solution2(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        return "" if n == 0 else self.convertToTitle((n - 1) // 26) + chr((n - 1) % 26 + ord('A'))
