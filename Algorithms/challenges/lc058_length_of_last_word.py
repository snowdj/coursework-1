"""
Time: O(n)
Space: O(1)

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

For example,
Given s = "Hello World",
return 5.
"""


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        while n > 0 and s[n-1] == ' ':
            n -= 1
        end = n
        while n > 0 and s[n-1] != ' ':
            n -= 1
        return end - n


# just for fun
def lengthOfLastWord(self, s):
    return 0 if len(s.split()) == 0 else len(s.split()[-1])
