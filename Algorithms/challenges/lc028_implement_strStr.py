"""
Time: O(m*n)
Space: O(1)

Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if
needle is not part of haystack.
"""


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        m, n = len(haystack), len(needle)
        for i in range(m-n+1):
            j = 0
            while j < n and needle[j] == haystack[i+j]:
                j += 1
            if j == n:
                return i
        return -1
