#!/usr/bin/env python3
"""
Implementations of classic tree data structures:
Binary tree, binary search tree, AVL tree, red-black tree.

For practical implementations or use cases:
    1.  The practical use cases of Trees are mostly covered by maps and sets.
        Like other languages (e.g. C++), Python has no trees library.
    2.  collections.defaultdict can be used as trees. The disadvantages are:
        (1) Values can only be stored at leaves.
        (2) Hard to use tree manipulation algorithms.
        References:
        https://gist.github.com/hrldcpr/2012250
        http://connor-johnson.com/2015/02/28/generate-a-tree-structure-in-python/
    3.  3rd-party libraries
        (1) bintrees, SortedContainers
          http://kmike.ru/python-data-structures/
        (2) https://github.com/caesar0301/treelib
        (3) https://github.com/c0fec0de/anytree
"""


from random import sample
from collections import deque


def is_sortable(obj):
    """
    Check if an object is sortable in Python 3.
    Ref: https://stackoverflow.com/questions/19614260/check-if-an-object-is-order-able-in-python/  # noqa
    """
    cls = obj.__class__
    return cls.__lt__ != object.__lt__ or cls.__gt__ != object.__gt__


class BTNode:
    """
    Node class of linked binary tree.
    Inspired by DSAP code fragment 8.8.

    When creating a node, the key can be any data type. But when it is linked
    to a tree or another node, the nodes' class and their key types will be
    checked to be the same.
    """

    __slots__ = ('_key', '_parent', '_left', '_right')

    def __init__(self, key, parent=None, left=None, right=None):
        self._key = key
        self._parent = None
        self._left = None
        self._right = None
        self.parent = parent
        self.left = left
        self.right = right

    @property
    def key(self):
        return self._key

    @key.setter
    def key(self, k):
        self._key = k

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, node):
        if node is None:
            self._parent = None
        else:
            if not isinstance(node, self.__class__):
                raise TypeError("Parent type must be BTNode.")
            self._parent = node

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, node):
        if node is None:
            self._left = None
        else:
            if not isinstance(node, self.__class__):
                raise TypeError("Left child type must be BTNode.")
            self._left = node

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, node):
        if node is None:
            self._right = None
        else:
            if not isinstance(node, self.__class__):
                raise TypeError("Right child type must be BTNode.")
            self._right = node


