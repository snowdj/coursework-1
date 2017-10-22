"""
Time: O(n^2)
Space: O(n)

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".
"""


class Solution(object):
    """
    Dynamic Programming Steps:
    (1) subproblems: prefixes, s[:i], i in range(n+1)
        -- number of subproblems: n
    (2) guess: if s[:j] for j in range(i) break s[:i]
        -- number of guesses = i = O(n)
    (3) recurrence: DP[i] = any(DP[j] and s[j:i] in wordDict
                                for j in range(i))
        -- time/subproblem = i = O(n)
        -- j = 0 means the whole substring s[0:i].
        -- DP[0] = True: base case, empty string.
    (4) topological order: i = 0, ..., n
        -- total time: O(n^2)
    (5) Solve original problem: DP[n]
    """
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        DP = [True] * (n+1)
        for i in range(1, n+1):
            DP[i] = any(DP[j] and s[j:i] in wordDict for j in range(i))
        return DP[n]
