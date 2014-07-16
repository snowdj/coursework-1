"""Submission for CS 61A Homework 4.

Name:
Login:
Collaborators:
"""

# Q1.

# [This problem, as promised, held over from last week.]
# Submit a copy of your hw3.py solution with this hw4.py file.

from hw3 import *

def non_zero(x):
    """Return whether x contains 0."""
    return lower_bound(x) > 0 or upper_bound(x) < 0 

def square_interval(x):
    """Return the interval that contains all squares of values in x, where x
    does not contain 0.
    """
    assert non_zero(x), 'square_interval is incorrect for x containing 0'
    return mul_interval(x, x)

# The first two of these intervals contain 0, but the third does not.
seq = (make_interval(-1, 2), make_center_width(-1, 2), make_center_percent(-1, 50))

zero = make_interval(0, 0)

def sum_nonzero_with_for(seq):
    """Returns an interval that is the sum of the squares of the non-zero
    intervals in seq, using a for statement.
    
    >>> str_interval(sum_nonzero_with_for(seq))
    '0.25 to 2.25'
    """
    "*** YOUR CODE HERE ***"

from functools import reduce
def sum_nonzero_with_map_filter_reduce(seq):
    """Returns an interval that is the sum of the squares of the non-zero
    intervals in seq, using using map, filter, and reduce.
    
    >>> str_interval(sum_nonzero_with_map_filter_reduce(seq))
    '0.25 to 2.25'
    """
    "*** YOUR CODE HERE ***"

def sum_nonzero_with_generator_reduce(seq):
    """Returns an interval that is the sum of the squares of the non-zero
    intervals in seq, using using reduce and a generator expression.
    
    >>> str_interval(sum_nonzero_with_generator_reduce(seq))
    '0.25 to 2.25'
    """
    "*** YOUR CODE HERE ***"


# Definitions from lecture.

empty_rlist = None

def make_rlist(first, rest = empty_rlist):
    """A recursive list, r, such that first(r) is 'first' and 
    rest(r) is 'rest,'  which must be an rlist."""
    return first, rest

def first(r):
    """The first item in r."""
    return r[0]

def rest(r):
    """The tail of r."""
    return r[1]

def extend_rlist(left, right):
    """The sequence of items of rlist 'left' followed
    by the items of 'right'."""
    if left == empty_rlist:
         return right
    else:
         return make_rlist(first(left), 
                           extend_rlist(rest(left), right))
    
# Q2.

def is_tuple(x):
    return type(x) is tuple

def to_rlist(items):
    """The sequence of values in 'items', converted into a corresponding
    rlist.  Any tuples among the items also become rlists.
    >>> to_rlist((1, (0, 2), (), 3))
    (1, ((0, (2, None)), (None, (3, None))))
    """
    "*** YOUR CODE HERE ***"
    rl = empty_rlist
    for item in reversed(items):
        if is_tuple(item):
            rl = make_rlist(to_rlist(item), rl)
        else:
            rl = make_rlist(item, rl)
    return rl
        

# Q3.

def could_be_rlist(x):
    """Return true iff x might represent an rlist."""
    return x is None or type(x) is tuple

def to_tuple(L):
    """Assuming L is an rlist, returns a tuple containing the same
    sequence of values.
    >>> x = to_rlist((1, (0, 2), (), 3))
    >>> to_tuple(x)
    (1, (0, 2), (), 3)
    """
    "*** YOUR CODE HERE ***"
    rl = L
    tp = ()
    while rl:
        if could_be_rlist(first(rl)):
            tp = tp + (to_tuple(first(rl)),)
        else:
            tp = tp + (first(rl),)
        rl = rest(rl)
    return tp

# Q4.

def inserted_into_all(item, list_list):
    """Assuming that 'list_list' is an rlist of rlists, return the
    rlist consisting of the rlists in 'list_list', but with 
    'item' prepended as the first item in each.
    >>> L0 = to_rlist(((), (1, 2), (3,)))
    >>> L1 = inserted_into_all(0, L0)
    >>> to_tuple(L1)
    ((0,), (0, 1, 2), (0, 3))
    """
    "*** YOUR CODE HERE ***"
    if list_list == empty_rlist:
        return list_list
    else:
        return make_rlist(make_rlist(item, first(list_list)), inserted_into_all(item, rest(list_list)))


