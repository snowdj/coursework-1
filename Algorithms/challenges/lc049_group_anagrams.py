"""
Time: O(m*n)  m is max length of strings.
Space: O(n)

Given an array of strings, group anagrams together.

For example, given: ["eat", "tea", "tan", "ate", "nat", "bat"], 
Return:

[
  ["ate", "eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note: All inputs will be in lower-case.
"""


# Hash alphabet counting table. 279ms.
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        tbl = {}
        for s in strs:
            cnt = [0] * 26
            for c in s:
                cnt[ord(c)-ord('a')] += 1
            tbl.setdefault(tuple(cnt), []).append(s)
        return [member for group, member in tbl.items()]


# Sort each string. 229ms. O(mlg(m)*n) / O(n)
class Solution2(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = collections.defaultdict(list)
        for s in strs:
            groups[tuple(sorted(s))].append(s)
        return map(sorted, groups.values())


# 302ms
class Solution3(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = itertools.groupby(sorted(strs, key=sorted), sorted)
        return [sorted(members) for _, members in groups]
