"""
Time: O(lg(n))
Space: O(1)

Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
"""


# recursive
def closestValue(self, root, target):
    a = root.val
    kid = root.left if target < a else root.right
    if not kid:
        return a
    b = self.closestValue(kid, target)
    return a if abs(a - target) < abs(b - target) else b


# iterative
def closestValue2(self, root, target):
    closest = root.val
    while root:
        closest = min((root.val, closest), key=lambda x: abs(target - x))
        root = root.left if target < root.val else root.right
    return closest
