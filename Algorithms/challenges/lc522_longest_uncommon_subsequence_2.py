"""
Time: O(n^2 * L), L is the max length of strings.
Space: O(1)

Given a list of strings, you need to find the longest uncommon subsequence
among them. The longest uncommon subsequence is defined as the longest
subsequence of one of these strings and this subsequence should not be any
subsequence of the other strings.

A subsequence is a sequence that can be derived from one sequence by deleting
some characters without changing the order of the remaining
elements. Trivially, any string is a subsequence of itself and an empty string
is a subsequence of any string.

The input will be a list of strings, and the output needs to be the length of
the longest uncommon subsequence. If the longest uncommon subsequence doesn't
exist, return -1.

Example 1:
Input: "aba", "cdc", "eae"
Output: 3

Note:
All the given strings' lengths will not exceed 10.
The length of the given list will be in the range of [2, 50].
"""


class Solution(object):
    def findLUSlength(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        def subseq(sub, word):
            i = 0
            for c in word:
                if i < len(sub) and c == sub[i]:
                    i += 1
                if i == len(sub):
                    break
            return i == len(sub)

        strs.sort(key=len, reverse=True)
        for i, word1 in enumerate(strs):
            if all(not subseq(word1, word2)
                   for j, word2 in enumerate(strs) if i != j):
                return len(word1)
        return -1
