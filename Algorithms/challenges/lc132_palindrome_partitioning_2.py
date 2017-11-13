"""
Time: O(n^2)
Space: O(n^2)

Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

For example, given s = "aab",
Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""


# DP suffix subproblem. 1500ms.
# dp[i]: minimum cuts needed for s[i:]
# dp[i] = min(n-i-1, min(dp[j+1] + 1) for j in range(i, n) if s[i:j+1] is a palindrome)
class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [n-i-1 for i in range(n+1)]
        # Or dp=[-1] * (n+1). We only need dp[n] = -1
        for i in reversed(range(n)):
            dp[i] = min((dp[j+1]+1 for j in range(i, n)
                         if s[i] == s[j] and ((j-i <= 1) or s[i+1:j] == s[j-1:i:-1])),
                        default=n-i-1)
        return dp[0]


# Double DP. 670ms.
# pldm[i][j]: s[i:j+1] is a palindrome.
# pldm[i][j] = True if s[i] == s[j] and (j-i<=1 or pldm[i+1][j-1]) else False
class Solution2:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        pldm = [[False] * n for _ in range(n)]
        dp = [n-i-1 for i in range(n+1)]
        for i in reversed(range(n)):
            for j in range(i, n):
                if s[i] == s[j] and ((j-i <= 1) or pldm[i+1][j-1]):
                    pldm[i][j] = True
                    dp[i] = min(dp[i], dp[j+1]+1)
        return dp[0]
