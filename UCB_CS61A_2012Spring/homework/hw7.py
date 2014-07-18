"""Submission for CS61A Homework 7.

Name:
Login:
Collaborators:
"""

# Q1.


def part(n):
    """Return the number of partitions of positive integer n.

    >>> part(5)
    7
    """
    "*** YOUR CODE HERE ***"
    # http://code.activestate.com/recipes/218332-generator-for-integer-partitions/
    #
    # First algorithm: Ordered increse by 1, without duplicates.
    # If you have a partition of n, you can reduce it to a partition of n-1
    # in a canonical way by subtracting one from the smallest item in the
    # partition. E.g. 1+2+3 => 2+3, 2+4 => 1+4. This algorithm reverses the
    # process: for each partition p of n-1, it finds the partitions of n that
    # would be reduced to p by this process. Therefore, each partition of n is
    # output exactly once, at the step when the partition of n-1 to which it
    # reduces is considered.
    #
    def partitions(n):
        # base case of recursion: zero is the sum of the empty list
        if n == 0:
            yield ()
            return
            
	# modify partitions of n-1 to form partitions of n
        for p in partitions(n-1):
            yield (1,) + p
            if p and (len(p) < 2 or p[1] > p[0]):
                yield (p[0] + 1,) + p[1:]

    # Alternative algorithm: Permutation without order, and then eliminate duplicates.
    # http://stackoverflow.com/questions/10035752/elegant-python-code-for-integer-partitioning
    def partition(number):
        answer = set()
        answer.add((number, ))
        for x in range(1, number):
            for y in partition(number - x):
                answer.add(tuple(sorted((x, ) + y)))
        return answer

    return len(tuple(partitions(n)))


# Q2.
def g(n):
    """Return the value of g, defined
          g(n) = n,                                       if n <= 3
          g(n) = g(n - 1) + 2 * g(n - 2) + 3 * g(n - 3),  if n > 3
    For integers n > 0.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    """
    "*** YOUR CODE HERE ***"
    if n <= 3:
        return n
    else:
        return g(n-1) + 2 * g(n - 2) + 3 * g(n - 3)


def g_iter(n):
    """Return the value of g, defined
          g(n) = n,                                       if n <= 3
          g(n) = g(n - 1) + 2 * g(n - 2) + 3 * g(n - 3),  if n > 3
    For integers n > 0.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    """
    "*** YOUR CODE HERE ***"
    if n <= 3:
        return n
    else:
        g_n_3 = 1
        g_n_2 = 2
        g_n_1 = 3
        for _ in range(n-3):
            g_n = g_n_1 + 2 * g_n_2 + 3 * g_n_3
            g_n_1, g_n_2, g_n_3 = g_n, g_n_1, g_n_2
        return g_n


# Q3.
def g_counted(n):
    """Return a tuple (g(n), cost(n)), where cost(n) is the number of times
    the recursive version of g is called during the computation of g(n).

    >>> g_counted(2)
    (2, 1)
    >>> g_counted(4)
    (10, 4)
    >>> g_counted(5)
    (22, 7)
    """
    "*** YOUR CODE HERE ***"
    if n <= 3:
        return (n, 1)
    else:
        g_n_1 = g_counted(n-1)
        g_n_2 = g_counted(n-2)
        g_n_3 = g_counted(n-3)
        g_n = g_n_1[0] + 2 * g_n_2[0] + 3 * g_n_3[0]
        c_n = g_n_1[1] + g_n_2[1] + g_n_3[1] + 1
        return g_n, c_n


# Q4.

from math import sqrt

class vect:
    """A vector in 2-dimensional Euclidean space.

    >>> v1 = vect(3, 4)
    >>> v1
    vect(3, 4)
    >>> print(v1)
    (3, 4)
    >>> v1.x
    3
    >>> v1.y
    4
    >>> v1.x = 7
    Traceback (most recent call last):
        ...
    AttributeError: can't set attribute
    >>> v1 * 3
    vect(9, 12)
    >>> 3 * v1
    vect(9, 12)
    >>> v2 = vect(4, -2)
    >>> v1 + v2
    vect(7, 2)
    >>> v1 - v2
    vect(-1, 6)
    >>> v1 * v2             # inner product = 12 - 8
    4
    >>> abs(v1)             # = sqrt(3**2 + 4**2)
    5.0
    """

    "*** YOUR CODE HERE ***"

# Q5.

def partm(n):
    """Return the number of partitions of positive integer n.

    >>> partm(5)
    7
    >>> partm(500)
    2300165032574323995027
    """

    "*** YOUR CODE HERE ***"

## Q6.

class rlist:
    """A mutable recursive list."""

    empty = None

    def __init__(self, first, rest = empty):
        self.__first = first
        self.__rest = rest

    def first(r):
        return r.__first

    def rest(r):
        return r.__rest

    def set_first(r, new_first):
        r.__first = new_first
    def set_rest(r, new_rest):
        r.__rest = new_rest

    def rlist_to_list(r):
        """The standard Python list containing the same items as R."""
        result = []
        while r is not rlist.empty:
             result.append(r.first())
             r = r.rest()
        return result

def has_cycle(L):
    """True iff L is a circular rlist.

    >>> C = rlist(1, rlist(2, rlist(3)))
    >>> has_cycle(C)
    False
    >>> C.rest().rest().set_rest(C)
    >>> has_cycle(C)
    True
    >>> C = rlist(0, C)
    >>> has_cycle(C)
    True
    """
    "*** YOUR CODE HERE ***"
    
## Q7.  Extra for experts

def has_cycle2(L):
    """True iff L is a circular rlist.

    >>> C = rlist(1, rlist(2, rlist(3)))
    >>> has_cycle2(C)
    False
    >>> C.rest().rest().set_rest(C)
    >>> has_cycle2(C)
    True
    >>> C = rlist(0, C)
    >>> has_cycle2(C)
    True
    """
    "*** YOUR CODE HERE ***"

## Q8.  Extra for experts

from operator import sub, mul

def fact_maker():
    """
    >>> fact_maker()(5)
    120
    """
    "*** YOUR CODE HERE ***"
    #return YOUR_CODE_HERE