class BinaryTree:
    """
    Generic linked binary tree.
    Inspired by DSAP code fragment 8.1, 8.7, 8.8-8.11, 8.16, 8.21.
    """

    _NIL = None  # Define NIL node as class variable.

    def __init__(self):
        self._root = self._NIL
        self._size = 0

    def __len__(self):
        return self._size

    @property
    def root(self):
        return self._root

    @root.setter
    def root(self, node):
        """
        Set root pointer to node.
        """
        if not isinstance(node, BTNode):
            raise TypeError("New root type must be BTNode.")
        self._root = node

    def add_left(self, x, e):
        """
        Add element e as the left child as node x.
        If x already has left child, raise ValueError.
        """
        if x.left is not self._NIL:
            raise ValueError('Left child exists.')
        y = BTNode(e, x, self._NIL, self._NIL)
        x.left = y
        self._size += 1

    def add_right(self, x, e):
        """
        Add element e as the right child as node x.
        If x already has right child, raise ValueError.
        """
        if x.right is not self._NIL:
            raise ValueError('Right child exists.')
        y = BTNode(e, x, self._NIL, self._NIL)
        x.right = y
        self._size += 1

    def sibling(self, node):
        """Return a node's sibling, or None if no sibling.
        """
        if node is self.root:
            return None
        parent = node.parent
        if node is parent.left:
            return parent.right
        else:
            return parent.left

    def children(self, x):
        """Return existing children of node x.
        """
        return (child for child in [x.left, x.right]
                if child is not self._NIL)

    def num_children(self, x):
        """Return the number of children (0, 1, or 2) of node x.
        """
        return len(list(self.children(x)))

    def is_root(self, node):
        return node is self.root

    def is_leaf(self, node):
        return self.num_children(node) == 0

    def is_empty(self):
        return len(self) == 0

    def inorder(self, node):
        """
        Generator for inorder traversal of a subtree.
        """
        if node.left is not self._NIL:  # has left subtree
            for x in self.inorder(node.left):
                yield x
        yield node
        if node.right is not self._NIL:  # has right subtree
            for x in self.inorder(node.right):
                yield x

    def inorder_iter(self, node):
        """
        Iterative inorder walk using a stack.
        """
        stack = []
        while stack or node is not self._NIL:
            if node is not self._NIL:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                yield node
                node = node.right

    def inorder_morris(self, node):
        """
        Morris inorder traversal using O(n) time and O(1) extra memory.
        http://www.geeksforgeeks.org/inorder-tree-traversal-without-recursion-and-without-stack/
        http://www.cnblogs.com/AnnieKim/archive/2013/06/15/MorrisTraversal.html
        https://en.wikipedia.org/wiki/Tree_traversal#Morris_in-order_traversal_using_threading
        """
        cur = node

        while cur is not self._NIL:
            if cur.left is self._NIL:  # cur reached the leftmost node
                yield cur
                cur = cur.right  # either walk to right subtree, or walk back to succssor by link
            else:
                pre = cur.left
                while pre.right not in (self._NIL, cur):
                    pre = pre.right
                if pre.right is self._NIL:
                    pre.right = cur  # Link predecessor of cur back to cur.
                    cur = cur.left  # Walk to left after linking predecessor.
                else:  # pre.right == cur, meaning walked back from predecessor by link
                    pre.right = self._NIL  # delete link and restore tree
                    yield cur
                    cur = cur.right

    def _inorder_walk(self):
        """
        Generator for inorder traversal of this tree.
        Yield NIL node for an empty tree.
        """
        for x in self.inorder(self.root):
            yield x

    def preorder_iter(self, node):
        """
        Iterative preorder traversal using a stack.
        http://www.geeksforgeeks.org/iterative-preorder-traversal/
        1) Create an empty stack nodeStack and push root node to stack.
        2) Do following while nodeStack is not empty.
        ….a) Pop an item from stack and print it.
        ….b) Push right child of popped item to stack
        ….c) Push left child of popped item to stack
        """
        stack = [] if node is self._NIL else [node]
        while stack:
            node = stack.pop()
            stack.extend([child for child in [node.right, node.left]
                          if child is not self._NIL])
            yield node

    def postorder_iter_twostacks(self, node):
        """
        Iterative postorder traversal using two stacks.
        http://www.geeksforgeeks.org/iterative-postorder-traversal/
        1. Push root to first stack.
        2. Loop while first stack is not empty
           2.1 Pop a node from first stack and push it to second stack
           2.2 Push left and right children of the popped node to first stack
        3. Print contents of second stack
        """
        stack1, stack2 = [], []
        if node is not self._NIL:
            stack1.append(node)
        while stack1:
            node = stack1.pop()
            stack2.append(node)  # push to stack2 by reversed postorder
            stack1.extend([child for child in [node.left, node.right]
                           if child is not self._NIL])
        while stack2:
            yield stack2.pop()

    def postorder_iter_onestack(self, node):
        """
        Iterative postorder traversal using one stack.
        """
        stack = []
        last = self._NIL  # last visited node
        while stack or node is not self._NIL:
            if node is not self._NIL:
                stack.append(node)
                node = node.left
            else:  # reached leftmost node's left NIL child
                node = stack[-1]  # back to leftmost node
                if node.right is self._NIL or last is node.right:
                    # no right child, or right child was visited last time
                    node = stack.pop()
                    yield node
                    last, node = node, self._NIL
                else:
                    node = node.right

    def __iter__(self):
        """
        Generate an iteration of tree nodes' element.
        """
        for x in self._inorder_walk():
            yield x.key

    def _height2(self, x):
        """
        Return the height of the subtree rooted at x.
        DSAP code fragment 8.5.
        """
        if self.is_leaf(x):
            return 0
        else:
            return 1 + max(self._height2(child) for child in self.children(x))

    def _height3(self, x):
        """
        Return the height of the subtree rooted at x.
        Define the height of a NIL node is -1 for easy rebalance.
        Ref: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/readings/binary-search-trees/avl.py  # noqa
        """
        if x is self._NIL:
            return -1
        else:
            return 1 + max(self._height3(x.left), self._height3(x.right))

    def height(self, x=None):
        """
        Return the height of the subtree rooted at x.
        If x is None, return the height of the entire tree.
        DSAP code fragment 8.6.
        """
        if x is None:
            x = self.root
        return self._height3(x)

    def breadth_first_walk(self, include_nil=False):
        """
        Generator for breadth-first traversal of this tree.
        Adapted from DSAP code fragment 8.20.

        :param include_nil: Switch if yielding NIL nodes, for printing purpose.
        """
        # A linked FIFO queue holding children of the next level
        # initialized to tree's root
        children_queue = deque([self.root])

        # Loop over all nodes, and enqueue the next-level children of each node
        while len(children_queue) != 0 \
                and any(x is not self._NIL for x in children_queue):
            x = children_queue.popleft()
            if x is self._NIL:
                children_queue.extend([self._NIL, self._NIL])
            else:
                children_queue.extend([x.left, x.right])
            if x is not self._NIL or include_nil:
                yield x

    def _get_node_str(self):
        """
        Generate a list of node strings for printing by breadth-first walk.
        """
        bf_walk = deque()
        for x in self.breadth_first_walk(include_nil=True):
            if x is self._NIL:  # Print space for NIL nodes
                bf_walk.append(' ')
            else:  # normal BTNode
                bf_walk.append(str(x.key))
        return bf_walk

    def __str__(self):
        """
        Print tree structure using breadth-first traversal, including NIL nodes
        """
        if self.is_empty():
            return "Empty tree."
        bf_walk = self._get_node_str()

        # Set node unit width to the max width of all nodes. Max is 5.
        node_max_width = max(len(x) for x in bf_walk)
        if node_max_width > 5:
            print("\nWarning! Node is too long to print correctly.\n")
        unit_width = min(node_max_width, 5)

        # Obtain tree height to calculate the width of leaf level, as well as
        # tree's center position (root's position) for printing.
        h = self.height()

        # Leaf-level width is 2^h x leaf_node_width
        # leaf_width = 2**h * (unit_width + 1)
        leaf_width = (2**h + 2**h-1) * unit_width

        # root position in the first line.
        center_pos = [int((leaf_width + 1) / 2) + unit_width]

        # Make string for root
        tree_str = ' ' * (center_pos[0] - 1)
        x = bf_walk.popleft()
        x_str = '{:{width}}'.format(x, width=unit_width)
        tree_str += x_str
        tree_str += ' <-- root\n'

        # Append strings for other nodes
        for level in range(1, h+1):
            # Compute center node positions of current level
            cp_shift = max(int(leaf_width/2**(level+1)), 1)
            center_pos = [(cp-cp_shift, cp+cp_shift) for cp in center_pos]

            # Add edges for current level
            cursor = 1
            for cp_pair in center_pos:
                tree_str += (cp_pair[0] - cursor) * ' '
                tree_str += '/'
                cursor = cp_pair[0] + 1
                tree_str += (cp_pair[1] - cursor) * ' '
                tree_str += '\\'
                cursor = cp_pair[1] + 1
            tree_str += '\n'

            # Add nodes for each level
            center_pos = [c for cp in center_pos for c in cp]
            cursor = 1
            x_str_excess_width = 0
            for cp in center_pos:
                try:
                    x = bf_walk.popleft()
                    x_str = '{:{width}}'.format(x, width=unit_width)
                    tree_str += (cp - cursor - x_str_excess_width) * ' '
                    tree_str += x_str
                    x_str_excess_width = len(x_str) - 1
                    cursor = cp + 1
                except IndexError:  # bf_walk has no more node to print
                    break
            tree_str += '\n'

        return tree_str


