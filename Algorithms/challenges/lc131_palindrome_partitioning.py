"""
Time: O(n^2)
Space: O(N)

Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

For example, given s = "aab",
Return

[
  ["aa","b"],
  ["a","a","b"]
]
"""


# Stefan's Recursive DFS
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        return [
            [s[:i]] + rest
            for i in range(1, len(s)+1)
            if s[:i] == s[i-1::-1]
            for rest in self.partition(s[i:])
        ] or [[]]
