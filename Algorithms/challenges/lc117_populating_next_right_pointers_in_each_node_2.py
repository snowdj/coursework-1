"""
Time: O(n)
Space: O(1)

Follow up for problem "116. Populating Next Right Pointers in Each Node".

What if the given tree could be any binary tree? Would your previous solution still work?

Note:

You may only use constant extra space.
For example,
Given the following binary tree,
         1
       /  \
      2    3
     / \    \
    4   5    7
After calling your function, the tree should look like:
         1 -> NULL
       /  \
      2 -> 3 -> NULL
     / \    \
    4-> 5 -> 7 -> NULL
"""


# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        dummy = TreeLinkNode(0)
        p = dummy
        while root:
            if root.left:
                p.next = root.left
                p = p.next
            if root.right:
                p.next = root.right
                p = p.next
            root = root.next
            if root is None:
                p = dummy
                root = dummy.next  # move root to next level
                dummy.next = None
