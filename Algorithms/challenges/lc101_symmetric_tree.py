"""
Time: O(n)
Space: O(n)

Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# recursively
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def bfs(l, r):
            if l and r:
                return l.val == r.val and bfs(l.left, r.right) and bfs(l.right, r.left)
            else:
                return l == r
        return bfs(root.left, root.right) if root else True


# iteratively
from collections import deque
class Solution2(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        q = deque([(root.left, root.right)])
        while q:
            l, r = q.popleft()
            if l and r and l.val == r.val:  # neither is None
                q.extend([(l.right, r.left), (l.left, r.right)])
            elif l == r:  # both should be None if one is None
                continue
            else:  # val not same, or only one is None.
                return False
        return True
