"""
Time: O(n)
Space: O(lg(n)) recursively, O(n) BFS.

Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
"""


from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# DFS recursively
class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return min((self.minDepth(child)
                    for child in (root.left, root.right) if child),
                   default=0) + 1  # Python 3. For Py2, use min([iter] + [0]).


# BFS
class Solution2(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        q, mindep = deque([(root, 1)]), 0
        while q:
            node, mindep = q.popleft()
            if any([node.left, node.right]):
                q.extend([(child, mindep+1)
                          for child in (node.left, node.right) if child])
            else:
                return mindep
