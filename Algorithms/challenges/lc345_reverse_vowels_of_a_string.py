"""
Time: O(n)
Space: O(n)

Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".
"""


import re


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = [i for i in range(len(s)) if s[i] in 'aeiouAEIOU']
        s1 = list(s)
        for i in range(len(vowels)//2):
            s1[vowels[i]], s1[vowels[-i-1]] = s1[vowels[-i-1]], s1[vowels[i]]
        return ''.join(s1)


def reverseVowels1(self, s):
    vowels = re.findall('(?i)[aeiou]', s)
    return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)


def reverseVowels2(self, s):
    vowels = (c for c in reversed(s) if c in 'aeiouAEIOU')
    return re.sub('(?i)[aeiou]', lambda m: next(vowels), s)