class BinarySearchTree(BinaryTree):
    """
    Base class of binary search tree without rebalance.

    Implementations of BST algorithms in CLRS 3ed chap 12.
    """

    _NIL = BTNode(None, None, None, None)

    def __init__(self):
        super(BinarySearchTree, self).__init__()

    def tree_search(self, k, x=None):
        """
        Search the node with key=k in the subtree rooted at node x.
        If k is not found, return None (virtual leaf).
        CLRS 3ed page 291.
        """
        if x is None:  # search the whole tree starting from root.
            x = self.root

        # Walk down the tree by comparing keys.
        while x is not self._NIL and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x

    def tree_minimum(self, x=None):
        """
        Find the node with minimum key in the subtree rooted at node x.
        CLRS 3ed page 291.
        """
        if x is None:  # search the whole tree starting from root.
            x = self.root

        # Walk down through the left subtree until leaf.
        # x.left.key=None means T.NIL in RB-tree
        while x.left is not self._NIL:
            x = x.left
        return x

    def tree_maximum(self, x=None):
        """
        Find the node with maximum key in the subtree rooted at node x.
        CLRS 3ed page 291.
        """
        if x is None:  # search the whole tree starting from root.
            x = self.root

        # Walk down through the right subtree until leaf.
        # x.right.key=None means T.NIL in RB-tree
        while x.right is not self._NIL:
            x = x.right
        return x

    def tree_successor(self, x=None):
        """
        Find the successor of the given node x in the BST.
        Return None if node x has the largest key in the tree.
        CLRS 3ed page 292.
        """
        if x is None:  # search the whole tree starting from root.
            x = self.root

        if x.right is not self._NIL:  # Node x has right subtree.
            return self.tree_minimum(x.right)

        # Node x has no right subtree. The successor is the lowest ancestor of
        # the given node x whose left child is also an ancestor of node x.
        y = x.parent  # cover the case x is tree's only node. Return None.
        while y is not self._NIL and x is y.right:
            x = y
            y = y.parent
        return y

    def tree_predecessor(self, x=None):
        """
        Find the predecessor of the given node x in the BST.
        Return None if node x has the smallest key in the tree.
        CLRS 3ed page 293, exercise 12.2-3..
        """
        if x is None:  # search the whole tree starting from root.
            x = self.root

        if x.left is not self._NIL:  # node has left subtree.
            return self.tree_maximum(x.left)

        # Node z has no right subtree. The successor is the lowest ancestor of
        # node z whose right child is also an ancestor of node z.
        y = x.parent  # cover the case x is tree's only node. Return None.
        while y is not self._NIL and x is y.left:
            x = y
            y = y.parent
        return y

    def _insert_node(self, z):
        """
        Insert node z into BST and maintain BST property.
        CLRS 3ed page 294.
        :param z: The node to be inserted.
        """
        # y is the parent of the target insertion position. Initialized to
        # self.root.parent to cover the case of empty tree.
        y = self._NIL
        # x is walk node and reaches the target position at the end of loop.
        x = self.root

        # Search for the appropriate position to maintain BST property.
        while x is not self._NIL:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y

        # Link parent's child to z.
        if y is self._NIL:  # empty tree
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

        # update tree size
        self._size += 1

    def tree_insert(self, k):
        """
        Make a BTNode for key k and insert it into BST.
        :param k: The key to be inserted.
        """
        # z.key = k, z.parent = z.left = z.right = NIL
        z = BTNode(k, parent=self._NIL, left=self._NIL, right=self._NIL)
        self._insert_node(z)
        return z

    def _transplant(self, u, v):
        """
        Replace the subtree rooted at node u with the subtree rooted at v.
        CLRS 3ed page 296.
        """
        if self.root is u:
            self.root = v
        elif u is u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not self._NIL:
            v.parent = u.parent

    def tree_delete(self, z):
        """
        Delete node z from BST.
        CLRS 3ed page 298.
        """
        # Record action position for AVLTree rebalance.
        # See http://www.mathcs.emory.edu/~cheung/Courses/323/Syllabus/Trees/AVL-delete.html  # noqa
        action_pos = z.parent

        if z.left is self._NIL:
            # case (a): z has only right subtree, or no child at all.
            self._transplant(z, z.right)
        elif z.right is self._NIL:
            # case (b): z has only left subtree.
            self._transplant(z, z.left)
        else:  # case(c) and (d): z has both children.
            # Find z's successor y.
            # Note: y must have no left child, otherwise it won't be
            # z's successor.
            y = self.tree_minimum(z.right)

            # Action position changed to y's parent.
            action_pos = y.parent

            # case (d): z's successor is not z's right child r.
            if y.parent is not z:
                # (d-1) Replace y by its own right subtree.
                self._transplant(y, y.right)
                # (d-2) Link r as y's right child.
                y.right = z.right
                y.right.parent = y

            # case (c): z's successor is z's right child.
            # (d-3) Link z's parent as y's parent.
            self._transplant(z, y)
            # (d-4) Link z's left child as y's left child.
            y.left = z.left
            y.left.parent = y

        self._size -= 1
        del z  # Remove z from memory.
        return action_pos  # for AVLTree rebalance

    def randomly_build(self, s):
        """
        Randomly permute input sequence s, and then make BTNode for each
        element and insert into BST.
        CLRS 3ed chap 12.4.

        :param s: An iterable with elements of the same comparable data type.
        """

        # check if elements of s have the same data type and if sortable
        if not all(isinstance(x, s[0].__class__) for x in s):
            raise TypeError('All elements in s must be the same type.')
        if not is_sortable(s[0]):
            raise TypeError('Elements of s must have sortable data type.')

        # Randomly permute s
        s_perm = sample(s, k=len(s))

        # Insert permuted s into BST.
        for e in s_perm:
            self.tree_insert(e)


