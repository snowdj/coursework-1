"""
Time: O(n^2) with scanning centers or DP, or O(n) with Manacher's algorithm.
Space: O(1) with scanning centers, O(n) with DP and Manacher's algorithm.

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example:

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.
Example:

Input: "cbbd"

Output: "bb"
"""


# Scanning centers, and expanding around centers.
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def expand_around_center(s, left, right):
            l, r = left, right
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l, r = l-1, r+1
            return r-l-1

        start = end = 0
        for i in range(len(s)):
            len1 = expand_around_center(s, i, i)
            len2 = expand_around_center(s, i, i+1)
            maxlen = max(len1, len2)
            if maxlen > end-start+1:
                start = i - (maxlen-1) // 2
                end = i + maxlen // 2
        return s[start:end+1]


# Dynamic Programming
# 1. subproblems. For string s of length n, we have:
#                 1 subproblem of length n, s[0:n]
#                 2 subproblems of length n-1, s[0:n-1], s[1:n]
#                 3 subproblems of length n-2, s[0:n-2], s[1:n-1], s[2:n]
#                 ...
#                 n subproblems of length 1, s[0:1], s[1:2], ..., s[n-1:n]
#    Total # subproblems: 1 + 2 + 3 + ... + n = n(n+1)/2 = O(n^2)
# 2. guess. For subproblem s[i:j], it is a palindrome if
#           s[i] == s[j-1], if s[i+1:j-1]
#    - # guesses: 2
# 3. Recurrence: dp(i, j) = dp(i+1, j-1) and s[i] == s[j-1]
#    - base case: dp(i, i+1) = True, dp(i, i+2) = s[i] == s[i+1]
#    - Time: O(1)
# 4. Total time: O(n^2)
#    - topological sort: dp(i, i+l) for i=1..n for l =1..n
# 5. solve original problem: dp(0, n)


# Manacher's Algorithm
# http://www.cnblogs.com/grandyang/p/4475985.html
# http://www.geeksforgeeks.org/manachers-algorithm-linear-time-longest-palindromic-substring-part-1/
