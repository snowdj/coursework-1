"""
Time: O(n)
Space: O(lg(n))

Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:
    2
   / \
  1   3
Binary tree [2,1,3], return true.
Example 2:
    1
   / \
  2   3
Binary tree [1,2,3], return false.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Direct DFS recursion
class MySolution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(root, left, right):
            if not root:
                return True
            return (root.left and left < root.left.val < root.val
                    and dfs(root.left, left, root.val) or not root.left)\
                    and\
                    (root.right and root.val < root.right.val < right
                     and dfs(root.right, root.val, right) or not root.right)
        return dfs(root, float('-inf'), float('inf'))


# Convert tree to sorted array by inorder traversal
class Solution2:
    def isValidBST(self, root):
        def inOrder(root):
            if root is None:
                return
                yield
            for x in inOrder(root.left):
                yield x
            yield root.val
            for x in inOrder(root.right):
                yield x

        pre = float('-inf')
        for x in inOrder(root):
            if pre >= x:
                return False
            pre = x
        return True
