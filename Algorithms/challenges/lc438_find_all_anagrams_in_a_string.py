"""
Time: O(ns+np)
Space: O(ns+np)

Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res, pm, sm = [], {}, {}
        for c in p:
            pm[c] = pm.get(c, 0) + 1
        for i in range(len(s)):
            sm[s[i]] = sm.get(s[i], 0) + 1
            if i >= len(p):
                sm[s[i-len(p)]] -= 1
                if sm[s[i-len(p)]] == 0:
                    del sm[s[i-len(p)]]
            if pm == sm:
                res.append(i + 1 - len(p))  # look backward, add start index.
        return res


from collections import Counter


# Very smart solution.
# Assign positive/negative count to p and s.
# Use Counter.update() to increase or decrease.
class Solution2(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        ns, np, res = len(s), len(p), []
        cnt = Counter(p)  # positive count for p
        cnt.subtract(s[:np-1])  # negative count for s
        for i in range(np-1, ns):
            cnt.update({s[i]: -1})  # decrease window right
            i < np or cnt.update({s[i-np]: 1})  # increase window left
            if not any(cnt.values()):  # check all letters count 0
                res.append(i-(np-1))
        return res
