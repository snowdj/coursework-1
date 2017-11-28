"""
Given two words (beginWord and endWord), and a dictionary's word list, find all shortest transformation sequence(s) from beginWord to endWord, such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
Return
  [
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
  ]
Note:
Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
"""
import string
import collections


# 959ms
class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if endWord not in wordList:
            return []
        wordDict = set(wordList)
        wordDict.add(endWord)
        level = {beginWord}
        parents = collections.defaultdict(set)
        while level and endWord not in parents:
            next_level = collections.defaultdict(set)
            for node in level:
                for char in string.ascii_lowercase:
                    for i in range(len(beginWord)):
                        n = node[:i]+char+node[i+1:]
                        if n in wordDict and n not in parents:
                            next_level[n].add(node)
            level = next_level
            parents.update(next_level)
        res = [[endWord]]
        while res and res[0][0] != beginWord:
            res = [[p]+r for r in res for p in parents[r[0]]]
        return res


# 200ms
class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        if endWord not in wordList:
            return []
        wordDict = set(wordList)

        def construct_paths(source, dest, tree):
            if source == dest:
                return [[source]]
            return [[source] + path
                    for child in tree[source]
                    for path in construct_paths(child, dest, tree)]

        def add_path(tree, word, neigh, is_forw):
            if is_forw:
                tree[word] += neigh,
            else:
                tree[neigh] += word,

        def bfs(this_lev, oth_lev, is_forw):
            if not this_lev:
                return False

            if len(this_lev) > len(oth_lev):
                this_lev, oth_lev = oth_lev, this_lev
                is_forw = not is_forw

            nonlocal tree, wordDict

            wordDict -= this_lev.union(oth_lev)

            next_lev, done = set(), False
            while this_lev:
                word = this_lev.pop()
                for c in string.ascii_lowercase:
                    for index in range(len(word)):
                        neigh = word[:index] + c + word[index+1:]
                        if neigh in oth_lev:
                            done = True
                            add_path(tree, word, neigh, is_forw)
                        if not done and neigh in wordDict:
                            next_lev.add(neigh)
                            add_path(tree, word, neigh, is_forw)
            return done or bfs(next_lev, oth_lev, is_forw)

        tree = collections.defaultdict(list)
        is_found = bfs(set([beginWord]), set([endWord]), True)
        return construct_paths(beginWord, endWord, tree)
