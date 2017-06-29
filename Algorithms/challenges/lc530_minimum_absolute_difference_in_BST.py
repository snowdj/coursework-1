"""
Time: O(n)
Space: O(log(n))

Given a binary search tree with non-negative values, find the minimum absolute
difference between values of any two nodes.

Example:

Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1, which is the difference between 2 and 1
(or between 2 and 3).

Note: There are at least two nodes in this BST.
"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        Recursive inorder tree walk. Time: O(n) Space: O(n).
        """
        nums = self.inorder(root)
        return min(nums[i+1]-nums[i] for i in range(len(nums)-1))

    def inorder(self, root):
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)\
            if root else []


class Solution1(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        Recursive inorder tree walk.
        """
        def inorder(node, pre, res):
            """
            """
            if node is None:
                return pre, res
            pre, res = inorder(node.left, pre, res)
            res = min(res, node.val - pre)
            pre = node.val
            pre, res = inorder(node.right, pre, res)
            return pre, res
        pre, res = inorder(root, -float('inf'), float('inf'))
        return res


class Solution2(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        Iterative inorder tree walk with a stack.
        """
        pre, res = -float('inf'), float('inf')
        node = root
        stk = []
        while node or stk:
            while node:
                stk.append(node)
                node = node.left
            node = stk[-1]  # step back from NIL node
            res = min(res, stk.pop().val - pre)
            pre = node.val
            node = node.right
        return res


class Solution3(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        Recursive preorder tree walk.
        """
        def preorder(node, pred, succ, res):
            """
            At each recursion, ignore node's subtree and compare node with its
            current predecessor and current successor.
            :param pred: current predecessor of node if ignoring its subtree
            :param succ: current successor of node if ignoring its subtree
            """
            if node is None:
                return res
            res = min(res, node.val - pred)
            res = min(res, succ - node.val)
            res = preorder(node.left, pred, node.val, res)
            res = preorder(node.right, node.val, succ, res)
            return res
        return preorder(root, -float('inf'), float('inf'), float('inf'))
