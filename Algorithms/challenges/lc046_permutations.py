"""
Time: O(n*n!)
Space: O(n)

Given a collection of distinct numbers, return all possible permutations.

For example,
[1,2,3] have the following permutations:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        res = []

        def dfs(level, visited, s):
            if level == n:
                res.append(list(s))
            else:
                for i in range(n):
                    if not visited[i]:
                        visited[i] = True
                        s.append(nums[i])
                        dfs(level+1, visited, s)
                        s.pop()
                        visited[i] = False

        dfs(0, [False] * n, [])
        return res


# DP/BFS
# Insert a3 to a1a2 and a2a1:
#   _ a1 _ a2 _ : a3a1a2, a1a3a2, a1a2a3
#   _ a2 _ a1 _ : a3a2a1, a2a3a1, a2a1a3
class Solution2(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []

        n = len(nums)
        res, stk = [[]], []
        for level in range(n):
            res, stk = stk, res
            while stk:
                s = stk.pop()
                for i in range(len(s)+1):
                    res.append(s[:i] + [nums[level]] + s[i:])
        return res
