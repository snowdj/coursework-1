"""Submission for CS61A Homework 8.

Name:
Login:
Collaborators:
"""

# Copied from lecture.  

class Tree:
    """A Tree consists of a label and a sequence of 0 or more
    Trees, called its children."""

    def __init__(self, label, *children):
        """A Tree with given label and children.  For convenience,
        if children[k] is not a Tree, it is converted into a leaf
        whose operator is children[k]."""
        self.__label = label;
        self.__children = \
          [ c if type(c) is Tree else Tree(c) for c in children]

    @property
    def is_leaf(self):
        return self.arity == 0

    @property
    def label(self):
        return self.__label

    @property
    def arity(self):
        return len(self.__children)

    def __getitem__(self, k):
        return self.__children[k]

    def __iter__(self):
        return iter(self.__children)

    def __repr__(self):
        if self.is_leaf:
            return "Tree({0})".format(self.label)
        else:
            return "Tree({0}, {1})" \
               .format(self.label, str(self.__children)[1:-1])


# Q1.

from random import Random
from math import sqrt

def make_binary_tree(L, randoms = Random()):
    """Returns a binary tree, T, such that the labels of T in inorder (i.e.,
    keys in left child of T, followed by the label of T, followed
    by keys in the right child of T) are L.  The structure of the tree
    (which nodes are children of which) is determined randomly according to
    RANDOMS, an instance of Random.  An empty tree is represented as a
    Tree with a label of None."""
    if len(L) == 0:
        return Tree(None)
    else:
        left = randoms.randint(0, len(L)-1)
        return Tree(L[left], make_binary_tree(L[0:left], randoms),
                    make_binary_tree(L[left+1:], randoms))
    
PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
          59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113,
          127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181,
          191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251,
          257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317,
          331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397,
          401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463,
          467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557,
          563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619,
          631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701,
          709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787,
          797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863,
          877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953,
          967, 971, 977, 983, 991, 997 )


PRIME_BINARY_TREE = make_binary_tree(PRIMES)

# Implement the following non-recursively:

def tree_find(T, x):
    """True iff x is a label in set T, represented as a search tree.
    That is, T 
       (a) Represents an empty tree if its label is None, or
       (b) has two children, both search trees, and all labels in 
           T[0] are less than T.label, and all labels in T[1] are 
           greater than T.label.
    >>> tree_find(PRIME_BINARY_TREE, 5)
    True
    >>> tree_find(PRIME_BINARY_TREE, 0)
    False
    >>> tree_find(PRIME_BINARY_TREE, 27)
    False
    >>> tree_find(PRIME_BINARY_TREE, 929)
    True
    >>> tree_find(PRIME_BINARY_TREE, 989)
    False
    """
    "*** YOUR CODE HERE ***"

    #--- Recursively: ---#
    # if T.label is None:
    #     return False
    # else:
    #     return x == T.label \
    #            or (x < T.label and tree_find(T[0], x)) \
    #            or (x > T.label and tree_find(T[1], x))

    #--- Iteratively: ---#
    T1 = T
    while T1.label is not None:
        if x == T1.label:
            return True
        elif x < T1.label:
            T1 = T1[0]
        else:
            T1 = T1[1]
    return False
            

# Q2.
def depth(T, x):
    """The depth, in any, at which x appears as a label in T.  Returns
    None if x is not in T.
    >>> T = Tree(1, Tree(3, Tree(4, 5, 6)))
    >>> depth(T, 1)
    0
    >>> depth(T, 5)
    3
    >>> depth(T, 10)   # Result is None
    """
    "*** YOUR CODE HERE ***"
    dep = 0

    def tree_find(T, x, update_dep=False):
        nonlocal dep
        if update_dep:
            dep += 1

        if x == T.label:
            return True
        elif T.label is None or T.arity == 0:
            return False
        elif T.arity == 1:
            return tree_find(T[0], x, True)
        else:  # T.arity > 1
            return tree_find(T[0], x, True) \
                or any(map(tree_find, T[1:], (x,)*(T.arity-1)))

    if not tree_find(T, x):
        return None
    else:
        return dep
    

# Q3.

# Define a "general search tree" to be one whose labels are lists of keys
# such that

#  a. A node whose label is None represents an empty collection.
#  b. Otherwise, there is at least one key in a node label and
#     the keys are sorted in ascending order.
#  c. A non-empty node with *N* keys has *N+1* children, which are
#     also general search trees.
#  d. If x is key #k in a node's label, then all keys in child #k are 
#     less than x and all those in child #k+1 are greater than x.

def make_general_tree(L, randoms = Random()):
    """Returns a general search tree, T, containing the labels of L, assuming
    it is ordered.  The numbers of keys in each and subtree is decided
    randomly according to RANDOMS, an instance of random.Random."""
    if len(L) == 0:
        return Tree(None)
    else:
        arity = randoms.randint(1, int(sqrt(len(L))))
        key_indices = randoms.sample(range(0, len(L)), arity)
        key_indices.sort()
        keys = [ L[i] for i in key_indices ]
        children = [make_general_tree(L[0:key_indices[0]], randoms)] \
                   + [ make_general_tree(L[key_indices[i]+1:key_indices[i+1]],
                                         randoms)
                       for i in range(0, len(key_indices)-1) ] \
                   + [make_general_tree(L[key_indices[-1]+1:], randoms)]
        return Tree(keys, *children)

PRIME_GENERAL_TREE = make_general_tree(PRIMES)


