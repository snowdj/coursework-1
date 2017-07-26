"""
Time: O(n)
Space: O(lg(n))

Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# recursive post-order traversal
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def post(root):
            if not root:
                return True, 0
            left, ht_left = post(root.left)
            right, ht_right = post(root.right)
            return left and right and abs(ht_left - ht_right) < 2, max(ht_left, ht_right) + 1
        return post(root)[0]


# iterative post-order traversal using two stacks
# or using one stack:
#   https://discuss.leetcode.com/topic/42953/very-simple-python-solutions-iterative-and-recursive-both-beat-90
class Solution2(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        depth = {}
        s1, s2 = [], []
        if root:
            s1.append(root)
        while s1:
            node = s1.pop()
            s2.append(node)
            if node.left:
                s1.append(node.left)
            if node.right:
                s1.append(node.right)
        while s2:  # reversed postorder traversal
            node = s2.pop()
            ht_left, ht_right = depth.get(node.left, 0), depth.get(node.right, 0)
            if abs(ht_left - ht_right) > 1:
                return False
            depth[node] = 1 + max(ht_left, ht_right)
        return True
