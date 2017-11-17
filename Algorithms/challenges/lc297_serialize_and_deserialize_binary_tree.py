"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to the original tree structure.

For example, you may serialize the following tree

    1
   / \
  2   3
     / \
    4   5
as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a binary tree. You do not necessarily need to follow this format, so please be creative and come up with different approaches yourself.
Note: Do not use class member/global/static variables to store states. Your serialize and deserialize algorithms should be stateless.
"""

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# preorder traversal
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def preorder(node):
            if node:
                data.append(str(node.val))
                preorder(node.left)
                preorder(node.right)
            else:
                data.append('#')
        data = []
        preorder(root)
        return ' '.join(data)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        def preorder():
            val = next(tree)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = preorder()
            node.right = preorder()
            return node
        tree = iter(data.split())
        return preorder()


# level-order traversal
class Codec2:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '[]'
        res = [root.val]
        q = collections.deque([root])
        while q:
            front = q.popleft()
            if front.left:
                q.append(front.left)
            if front.right:
                q.append(front.right)
            res.append(front.left.val if front.left else 'null')
            res.append(front.right.val if front.right else 'null')
        while res and res[-1] == 'null':
            res.pop()
        return '[' + ','.join(map(str, res)) + ']'

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '[]':
            return None
        nodes = collections.deque([[TreeNode(o), None][o == 'null']
                                    for o in data[1:-1].split(',')])
        q = collections.deque([nodes.popleft()]) if nodes else None
        root = q[0] if q else None
        while q:
            parent = q.popleft()
            left = nodes.popleft() if nodes else None
            right = nodes.popleft() if nodes else None
            parent.left, parent.right = left, right
            if left:
                q.append(left)
            if right:
                q.append(right)
        return root


# json + tuple
# https://discuss.leetcode.com/topic/28059/tuplify-json-python
import json
class Codec3:

    def serialize(self, root):
        def tuplify(root):
            return root and (root.val, tuplify(root.left), tuplify(root.right))
        return json.dumps(tuplify(root))

    def deserialize(self, data):
        def detuplify(t):
            if t:
                root = TreeNode(t[0])
                root.left = detuplify(t[1])
                root.right = detuplify(t[2])
                return root
        return detuplify(json.loads(data))
