"""
Time: O(n^2)
Space: O(n^2)

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. You may assume the dictionary does not contain duplicate words.

Return all such possible sentences.

For example, given
s = "catsanddog",
dict = ["cat", "cats", "and", "sand", "dog"].

A solution is ["cats and dog", "cat sand dog"].
"""


# DP of suffix subproblems, recursively.
# For either solution, key point is DFS + memoize.

# Stefan's solution
# m[i] memoizes all combinations that can be built from s[i:]
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        n = len(s)
        m = {n: ['']}

        def DFS(i):
            if i not in m:
                m[i] = [
                    s[i:j] + (tail and ' '+tail)
                    for j in range(i+1, n+1)
                    if s[i:j] in wordDict
                    for tail in DFS(j)
                ]
            return m[i]
        return DFS(0)


# From Java solution. Loop over wordDict, instead of j in range(i+1,n+1).
# Use substring as hash table keys.
# m[s] memoizes all combinations that can be built from s.
class Solution2(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        m = {'': ['']}

        def DFS(s):
            if s not in m:
                m[s] = [
                    word + (tail and ' '+tail)
                    for word in wordDict
                    if s.startswith(word)
                    for tail in DFS(s[len(word):])
                ]
            return m[s]

        return DFS(s)
