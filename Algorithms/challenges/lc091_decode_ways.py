"""
Time: O(n)
Space: O(n) or O(1) for DP

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2.
"""


# DP
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':
            return 0
        n = len(s)
        dp = [0] * (n+1)
        dp[0] = 1
        for i in range(n):
            if s[i] != '0':
                dp[i+1] = dp[i]
            if i > 0 and '10' <= s[i-1:i+1] <= '26':
                dp[i+1] += dp[i-1]
        return dp[-1]
