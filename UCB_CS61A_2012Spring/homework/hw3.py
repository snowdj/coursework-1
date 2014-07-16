"""Submission for CS 61A Homework 3.

Name:
Login:
Collaborators:
"""

def str_interval(x):
    """Return a string representation of interval x.
    
    >>> str_interval(make_interval(-1, 2))
    '-1 to 2'
    """
    return '{0} to {1}'.format(lower_bound(x), upper_bound(x))

def add_interval(x, y):
    """Return an interval that contains the sum of any value in interval x and
    any value in interval y.

    >>> str_interval(add_interval(make_interval(-1, 2), make_interval(4, 8)))
    '3 to 10'
    """
    lower = lower_bound(x) + lower_bound(y)
    upper = upper_bound(x) + upper_bound(y)
    return make_interval(lower, upper)

def mul_interval(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y.

    >>> str_interval(mul_interval(make_interval(-1, 2), make_interval(4, 8)))
    '-8 to 16'
    """
    p1 = lower_bound(x) * lower_bound(y)
    p2 = lower_bound(x) * upper_bound(y)
    p3 = upper_bound(x) * lower_bound(y)
    p4 = upper_bound(x) * upper_bound(y)
    return make_interval(min(p1, p2, p3, p4), max(p1, p2, p3, p4))

# Q1
def make_interval(a, b):
    """Construct an interval from a to b."""
    "*** YOUR CODE HERE ***"
    return (a, b)

def lower_bound(x):
    """Return the lower bound of interval x."""
    "*** YOUR CODE HERE ***"
    return x[0]

def upper_bound(x):
    """Return the upper bound of interval x."""
    "*** YOUR CODE HERE ***"
    return x[1]

# Q2
def div_interval(x, y):
    """Return the interval that contains the quotient of any value in x divided
    by any value in y.

    Division is implemented as the multiplication of x by the reciprocal of y.

    >>> str_interval(div_interval(make_interval(-1, 2), make_interval(4, 8)))
    '-0.25 to 0.5'
    """
    "*** YOUR CODE HERE ***"
    assert lower_bound(y) != upper_bound(y) and lower_bound(y) != 0 and upper_bound(y) != 0,\
                             "Divisor is 0!"
    reciprocal_y = make_interval(1/upper_bound(y), 1/lower_bound(y))
    return mul_interval(x, reciprocal_y)

# Q3
def sub_interval(x, y):
    """Return the interval that contains the difference between any value in x
    and any value in y.

    "*** YOUR CODE HERE ***"

    """
    lower = lower_bound(x) - lower_bound(y)
    upper = upper_bound(x) - upper_bound(y)
    return make_interval(lower, upper)
    "*** YOUR CODE HERE ***"

# Q4
def mul_interval_fast(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y, using as few multiplications as possible.

    "*** YOUR CODE HERE ***"
    Only [-,+] * [-,+] requires more than 2 multiplictions.
    """
    
    "*** YOUR CODE HERE ***"
 

# Q5
def make_center_width(c, w):
    """Construct an interval from center and width."""
    return make_interval(c - w, c + w)

def center(x):
    """Return the center of interval x."""
    return (upper_bound(x) + lower_bound(x)) / 2

def width(x):
    """Return the width of interval x."""
    return (upper_bound(x) - lower_bound(x)) / 2

def make_center_percent(c, p):
    """Construct an interval from center and percentage tolerance.
    
    >>> str_interval(make_center_percent(2, 50))
    '1.0 to 3.0'
    """
    "*** YOUR CODE HERE ***"

    return make_interval(c * (1 - p), c * (1 + p))

def percent(x):
    """Return the percentage tolerance of interval x.
    
    >>> percent(make_interval(1, 3))
    50.0
    """
    "*** YOUR CODE HERE ***"
    tol = (upper_bound(x) - lower_bound(x)) / 2.0
    mean = (upper_bound(x) + lower_bound(x)) / 2.0
    return tol/mean

# Q6
def par1(r1, r2):
    return div_interval(mul_interval(r1, r2), add_interval(r1, r2))

def par2(r1, r2):
    one = make_interval(1, 1)
    rep_r1 = div_interval(one, r1)
    rep_r2 = div_interval(one, r2)
    return div_interval(one, add_interval(rep_r1, rep_r2))

"""Lem complains that Alyssa's program gives different answers for the two ways
of computing. This is a serious complaint.

Demonstrate that Lem is right with some well chosen print statements."""

"*** YOUR CODE HERE ***"
r1 = make_interval(200, 201)
r2 = make_interval(345, 349)
print('1st range: {}; 2nd range: {}'.format(str_interval(r1), str_interval(r2)))
print('par1 result: {}'.format(par1(r1, r2)))
print('par2 result: {}'.format(par2(r1, r2)))
# Q7

"""Tell whether par2 is a better program for parallel resistances than par1 and
why.  Write the explanation as a string below."""

"*** YOUR CODE HERE ***"
print("When two intervals are multiplied, their widths are multiplied, so the tolerance is enlarged.")
print("On the other hand, if an interval (uncertain number) is referred once, then the uncertain width will not be expaned. That is by par2 is better than par1.")

# Q8
def quadratic(x, a, b, c):
    """Return the interval that is the range of values taken on by the
    the quadratic defined by a, b, and c, over the domain interval x.

    >>> str_interval(quadratic(make_interval(0, 2), -2, 3, -1))
    '-3 to 0.125'
    >>> str_interval(quadratic(make_interval(1, 3), 2, -3, 1))
    '0 to 10'
    """
    "*** YOUR CODE HERE ***"

# Q9  [Extra problem to be repeated next week.]
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
    sum = zero
    for x in seq:
        if non_zero(x):
            sum = add_interval(sum, square_interval(x))
    return sum


from functools import reduce
def sum_nonzero_with_map_filter_reduce(seq):
    """Returns an interval that is the sum of the squares of the non-zero
    intervals in seq, using using map, filter, and reduce.
    
    >>> str_interval(sum_nonzero_with_map_filter_reduce(seq))
    '0.25 to 2.25'
    """
    "*** YOUR CODE HERE ***"
    return reduce(add_interval, map(square_interval, filter(nonzero, seq)), zero)

def sum_nonzero_with_generator_reduce(seq):
    """Returns an interval that is the sum of the squares of the non-zero
    intervals in seq, using using reduce and a generator expression.
    
    >>> str_interval(sum_nonzero_with_generator_reduce(seq))
    '0.25 to 2.25'
    """
    "*** YOUR CODE HERE ***"
    return reduce(add_interval, (square_interval(x) for x in seq if non_zero(x)), zero)

# Q10 (Extra)

def polynomial(x, c):
    """Return the interval that is the range the polynomial defined by
    coefficients c, for domain interval x.

    >>> str_interval(polynomial(make_interval(0, 2), (-1, 3, -2)))
    '-3 to 0.125'
    >>> str_interval(polynomial(make_interval(1, 3), (1, -3, 2)))
    '0 to 10'
    >>> r = polynomial(make_interval(0.5, 2.25), (10, 24, -6, -8, 3))
    >>> round(lower_bound(r), 5)
    18.0
    >>> round(upper_bound(r), 5)
    23.0
    """
    "*** YOUR CODE HERE ***"

