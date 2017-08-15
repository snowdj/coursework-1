"""
Time: O(n)
Space: O(lg(n)) with passing indices instead of list slices.

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        root = TreeNode(preorder[0])
        i = inorder.index(root.val)
        inorder_left, inorder_right = inorder[:i], inorder[i+1:]
        root.left = self.buildTree(preorder[1:len(inorder_left)+1], inorder_left)
        root.right = self.buildTree(preorder[len(inorder_left)+1:], inorder_right)
        return root


# faster, as pop() removes all left subtree nodes after return root.left.
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind+1:])
            return root
