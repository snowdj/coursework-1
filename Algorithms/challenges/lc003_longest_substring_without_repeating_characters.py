"""
Time: O(n)
Space: O(1)  because max of len(set) is 256, size of ASCII.

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        i = -1  # critical: i is exclusive left boundary of unique set.
        m = {}  # or use a list of 256 0s.
        maxlen = 0
        for j in range(n):
            i = max(m.get(s[j], -1), i)  # critical
            m[s[j]] = j
            maxlen = max(maxlen, j-i)
        return maxlen
