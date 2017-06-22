"""
Time: O(n)
Space: O(1)

Given a list of words and two words word1 and word2, return the shortest
distance between these two words in the list.

For example,
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Given word1 = “coding”, word2 = “practice”, return 3.
Given word1 = "makes", word2 = "coding", return 1.

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both
in the list.
"""


class Solution(object):
    def shortestDistance(self, words, word1, word2):
        distance = len(words) - 1  # init to max possible distance
        p = -1  # index of last occurence of word1 or word2
        for i, w in enumerate(words):
            if w in (word1, word2):
                if p != -1 and w != words[p]:
                    distance = min(distance, abs(i - p))
                p = i
        return distance
