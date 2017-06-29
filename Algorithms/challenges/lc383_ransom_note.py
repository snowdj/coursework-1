"""
Time: O(m+n)
Space: O(m)

Given an arbitrary ransom note string and another string containing letters
from all the magazines, write a function that will return true if the ransom
note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note: You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true
"""


from collections import Counter


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        mag = {}
        for c in magazine:
            mag[c] = mag.get(c, 0) + 1
        for c in ransomNote:
            if mag.get(c, 0) == 0:
                return False
            else:
                mag[c] -= 1
        return True


class Solution2(object):
    def canConstruct(self, ransomNote, magazine):
        """
        Counter subtraction using operator '-' only keeps nonnegative values,
        but Counter.subtract(Counter) can keep negative values.
        """
        return not Counter(ransomNote) - Counter(magazine)
