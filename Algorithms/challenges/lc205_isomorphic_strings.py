"""
Time: O(n)
Space: O(1) because max(len(hash table)) = 256.

Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

For example,
Given "egg", "add", return true.

Given "foo", "bar", return false.

Given "paper", "title", return true.

Note:
You may assume both s and t have the same length.
"""


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        tbl, r = {}, ''
        for i in range(len(s)):
            if s[i] not in tbl and t[i] in tbl.values():
                return False
            r += tbl.setdefault(s[i], t[i])
        return r == t


def isIsomorphic(self, s, t):
    d1, d2 = [0] * 256, [0] * 256
    for i in range(len(s)):
        if d1[ord(s[i])] != d2[ord(t[i])]:
            return False
        d1[ord(s[i])] = i+1
        d2[ord(t[i])] = i+1
    return True


# best
def isIsomorphic3(self, s, t):
    return len(set(zip(s, t))) == len(set(s)) == len(set(t))


def isIsomorphic4(self, s, t):
    return [s.find(i) for i in s] == [t.find(j) for j in t]


def isIsomorphic5(self, s, t):
    return map(s.find, s) == map(t.find, t)


def isIsomorphic1(self, s, t):
    d1, d2 = {}, {}
    for i, val in enumerate(s):
        d1.setdefault(val, []).append(i)
    for i, val in enumerate(t):
        d2.setdefault(val, []).append(i)
    return sorted(d1.values()) == sorted(d2.values())  # O(n*lg(n))

def isIsomorphic2(self, s, t):
    d1, d2 = [[] for _ in range(256)], [[] for _ in range(256)]
    for i, val in enumerate(s):
        d1[ord(val)].append(i)
    for i, val in enumerate(t):
        d2[ord(val)].append(i)
    return sorted(d1) == sorted(d2)  # O(n*lg(n))


