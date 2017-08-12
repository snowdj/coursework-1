"""
Time: O(n^2)
Space: O(n) for timsort.

Given a set of distinct integers, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


# Add new element x to previous level if x is larger than the last element.
class MySolution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        res = [[]]
        for level in range(n):
            for st in res:
                if len(st) == level:
                    for x in sorted(nums):
                        if not st or x > st[-1]:
                            res.append(st + [x])
        return res


# For each new element, add it to all previous subsets.
class Solution1(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for x in sorted(nums):
            res += [subset + [x] for subset in res]
        return res


# Bit manipulation. Go over true table of the index of all combinations.
class Solution2(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        res = []
        nums.sort()
        for k in range(1 << n):  # 2^n subsets
            subset = []  # O(n) space
            for j in range(n):
                if k & 1 << j:  # k >> j & 1
                    subset.append(nums[j])
            res.append(subset)
        return res


# DFS recursively
class Solution3(object):
    def subsets(self, nums):
        res = []
        self.dfs(sorted(nums), 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in xrange(index, len(nums)):
            self.dfs(nums, i+1, path+[nums[i]], res)
