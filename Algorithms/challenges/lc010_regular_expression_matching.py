"""
Time: O(m*n)
Space: O(m*n)

Implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") ? false
isMatch("aa","aa") ? true
isMatch("aaa","aa") ? false
isMatch("aa", "a*") ? true
isMatch("aa", ".*") ? true
isMatch("ab", ".*") ? true
isMatch("aab", "c*a*b") ? true
"""


# Prefix dynamic programming
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # General cases
        # 1 If p[j] == s[i]:  dp[i][j] = dp[i-1][j-1]
        # 2 If p[j] == '.':  dp[i][j] = dp[i-1][j-1]
        # 3 If p[j] == '*', two sub conditions:
        #   3.1   if p[j-1] != s[i] and p[j-1] != '.':
        #             dp[i][j] = dp[i][j-2]  //in this case, a* only counts as empty
        #   3.2   if p[j-1] == s[i] or p[j-1] == '.':
        #             dp[i][j] = dp[i-1][j]   // in this case, a* counts as multiple a 
        #          or dp[i][j] = dp[i][j-1]   // in this case, a* counts as single a
        #          or dp[i][j] = dp[i][j-2]   // in this case, a* counts as empty

        m, n = len(s), len(p)

        # dp[i][j] means the match status between p[:i] and s[:j].
        # dp[0][0] means the match status of two empty strings.
        dp = [[False] * (n+1) for _ in range(m+1)]

        # Base case
        dp[0][0] = True

        # Corner case: s is empty but p is not.
        # Since each '*' can eliminate the charter before it, the table is
        # vertically updated by the one before previous.
        for j in range(2, len(p) + 1):
            dp[0][j] = p[j-1] == '*' and dp[0][j-2]

        # General cases
        for i in range(m):
            for j in range(n):
                if p[j] == '.' or p[j] == s[i]:
                    dp[i+1][j+1] = dp[i][j]
                if p[j] == '*':
                    if p[j-1] != s[i] and p[j-1] != '.':
                        dp[i+1][j+1] = dp[i+1][j-1]
                    else:
                        dp[i+1][j+1] = dp[i][j+1] or dp[i+1][j] or dp[i+1][j-1]
        return dp[m][n]
