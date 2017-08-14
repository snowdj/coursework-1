"""
Time: O(n)
Space: O(n)

Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""


import collections


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class MySolution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        next_level = collections.deque([root]) if root else []
        while next_level:
            res.append([])
            cur_level = next_level
            next_level = collections.deque()
            while cur_level:
                nd = cur_level.popleft()
                res[-1].append(nd.val)
                if nd.left:
                    next_level.append(nd.left)
                if nd.right:
                    next_level.append(nd.right)
        return res


class ShortSolution(object):
    def levelOrder(self, root):
        ans, level = [], [root]
        while root and level:
            ans.append([node.val for node in level])
            level = [kid for n in level for kid in (n.left, n.right) if kid]
        return ans
