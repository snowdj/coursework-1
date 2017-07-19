"""
Time: O(n)
Space: O(n)

Given a binary tree, return the bottom-up level order traversal of its nodes'
values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import collections


# BFS + queue
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        q = collections.deque([(root, 0)])
        while q:
            node, level = q.popleft()
            if node:
                if len(res) < level + 1:
                    res.insert(0, [])
                res[-(level+1)].append(node.val)
                q.append((node.left, level+1))
                q.append((node.right, level+1))
        return res

    def levelOrderBottom2(self, root):
            res, queue = [], [root]
            while queue:
                res.append([node.val for node in queue if node])
                queue = [child for node in queue if node for child in (node.left, node.right)]
            return res[-2::-1]


# BFS + stack
class Solution2(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        stack = [(root, 0)]
        while stack:
            node, level = stack.pop()
            if node:
                if len(res) < level + 1:
                    res.append([])
                res[level].append(node.val)
                stack.append((node.right, level+1))
                stack.append((node.left, level+1))
        return res[::-1]


# recursive DFS
class Solution3(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        def dfs(root, level, res):
            if root:
                if len(res) < level + 1:
                    res.append([])
                res[level].append(root.val)
                dfs(root.left, level+1, res)
                dfs(root.right, level+1, res)
        res = []
        dfs(root, 0, res)
        return res[::-1]
