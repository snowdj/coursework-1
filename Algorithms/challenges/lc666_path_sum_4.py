"""
Time: O(n)
Space: O(n)


If the depth of a tree is smaller than 5, then this tree can be represented by a list of three-digits integers.

For each integer in this list:

The hundreds digit represents the depth D of this node, 1 <= D <= 4.
The tens digit represents the position P of this node in the level it belongs to, 1 <= P <= 8. The position is the same as that in a full binary tree.
The units digit represents the value V of this node, 0 <= V <= 9.


Given a list of ascending three-digits integers representing a binary with the depth smaller than 5. You need to return the sum of all paths from the root towards the leaves.

Example 1:

Input: [113, 215, 221]
Output: 12
Explanation:
The tree that the list represents is:
    3
   / \
  5   1

The path sum is (3 + 5) + (3 + 1) = 12.


Example 2:

Input: [113, 221]
Output: 4
Explanation:
The tree that the list represents is:
    3
     \
      1

The path sum is (3 + 1) = 4.
"""


# DFS, preorder
class Solution(object):
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        res = 0
        tbl = {x // 10: x % 10 for x in nums}  # {loc: val}

        def dfs(loc, path_sum):
            nonlocal res, tbl
            path_sum += tbl[loc]
            level, pos = loc // 10, loc % 10
            left = (level + 1) * 10 + 2 * pos - 1
            right = left + 1
            if left not in tbl and right not in tbl:  # leaf
                res += path_sum
                return
            if left in tbl:
                dfs(left, path_sum)
            if right in tbl:
                dfs(right, path_sum)

        dfs(nums[0]//10, 0)
        return res


# BFS, preorder
from collections import deque
class Solution2(object):
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        res = 0
        tbl = {x // 10: x % 10 for x in nums}  # {loc: val}
        q = deque([nums[0]//10])
        while q:
            loc = q.popleft()
            level, pos = loc // 10, loc % 10
            left = (level + 1) * 10 + 2 * pos - 1
            right = left + 1
            if left not in tbl and right not in tbl:
                res += tbl[loc]
            if left in tbl:
                tbl[left] += tbl[loc]  # add current node value to children
                q.append(left)
            if right in tbl:
                tbl[right] += tbl[loc]  # add current node value to children
                q.append(right)
        return res
