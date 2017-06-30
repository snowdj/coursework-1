"""
Time: O(n)
Space: O(log(n)), or O(1) using iteration.

Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and
the nodes have the same value.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q


class Solution2(object):
    def isSameTree(self, p, q):
        def t(n):
            return n and (n.val, t(n.left), t(n.right))
        return t(p) == t(q)


class Solution3(object):
    def isSameTree(self, p, q):
        return p and q \
            and p.val == q.val \
            and all(map(self.isSameTree, (p.left, p.right), (q.left, q.right))) \
            or p is q
