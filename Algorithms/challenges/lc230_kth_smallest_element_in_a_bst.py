"""
Time: O(n)
Space: O(lg(n))

Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note: 
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def inorder(root):
            if not root:
                yield
                return
            for node in inorder(root.left):
                yield node
            yield root
            for node in inorder(root.right):
                yield node
        cnt = 0
        for node in inorder(root):
            if node is not None:
                cnt += 1
            if cnt == k:
                return node.val


# follow up: https://discuss.leetcode.com/topic/17668/what-if-you-could-modify-the-bst-node-s-structure/11
