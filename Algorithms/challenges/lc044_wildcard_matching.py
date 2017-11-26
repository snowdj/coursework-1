"""
Time: O(max(m,n))
Space: O(1)


Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false
"""


# Straightforward logic. 165ms
# http://www.cnblogs.com/grandyang/p/4401196.html
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)

        # si, pi: current char position in s and p
        si, pi = 0, 0
        # p_ast: position of last asterisk in p
        # s_ast: position in s corresponding to p_ast
        p_ast, s_ast = None, None

        while si < m:
            if pi < n and (s[si] == p[pi] or p[pi] == '?'):
                si += 1
                pi += 1
            elif pi < n and p[pi] == '*':
                p_ast, pi = pi, pi+1
                s_ast = si
            elif p_ast is not None:  # State explicitly bc p_ast could be 0.
                pi = p_ast + 1
                s_ast += 1
                si = s_ast
            else:
                return False  # p is consumed before s, or pi has a different char than si
        while pi < n and p[pi] == '*':  # consume all remaining * in p
            pi += 1
        return pi == n


# Prefix DP, similar as lc010 regular expression matching. O(m*n), 1325ms.
# Only difference is the meaning of '*'
# http://www.cnblogs.com/grandyang/p/4401196.html
class Solution2:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)

        # dp[i][j] means the match status between p[:i] and s[:j].
        # dp[0][0] means the match status of two empty strings.
        dp = [[False] * (n+1) for _ in range(m+1)]
        dp[0][0] = True  # base case

        # Corner case: s is empty but p is not
        # dp[0][j] is True if p[j-1] == '*'
        for j in range(1, n+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-1]

        # General case
        for i in range(m):
            for j in range(n):
                if p[j] != '*':
                    dp[i+1][j+1] = dp[i][j] and (s[i] == p[j] or p[j] == '?')
                else:
                    dp[i+1][j+1] = dp[i][j+1] or dp[i+1][j]  # depends on if s[i] == p[j-1]
        return dp[m][n]


# 1-dimension DP. Each column of dp[i][j] is updated from previous. O(m*n), 429ms.
class Solution3:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)

        # Corner case: s is empty but p is not
        if n - p.count('*') > m:
            return False

        # General case
        dp = [True] + [False] * m
        for px in p:
            if px != '*':
                for i in reversed(range(m)):
                    dp[i+1] = dp[i] and (px == s[i] or px == '?')
            else:
                for i in range(1, m+1):
                    dp[i] = dp[i-1] or dp[i]
            dp[0] = dp[0] and px == '*'
        return dp[-1]
