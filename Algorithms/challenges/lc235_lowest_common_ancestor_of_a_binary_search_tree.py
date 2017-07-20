"""
Time: O(lg(n))
Space: O(1) for iterative, O(lg(n)) for recursive

Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes v and w as the lowest node in T that has both v and w as descendants (where we allow a node to be a descendant of itself).”

        _______6______
       /              \
    ___2__          ___8__
   /      \        /      \
   0      _4       7       9
         /  \
         3   5
For example, the lowest common ancestor (LCA) of nodes 2 and 8 is 6. Another example is LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# recursive
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if min(p.val, q.val) <= root.val <= max(p.val, q.val):
            return root
        if max(p.val, q.val) < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)

    def lowestCommonAncestor2(self, root, p, q):
        return root if (root.val - p.val) * (root.val - q.val) < 1 else \
               self.lowestCommonAncestor((root.left, root.right)[p.val > root.val], p, q)


# iterative
class Solution2(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        while not (min(p.val, q.val) <= root.val <= max(p.val, q.val)):
            root = root.left if max(p.val, q.val) < root.val else root.right
        return root

    def lowestCommonAncestor2(self, root, p, q):
        while (root.val - p.val) * (root.val - q.val) > 0:
            root = (root.left, root.right)[p.val > root.val]
        return root
