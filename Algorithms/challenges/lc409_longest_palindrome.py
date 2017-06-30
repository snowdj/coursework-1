"""
Time: O(n)
Space: O(n)

Given a string which consists of lowercase or uppercase letters, find the
length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""


import collections


class mySolution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        lookup = set()
        for c in s:
            if c in lookup:
                lookup.remove(c)
            else:
                lookup.add(c)
        l = len(s) - len(lookup) + bool(lookup)
        return l


def shortlongestPalindrome1(self, s):
    use = sum(v & ~1 for v in collections.Counter(s).values())
    return use + (use < len(s))


def shortlongestPalindrome2(self, s):
    odds = sum(v & 1 for v in collections.Counter(s).values())
    return len(s) - odds + bool(odds)
    # or
    # return len(s) - odds + (odds > 0)


def shortlongestPalindrome3(self, s):
    counts = collections.Counter(s).values()
    return sum(v & ~1 for v in counts) + any(v & 1 for v in counts)
