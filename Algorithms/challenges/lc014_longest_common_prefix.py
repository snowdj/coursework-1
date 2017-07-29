"""
Time: O(n)
Space: O(1), excluding return.

Write a function to find the longest common prefix string amongst an array of strings.
"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        cnt = 0
        for s in zip(*strs):
            if len(set(s)) == 1:  # or scan over s to avoid extra space for set
                cnt += 1
            else:
                break
        return strs[0][:cnt] if strs else ''


class Solution2(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        return min(strs or [''])  # in case input is [''] or []
