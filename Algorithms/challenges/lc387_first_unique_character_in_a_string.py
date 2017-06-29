"""
Time: O(n)
Space: O(n)

Given a string, find the first non-repeating character in it and return it's
index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""


# Hash table
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        lookup = {}
        for c in s:
            lookup[c] = lookup.get(c, 0) + 1
        for i, c in enumerate(s):
            if lookup[c] == 1:
                return i
        return -1


# Use alphabet as a direct-address table
class Solution2(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        lookup = [0] * 26
        for c in s:
            lookup[ord(c) - ord('a')] += 1
        for i, c in enumerate(s):
            if lookup[ord(c) - ord('a')] == 1:
                return i
        return -1
