"""
Time: O(n)
Space: O(n)


You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Brute-force DFS. Pre-order traversal.
# Time: O(nlg(n)), worst O(n^2)  Space: O(lg(n)), worst O(n)
class Solution:
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        res, stk = 0, []  # a stack to remember the path from root to current node

        def dfs(node, cumsum):
            nonlocal res, target
            if not node:
                return
            cumsum += node.val
            if cumsum == target:
                res += 1
            stk.append(node.val)
            t = cumsum
            for i in range(len(stk)-1):  # Not including the last one to avoid counting none-node case for target==0
                t -= stk[i]
                if t == target:
                    res += 1
            dfs(node.left, cumsum)
            dfs(node.right, cumsum)
            stk.pop()

        dfs(root, 0)
        return res


# Pre-order DFS with 2-sum hash table
# Time: O(n)  Space: O(n+lg(n))
from collections import defaultdict
class Solution2:
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        res, tbl = 0, defaultdict(int)
        tbl[0] = 1

        def dfs(node, cumsum):
            nonlocal res, tbl
            if not node:
                return
            cumsum += node.val
            res += tbl[cumsum - target]
            tbl[cumsum] += 1  # increament after updating result to avoid counting none-node case for target==0
            dfs(node.left, cumsum)
            dfs(node.right, cumsum)
            tbl[cumsum] -= 1

        dfs(root, 0)
        return res


# Same as solution 1 brute-force, but using recursion instead of nodes stack.
# Time: O(nlg(n)), worst O(n^2)  Space: O(lg(n)), worst O(n)
class Solution3:
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        return self.sumup(root, 0, target) + self.pathSum(root.left, target) + self.pathSum(root.right, target)

    def sumup(self, node, pre, target):
        if not node:
            return 0
        cur = pre + node.val
        return (cur == target) + self.sumup(node.left, cur, target) + self.sumup(node.right, cur, target)