class AVLTree(BinarySearchTree):
    """
    AVL balanced binary search tree.
    Reference: MIT OCW 6.006 2011 Lecture 6.
    Video: https://www.youtube.com/watch?v=FNeL18KsWPc
      Re-balance algorithm: 29:50 - 48:33
      AVL Sort vs Heap Sort: 48:33 - End
    Code: https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/readings/binary-search-trees/  # noqa
    """
    def __init__(self):
        super(AVLTree, self).__init__()

    def _left_rotate(self, x):
        """
        Modified from LEFT-ROTATE in CLRS 3ed chapter 13.2, page 313.
        """
        if x.right is self._NIL:
            return
        y = x.right

        # Move y's left subtree to be x's right subtree,
        # resulting y and y's subtree are half-disconnected from tree.
        x.right = y.left
        if y.left is not self._NIL:
            y.left.parent = x

        # Link x's parent to y, resulting x is disconnected from tree.
        y.parent = x.parent
        if x.parent is self._NIL:  # x was root
            self.root = y
        elif x is x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        # Re-link x to tree as y's left
        y.left = x
        x.parent = y

    def _right_rotate(self, y):
        """
        RIGHT-ROTATE mirrors LEFT-ROTATE.
        """
        if y.left is self._NIL:
            return
        x = y.left

        # Move x's right subtree to be y's left subtree,
        # resulting x and x's subtree are half-disconnected from tree.
        y.left = x.right
        if x.right is not self._NIL:
            x.right.parent = y

        # Link y's parent to x, resulting y is disconnected from tree.
        x.parent = y.parent
        if y.parent is self._NIL:  # y was root
            self.root = x
        elif y is y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x

        # Re-link y to tree as x's right
        x.right = y
        y.parent = x

    def _rebalance(self, x):
        """
        Check children height balance from node x up to root. If unbalance is
        found, rebalance and then keep checking until reaching root's parent.
        """
        while x is not self._NIL:  # loop until x is root's parent
            if self.height(x.left) > self.height(x.right) + 1:  # left heavy
                if self.height(x.left.left) >= self.height(x.left.right):
                    # straight line case
                    self._right_rotate(x)  # single rotation.
                else:  # zig-zag case. Double rotations.
                    self._left_rotate(x.left)
                    self._right_rotate(x)
            elif self.height(x.right) > self.height(x.left) + 1:  # right heavy
                if self.height(x.right.right) >= self.height(x.right.left):
                    # straight line case
                    self._left_rotate(x)  # single rotation.
                else:  # zig-zag case. Double rotations.
                    self._right_rotate(x.right)
                    self._left_rotate(x)
            else:  # children are balanced. Good!
                pass
            # Children height balance achieved at x. Now move up.
            x = x.parent

    def tree_insert(self, k):
        """
        Insert key k into AVL BST and restore balance property.
        :param k: The key to be inserted.
        """
        z = super(AVLTree, self).tree_insert(k)
        self._rebalance(z)

    def tree_delete(self, z):
        """
        Delete node z from AVL BST and restore balance property.
        http://www.mathcs.emory.edu/~cheung/Courses/323/Syllabus/Trees/AVL-delete.html
        :param z: The node to be deleted.
        """
        action_pos = super(AVLTree, self).tree_delete(z)
        self._rebalance(action_pos)


