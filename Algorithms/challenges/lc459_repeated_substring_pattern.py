"""
Time: O(n*m)  m is length of substring by Boyer-Moore-Horspool.
Space: O(n)

Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

Example 1:
Input: "abab"

Output: True

Explanation: It's the substring "ab" twice.
Example 2:
Input: "aba"

Output: False
Example 3:
Input: "abcabcabcabc"

Output: True

Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
"""


class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sub = ''
        for i in range(len(s)//2+1):
            if sub and s[i] == sub[0] and (len(s)-i) % len(sub) == 0:
                j = i
                while j < len(s):
                    if s[j:j+len(sub)] != sub:
                        break
                    j += len(sub)
                if j == len(s):
                    return True
            sub += s[i]
        return False


# https://discuss.leetcode.com/topic/68206/easy-python-solution-with-explaination
def repeatedSubstringPattern(self, s):

        """
        :type s: str
        :rtype: bool
        """
        return s in (2 * s)[1:-1] if s else False