def subseqs(S):
    """Assuming that S is an rlist, return an rlist of all subsequences
    of S (an rlist of rlists).  The order in which the subsequences
    appear is unspecified.  
    >>> seqs = subseqs(to_rlist((1, 2, 3)))
    >>> show = list(to_tuple(seqs))   # Can only sort lists, not tuples
    >>> show.sort()
    >>> show
    [(), (1,), (1, 2), (1, 2, 3), (1, 3), (2,), (2, 3), (3,)]
    """
    "*** YOUR CODE HERE ***"
    if S == empty_rlist:
        return make_rlist(S)
    else:
        sub_of_rest = subseqs(rest(S))
        return extend_rlist(inserted_into_all(first(S), sub_of_rest), sub_of_rest)

# Q5.

def inserted_into_all_tuples(item, tuple_tuple):
    """Assuming that 'tuple_tuple' is a tuple of tuples, return the
    tuple consisting of the tuples in 'tuple_tuple', but with 
    'item' prepended as the first item in each.
    >>> inserted_into_all_tuples(0, ((), (1, 2), (3, )))
    ((0,), (0, 1, 2), (0, 3))
    """
    "*** YOUR CODE HERE ***"
    if tuple_tuple:
        return tuple(map(lambda x, tuple: (x,) + tuple, (item,)*len(tuple_tuple), tuple_tuple))
    else:
        return ((item,),)

def subseqs_tuples(S):
    """Assuming that S is a tuple, return tuple of all subsequences
    of S (a tuple of tuples).  The order in which the subsequences
    appear is unspecified.  
    >>> seqs = subseqs_tuples((1, 2, 3))
    >>> show = list(seqs)
    >>> show.sort()
    >>> show
    [(), (1,), (1, 2), (1, 2, 3), (1, 3), (2,), (2, 3), (3,)]
    """
    "*** YOUR CODE HERE ***"
    sub = ((),)
    for tp in reversed(S):
        sub = inserted_into_all_tuples(tp, sub) + sub
    return sub

# Q7.

def alt_filter(pred, L):
    """The tuple containing all elements, x, of L such that pred(x).
    >>> alt_filter(lambda x: x%2 == 0, (0, 1, 3, 8, 4, 12, 13))
    (0, 8, 4, 12)
    """
    "*** YOUR CODE HERE ***"
    return reduce(lambda x,y: x + (y,) if pred(y) else x , L, (()))
# Q8.

def capitalize_sentences(S):
    """The sequence of words (strings) S, with all initial words in 
    sentences capitalized, and all others unchanged.  A word begins a 
    sentence if it is either the first word in S, or the preceding word 
    in S ends in a period.
    >>> capitalize_sentences(("see", "spot", "run.", "run", "spot", "run."))
    ('See', 'spot', 'run.', 'Run', 'spot', 'run.')
    """
    "*** YOUR CODE HERE ***"
    first_word = True
    prev_word_end_with_dot = False
    def cap_word(w):
        nonlocal first_word
        nonlocal prev_word_end_with_dot
        if first_word:
            w_return = w.capitalize()
            first_word = False
        else:
            w_return = w
        if prev_word_end_with_dot:
            w_return = w.capitalize()
            prev_word_end_with_dot = False
        if w[-1] == ".":
            prev_word_end_with_dot = True
        return w_return

    return tuple(map(cap_word, S))
            
        
# Q9.

def repeat(f, x, n):
     """Apply f to x n times.  When n is 0, the result is x; when n is
     1, the result is f(x); when n is 2, f(f(x)), etc.
     >>> repeat(lambda x: x+1, 1, 5)
     6
     """
     "*** YOUR CODE HERE ***"
     return reduce(lambda x, _: f(x), range(n), x)

# Q10.  Extra for experts.

def sortit(S):
    """The sequence of strings S sorted into lexicographic order 
    (the < operator).
    >>> sortit(("The", "quick", "brown", "fox", "jumps", "over", "the", "lazy",
    ...         "dog."))
    ('The', 'brown', 'dog.', 'fox', 'jumps', 'lazy', 'over', 'quick', 'the')
    """
    "*** YOUR CODE HERE ***"