class RedBlackNode(BTNode):
    """
    Node class of Red-Black balanced BST.
    """
    __slots__ = ('_black',)

    def __init__(self, key, parent=None, left=None, right=None, black=False):
        self._black = None
        super(RedBlackNode, self).__init__(key, parent, left, right)
        self.black = black  # False - 'Red', True - 'Black'

    @property
    def black(self):
        return self._black

    @black.setter
    def black(self, c):
        if isinstance(c, bool):
            self._black = c


class RedBlackTree(BinarySearchTree):
    """
    Red-Black balanced binary search tree.
    Reference: MIT OCW 6.046J Fall 2005, Lec 10, by Erik Demaine.
    Video: https://www.youtube.com/watch?v=O3hI9FdxFOM
    Insertion: Starting from 40m:40s.
    """
    def __init__(self):
        super(RedBlackTree, self).__init__()
        self._NIL = RedBlackNode(key=None, black=True)  # T.NIL
        self.root = self._NIL  # Init root to T.NIL instead of None.

    def _get_node_str(self):
        """
        Override the method in BinaryTree to incorporate T.NIL.
        """
        bf_walk = deque()
        for x in self.breadth_first_walk(include_nil=True):
            if x is self._NIL:  # Print space for NIL nodes
                bf_walk.append(' ')
            elif not x.black:  # append * to red nodes
                bf_walk.append(str(x.key) + '*')
            else:  # black nodes
                bf_walk.append(str(x.key))
        return bf_walk

    def _left_rotate(self, x):
        """
        LEFT-ROTATE in CLRS 3ed chapter 13.2, page 313.
        Override _left_rotate in base class.
        """
        y = x.right

        # Move y's left subtree to be x's right subtree,
        # resulting y and y's subtree are half-disconnected from tree.
        x.right = y.left
        if y.left is not self._NIL:
            y.left.parent = x

        # Link x's parent to y, resulting x is disconnected from tree.
        y.parent = x.parent
        if x.parent is self._NIL:  # x was root
            self.root = y
        elif x is x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        # Re-link x to tree as y's left
        y.left = x
        x.parent = y

    def _right_rotate(self, y):
        """
        RIGHT-ROTATE mirrors LEFT-ROTATE.
        Override _right_rotate in base class.
        """
        x = y.left

        # Move x's right subtree to be y's left subtree,
        # resulting x and x's subtree are half-disconnected from tree.
        y.left = x.right
        if x.right is not self._NIL:
            x.right.parent = y

        # Link y's parent to x, resulting y is disconnected from tree.
        x.parent = y.parent
        if y.parent is self._NIL:  # y was root
            self.root = x
        elif y is y.parent.left:
            y.parent.left = x
        else:
            y.parent.right = x

        # Re-link y to tree as x's right
        x.right = y
        y.parent = x

    def _insert_node(self, z):
        """
        Override _insert_node() method in base class to incorporate T.NIL.
        CLRS 3ed page 315, RB-INSERT(T, z).
        """
        # y is the parent of the target insertion position. Initialized to
        # self.root.parent to cover the case of empty tree.
        y = self._NIL
        # x is walk node and reaches the target position at the end of loop.
        x = self.root

        # Search for the appropriate position to maintain BST property.
        while x is not self._NIL:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.parent = y

        # Link parent's child to z.
        if y is self._NIL:  # empty tree
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

        # Set z's children to T.NIL and color z to Red.
        z.left = self._NIL
        z.right = self._NIL
        z.black = False

        # update tree size
        self._size += 1

    def _rb_insert_fixup(self, z):
        """
        Fix red-black tree property 4 and 2, from node z up to root.
        CLRS 3ed page 316.
        """
        while not z.parent.black:  # Parent is Red. Need to fix property.4
            if z.parent is z.parent.parent.left:
                # Case A: parent is left child of grandparent
                uncle = z.parent.parent.right
                if not uncle.black:  # Case 1: Red uncle
                    z.parent.black = True  # recolor parent to Black
                    uncle.black = True  # recolor uncle to Black
                    z.parent.parent.black = False  # recolor grandparent to Red
                    z = z.parent.parent  # move up z to grandparent
                else:  # Case 2 & 3: Black uncle
                    if z is z.parent.right:
                        # Case 2: parent and grandparent are zig-zag.
                        z = z.parent  # move up z to parent
                        self._left_rotate(z)  # rotate at parent
                    # Case 2 continue, and Case 3:
                    # parent and grandparent are in a line.
                    z.parent.black = True  # recolor parent to Black
                    z.parent.parent.black = False  # recolor grandparent to Red
                    self._right_rotate(z.parent.parent)
            else:  # Case B: parent is right child of grandparent
                uncle = z.parent.parent.left
                if not uncle.black:  # Case 1: Red uncle
                    z.parent.black = True  # recolor parent to Black
                    uncle.black = True  # recolor uncle to Black
                    z.parent.parent.black = False  # recolor grandparent to Red
                    z = z.parent.parent  # move up z to grandparent
                else:  # Case 2 & 3: Black uncle
                    if z is z.parent.left:
                        # Case 3: parent and grandparent are zig-zag.
                        z = z.parent  # move up z to parent
                        self._right_rotate(z)  # rotate at parent
                    # Case 2 continue, and Case 3:
                    # parent and grandparent are in a line.
                    z.parent.black = True  # recolor parent to Black
                    z.parent.parent.black = False  # recolor grandparent to Red
                    self._left_rotate(z.parent.parent)
        self.root.black = True  # Fix property 2.

    def tree_insert(self, k):
        """
        Make a RedBlackNode for key k and insert it into RedBlackTree.
        :param k: The key to be inserted.
        """
        # z.key = k, z.parent = z.left = z.right = None, z.black = False
        z = RedBlackNode(k, black=False)
        self._insert_node(z)
        self._rb_insert_fixup(z)

    def _transplant(self, u, v):
        """
        Override _transplant() method in base class to incorporate T.NIL.
        CLRS 3ed page 323, RB-TRANSPLANT(T, u, v).
        """
        if self.root is u:
            self.root = v
        elif u is u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent  # Do this even if v is T.NIL.

    def _rb_delete_fixup(self, x):
        """
        Fix red-black property after delete a node.
        CLRS 3ed page 326.

        :param x: x is always the doubly-black node inside the while loop.
                  If x is red, the last line simply colors it to black to
                  fix property 4 (red children are black) and 5 (black height).
        """
        while not self.is_root(x) and x.black:  # x is doubly-black
            if x is x.parent.left:
                # x's sibling was y's original sibling in RB-DELETE(T,z)
                sibling = x.parent.right

                # Case 1: Red sibling. Black-height difference = 2.
                # Transform to Case 2,3,4.
                if not sibling.black:
                    sibling.black = True
                    x.parent.black = False
                    self._left_rotate(x.parent)
                    sibling = x.parent.right

                # Case 2: Black sibling, and both children black.
                # Black-height difference = 1. Similar as INSERT-FIXUP Case 1.
                # If x.parent was originally black, move up doubly-black node x
                # If x.parent was originally red (transformed from case 1),
                # loop will be terminated, and color x.parent to black.
                if sibling.left.black and sibling.right.black:
                    sibling.black = False
                    x = x.parent

                # Case 3: Black sibling, and its left child is red.
                # Black-height difference = 1, but sibling and its red child
                # are zig-zag, similar as INSERT-FIXUP Case 2.
                # Transform to Case 4. Swap color of sibling and its red child,
                # and right-rotate.
                else:
                    if sibling.right.black:  # sibling.left is red
                        sibling.left.black = True
                        sibling.black = False
                        self._right_rotate(sibling)
                        sibling = x.parent.right

                    # Case 4: Black sibling, and its right child is red.
                    # Black-height difference = 1, and sibling and its red
                    # child are in a line, similar as INSERT-FIXUP Case 3.
                    # Recolor sibling, red child and parent, and left-rotate.
                    # Set x to root to manually terminate the loop.
                    sibling.black = x.parent.black
                    sibling.parent.black = True
                    sibling.right.black = True
                    self._left_rotate(x.parent)
                    x = self.root

            else:  # symmetric case
                sibling = x.parent.left
                if not sibling.black:
                    sibling.black = True
                    x.parent.black = False
                    self._right_rotate(x.parent)
                    sibling = x.parent.left
                if sibling.left.black and sibling.right.black:
                    sibling.black = False
                    x = x.parent
                else:
                    if sibling.left.black:  # sibling.right is red
                        sibling.right.black = True
                        sibling.black = False
                        self._left_rotate(sibling)
                        sibling = x.parent.left
                    sibling.black = x.parent.black
                    sibling.parent.black = True
                    sibling.left.black = True
                    self._right_rotate(x.parent)
                    x = self.root

        # x was red-black, and color it to black to fix property 4 and 5.
        x.black = True

    def tree_delete(self, z):
        """
        Delete node z from red-black tree.
        CLRS 3ed page 324, RB-DELETE(T, z).
        """
        y = z
        y_original_color = y.black
        if z.left is self._NIL:  # case (a): z has only right subtree.
            x = z.right
            self._transplant(z, z.right)
        elif z.right is self._NIL:  # case (b): z has only left subtree.
            x = z.left
            self._transplant(z, z.left)
        else:  # case(c) and (d): z has both children.
            # Find z's successor y.
            # Note: y must have no left child, otherwise it won't be
            # z's successor.
            y = self.tree_minimum(z.right)
            y_original_color = y.black
            x = y.right
            if y.parent is z:
                x.parent = y
            else:  # case (d): z's successor is not z's right child r
                # (d-1) Replace y by its own right subtree.
                self._transplant(y, y.right)
                # (d-2) Link r as y's right child.
                y.right = z.right
                y.right.parent = y
            # case (c): z's successor is z's right child.
            # (d-3) Link z's parent as y's parent.
            self._transplant(z, y)
            # (d-4) Link z's left child as y's left child.
            y.left = z.left
            y.left.parent = y
            y.black = z.black
        if y_original_color:  # Black
            self._rb_delete_fixup(x)

        self._size -= 1
        del z  # Remove z from memory.


