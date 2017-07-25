"""
Time: O(n)
Space: O(1), excluding implicit recursion stack space,
       or use Morris inorder traversal to save recursion stack space.
https://discuss.leetcode.com/topic/77335/proper-o-1-space

Given a binary search tree (BST) with duplicates, find all the mode(s) (the most frequently occurred element) in the given BST.

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than or equal to the node's key.
The right subtree of a node contains only nodes with keys greater than or equal to the node's key.
Both the left and right subtrees must also be binary search trees.
For example:
Given BST [1,null,2,2],
   1
    \
     2
    /
   2
return [2].

Note: If a tree has more than one mode, you can return them in any order.

Follow up: Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def count_mode(self, val):
        if val != self.curval:
            self.curval = val
            self.cnt = 0
        self.cnt += 1
        if self.cnt > self.maxcnt:
            self.maxcnt = self.cnt
            self.modes = [self.curval]
            self.modecnt = 1
        elif self.cnt == self.maxcnt:
            self.modes.append(self.curval)
            self.modecnt += 1

    # recursive inorder walk, or use Morris inorder walk.
    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        self.count_mode(root.val)
        self.inorder(root.right)

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.curval, self.cnt, self.maxcnt, self.modecnt = None, 0, 0, 0
        self.modes = []
        self.inorder(root)
        return self.modes
