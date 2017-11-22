"""
Time: O(n)
Space: O(n)

Given a non-empty array of integers, return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note:
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is
the array's size.
"""
from collections import Counter


# heap O(nlg(k))
# Python Counter().most_common() uses heapq.nlargest(),
# complexity is O(nlg(k)): https://stackoverflow.com/questions/29240807/python-collections-counter-most-common-complexity
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 1.
        # cnt = Counter(nums)
        # return heapq.nlargest(k, cnt, key=cnt.get)
        # 2.
        # return list(zip(*Counter(nums).most_common(k)))[0]
        # 3.
        return [x for x, f in Counter(nums).most_common(k)]


# bucket sort O(n)
class Solution2:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        cnt = Counter(nums)
        bucket = [[] for _ in range(len(nums)+1)]
        for x, f in cnt.items():
            bucket[f].append(x)
        return sum(bucket, [])[-k:]