def test_bt():
    """
    Test BinaryTree class.
    """
    bt = BinaryTree()
    bt.root = BTNode(15)
    bt.add_left(bt.root, 6)
    n6 = bt.root.left
    bt.add_right(bt.root, 18)
    n18 = bt.root.right
    bt.add_left(n6, 3)
    n3 = n6.left
    bt.add_right(n6, 7)
    n7 = n6.right
    bt.add_left(n3, 2)
    bt.add_right(n3, 4)
    bt.add_right(n7, 13)
    bt.add_left(n7.right, 9)
    bt.add_left(n18, 17)
    bt.add_right(n18, 20)

    print("\nRecursive inorder traversal:")
    for x_key in bt:
        print(x_key)

    print("\nIterative inorder traversal:")
    for node in bt.inorder_iter(bt.root):
        print(node.key)

    print("\nMorris inorder traversal:")
    for node in bt.inorder_morris(bt.root):
        print(node.key)

    print("\nIterative preorder traversal:")
    for node in bt.preorder_iter(bt.root):
        print(node.key)

    print("\nIterative postorder traversal using two stacks:")
    for node in bt.postorder_iter_twostacks(bt.root):
        print(node.key)

    print("\nIterative postorder traversal using one stack:")
    for node in bt.postorder_iter_onestack(bt.root):
        print(node.key)

    print("\nBreadth-first traversal:")
    for x in bt.breadth_first_walk():
        print(x.key)

    print("\n\nTree Structure:")
    print(bt)

    print('Tree size = ', len(bt))
    print('Tree height = ', bt.height())

    print('Is Node 7 a leaf?', bt.is_leaf(n7))
    print('Is Node 4 a leaf?', bt.is_leaf(n3.right))


