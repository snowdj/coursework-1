"""
Time: O(n)
Space: O(n)

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""


# scan from left to right.
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        tbl = {'(': ')', '[': ']', '{': '}'}
        stk = []
        for c in s:
            if c in tbl.keys():
                stk.append(c)
            elif not stk or tbl[stk.pop()] != c:
                return False
        return not stk


# scan from right to left.
class Solution2(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        tbl = {'(': ')', '[': ']', '{': '}'}
        stk = []
        for c in reversed(s):
            if c in tbl.values():  # right parentheses
                stk.append(c)
            elif not stk or tbl[c] != stk.pop():  # no right parenthesis to match, or wrong type
                return False
        return not stk  # if any right parenthesis left in stack
