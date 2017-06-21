"""
Time: O(n)
Space: O(n)

Given a string, determine if a permutation of the string could form a
palindrome.

For example, "code" -> False, "aab" -> True, "carerac" -> True.

Hint:

1. Consider the palindromes of odd vs even length. What difference do you
notice?
2. Count the frequency of each character.
3. If each character occurs even number of times, then it must be a palindrome.
How about character which occurs odd number of times?

Solution: Number of odd character frequency can only be 0 (even number of
 characters) or 1 (odd number of characters).
"""


import collections


class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        m = collections.Counter(s)  # hash table for each character frequency
        return sum(v % 2 for v in m.values()) < 2


class Solution2(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st = set()
        for c in s:
            if c in st:
                st.remove(c)
            else:
                st.add(c)
        return len(st) < 2