def test_bst(tree_type):
    """
    Test BinarySearchTree, AVLTree, RedBlackTree.
    """
    if tree_type.upper() == 'BST':
        bst = BinarySearchTree()
    elif tree_type.upper() == 'AVL':
        bst = AVLTree()
    elif tree_type.upper() == 'REDBLACK':
        bst = RedBlackTree()
    else:
        return

    # Randomly building BST
    s = sample(range(101), 12)
    print("Randomly building tree from: {}".format(s))
    bst.randomly_build(s)
    print(bst)

    # in-order walk
    print('\nInorder traversal:')
    keys = [x_key for x_key in bst]
    print(keys)

    # 3 random queries
    for k in sample(keys, 3):
        node_k = bst.tree_search(k)
        print('Search {}: found {}'.format(k, node_k.key))
        print('Search min. in subtree of {}: found {}'.format(
            k, bst.tree_minimum(node_k).key))
        print('Search max. in subtree of {}: found {}'.format(
            k, bst.tree_maximum(node_k).key))
        try:
            print('Search predecessor of {}: found {}'.format(
                k, bst.tree_predecessor(node_k).key))
        except AttributeError:
            print('Search predecessor of {}: found None'.format(k))
        try:
            print('Search successor of {}: found {}'.format(
                k, bst.tree_successor(node_k).key))
        except AttributeError:
            print('Search successor of {}: found None'.format(k))

    # insert 3 new unique keys
    while True:
        k_ins = sample(range(121), 3)
        if all(k not in s for k in k_ins):
            break
    print('\nTree size = ', len(bst))
    print('Insert: ', k_ins)
    for k in k_ins:
        bst.tree_insert(k)
    print(bst)
    print('\nTree size = ', len(bst))

    # delete 3 keys
    k_del = sample(s + k_ins, 3)
    print('\nTree size = ', len(bst))
    print('Delete: ', k_del)
    for k in k_del:
        bst.tree_delete(bst.tree_search(k))
    print(bst)
    print('\nTree size = ', len(bst))


def test_trees(tree_type):
    """
    Test tree classes.
    :param tree_type: BT, BST, AVL, REDBLACK:
    """
    if tree_type.upper() == 'BT':
        test_bt()
    elif tree_type.upper() in ['BST', 'AVL', 'REDBLACK']:
        test_bst(tree_type)
    else:
        raise NotImplemented


if __name__ == '__main__':
    import sys
    if len(sys.argv) <= 1:
        print('Available test cases are: BT, BST, AVL, or REDBLACK.')
    else:
        try:
            test_trees(sys.argv[1])
        except NotImplementedError:
            print("Test case \"{}\" is not supported.".format(sys.argv[1]))