def gen_tree_find(T, x):
    """True iff x is a label in set T, represented as a general
    search tree.
    >>> gen_tree_find(PRIME_GENERAL_TREE, 5)
    True
    >>> gen_tree_find(PRIME_GENERAL_TREE, 0)
    False
    >>> gen_tree_find(PRIME_GENERAL_TREE, 27)
    False
    >>> gen_tree_find(PRIME_GENERAL_TREE, 929)
    True
    >>> gen_tree_find(PRIME_GENERAL_TREE, 989)
    False
    """
    # (non-recursive version)
    "*** YOUR CODE HERE ***"
    T1 = T
    while T1.label is not None:
        if x in T1.label:
            return True
        elif x > T1.label[-1]:
            T1 = T1[-1]
        else:
            for i in range(len(T1.label)):
                if x < T1.label[i]:
                    T1 = T1[i]
                    break
    return False
            

## use bisect.bisect_left() to find the child for next-loop
import bisect
def gen_tree_find_bisect(T, x):
    """True iff x is a label in set T, represented as a general
    search tree.
    >>> gen_tree_find(PRIME_GENERAL_TREE, 5)
    True
    >>> gen_tree_find(PRIME_GENERAL_TREE, 0)
    False
    >>> gen_tree_find(PRIME_GENERAL_TREE, 27)
    False
    >>> gen_tree_find(PRIME_GENERAL_TREE, 929)
    True
    >>> gen_tree_find(PRIME_GENERAL_TREE, 989)
    False
    """
    # (non-recursive version)
    "*** YOUR CODE HERE ***"
    T1 = T
    while T1.label is not None:
        if x in T1.label:
            return True
        else:
            T1 = T1[bisect.bisect_left(T1.label, x)]
    return False


# Q4.

def memoize(func):
    """Returns a function that takes the same arguments as 'func'
    and returns the same value, but with memoization.  That is, if
    f is the function returned by memoize(func), then f(v) returns
    func(v), but if f is called twice with the same arguments, v, it
    does not call func(v), but returns the previously returned value.
    We assume that 'func' is a pure function whose value depends only
    on the values of its arguments, and whose side-effects are irrelevant,
    and that the values of its argument, v, are of a type suitable for
    use as keys in a Python dictionary."""
    "*** YOUR CODE HERE ***"

# Q5.

def checked_memoize(func):
    """Returns a function that takes the same arguments as 'func'
    and returns the same value, but with memoization.  That is, if
    f is the function returned by memoize(func), then f(v) returns
    func(v), but if f is called twice with the same arguments, v, it
    does not call func(v), but returns the previously returned value.
    We assume that 'func' is a pure function whose value depends only
    on the values of its arguments, and whose side-effects are irrelevant,
    and that the values of its argument, v, are of a type suitable for
    use as keys in a Python dictionary.  Raises a RuntimeError if a
    value of the arguments is encountered during the computation of the
    value of the function on those arguments."""
    "*** YOUR CODE HERE ***"

# Q6.

empty_set = Tree(None)

def is_empty(T):
    return T.label is None

def adjoin_set(S, v):
    """Assuming S is a binary search tree representing a set (no
    duplicate values), the binary search tree representing the set
    S U {v}."""
    if S.label is None:
        return Tree(v, None, None)
    elif v < S.label:
        return Tree(S.label, adjoin_set(S[0], v), S[1])
    elif v == S.label:
        return S
    else:
        return Tree(S.label, S[0], adjoin_set(S[1], v))	

def adjoin_all(S, L):
    """The result of adding all the elements of L to set S, in order."""
    for v in L:
        S = adjoin_set(S, v)
    return S

def bad(N):
    "*** YOUR CODE HERE ***"

def good(N):
    "*** YOUR CODE HERE ***"

# Q7. [Extra for experts]

def inorder_labels(T):
    """The non-null labels in T in inorder (labels in the left child,
    then the label of T, then labels in the right child)."""
    if T.label is None:
        return []
    else:
        return inorder_labels(T[0]) + [T.label] + inorder_labels(T[1])

def delete_set(S, v):
    """Assuming S is a binary search tree representing a set, a binary
    search tree representing the same set but with v removed (if
    it is present).  The result is the same as S if v is not present.
    >>> T = Tree(5, Tree(3, Tree(2, None, None), Tree(4, None, None)),
    ...             Tree(6, None, Tree(10, Tree(9, None, None),
    ...                                    Tree(13, None, None))))
    >>> inorder_labels(T)
    [2, 3, 4, 5, 6, 9, 10, 13]
    >>> inorder_labels(delete_set(T, 7))
    [2, 3, 4, 5, 6, 9, 10, 13]
    >>> inorder_labels(delete_set(T, 2))
    [3, 4, 5, 6, 9, 10, 13]
    >>> inorder_labels(delete_set(T, 6))
    [2, 3, 4, 5, 9, 10, 13]
    >>> inorder_labels(delete_set(T, 5))
    [2, 3, 4, 6, 9, 10, 13]
    """
    "*** YOUR CODE HERE ***"

# Q8. [Extra for experts]

def preorder(T):
    return preorder_iter(T)

class preorder_iter:
    """>>> T = Tree(1, Tree(2, Tree(3, 4, 5), 6), 7, 8)
    >>> list(preorder(T))
    [1, 2, 3, 4, 5, 6, 7, 8]
    """
    def __init__(self, tree):
        "*** YOUR CODE HERE ***"

    def __next__(self):
        "*** YOUR CODE HERE ***"

    def __iter__(self):
        """Allow this iterator to be used after 'in' in a for loop."""
        return self

