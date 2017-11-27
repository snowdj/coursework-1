"""
Time: O(n)
Space: O(h)

Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# In DFS, res compares with the sum of both sub-branches and current node,
# but only return the larger branch.
class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = -float('inf')

        def dfs(root):
            nonlocal res
            if root is None:
                return 0
            leftmax = dfs(root.left)
            rightmax = dfs(root.right)
            res = max(res, max(leftmax, 0) + max(rightmax, 0) + root.val)
            return max(leftmax, rightmax, 0) + root.val
        dfs(root)
        return res
