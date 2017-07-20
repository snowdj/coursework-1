"""
Time: O(n*lg(n))  since the max # of leaves or paths is ceil(n/2).
Space: O(n*lg(n))

Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        left = self.binaryTreePaths(root.left)
        right = self.binaryTreePaths(root.right)
        if not left+right:
            return [str(root.val)]
        else:
            return ['{}->{}'.format(root.val, s) for s in left+right]

    # stefan's
    def binaryTreePaths2(self, root):
        if not root:
            return []
        return [str(root.val) + '->' + path
                for kid in (root.left, root.right) if kid
                for path in self.binaryTreePaths(kid)] or [str(root.val)]
