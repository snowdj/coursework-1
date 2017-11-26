"""
Time: O(n)
Space: O(1)


Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".

Note:
If there is no such window in S that covers all characters in T, return the empty string "".

If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
"""


# Counting in hash table. Negative counts to indicate unneeded characters.
# https://discuss.leetcode.com/topic/20692/12-lines-python
# Hash table of length <= 256 ASCII
class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # need[c]: how many times a valid window needs char c (can be negative)
        # missing: how many characters are still missing.
        need, missing = collections.Counter(t), len(t)

        # s[i:j]: current window
        # s[I:J]: result window
        i = I = J = 0

        # In the loop, first add the new character to the window.
        # Then, if nothing is missing (a valid window found), remove
        # as much as possible from the window start and then update the result.
        for j, c in enumerate(s, 1):  # starts from 1 for slicing end
            missing -= need[c] > 0
            need[c] -= 1  # Trick: unneeded chars not in t are negative
            if not missing:  # a valid window found
                while i < j and need[s[i]] < 0:  # s[i] is unneeded
                    need[s[i]] += 1  # add back counts for unneeded chars
                    i += 1  # move window left boundary
                if not J or j - i <= J - I:
                    I, J = i, j
        return s[I:J]
