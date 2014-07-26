"""Submission for CS61A Homework 9.

Name:
Login:
Collaborators:
"""


# Q1.
class Mobile(object):
    """A simple binary mobile that has branches of weights or other mobiles.
    
    >>> Mobile(1, 2)
    Traceback (most recent call last):
        ...
    TypeError: 1 is not a Branch
    >>> m = Mobile(Branch(1, Weight(2)), Branch(2, Weight(1)))
    >>> m.weight
    3
    >>> m.isbalanced
    True
    >>> m.left.contents = Mobile(Branch(1, Weight(1)), Branch(2, Weight(1)))
    >>> m.weight
    3
    >>> m.left.contents.isbalanced
    False
    >>> m.isbalanced # All submobiles must be balanced for m to be balanced
    False
    >>> m.left.contents.right.contents.weight = 0.5
    >>> m.left.contents.isbalanced
    True
    >>> m.isbalanced
    False
    >>> m.right.length = 1.5
    >>> m.isbalanced
    True
    """

    def __init__(self, left, right):
        """A Mobile whose two branches are 'left' and 'right'."""
        "*** YOUR CODE HERE ***"
        for arg in (left, right):
            if type(arg) is not Branch:
                raise TypeError("{0} is not a Branch".format(arg))
        self.left = left
        self.right = right

    @property
    def weight(self):
        """The total weight of the mobile."""
        "*** YOUR CODE HERE ***"
        return self.left.contents.weight +\
            self.right.contents.weight

    @property
    def isbalanced(self):
        """True if and only if the mobile is balanced."""
        "*** YOUR CODE HERE ***"
        return (self.left.torque == self.right.torque) and\
            self.left.contents.isbalanced and\
            self.right.contents.isbalanced


def check_positive(x):
    """Check that x is a positive number, and raise an exception otherwise.
    
    >>> check_positive('hello')
    Traceback (most recent call last):
    ...
    TypeError: hello is not a number
    >>> check_positive('1')
    Traceback (most recent call last):
    ...
    TypeError: 1 is not a number
    >>> check_positive(-2)
    Traceback (most recent call last):
    ...
    ValueError: -2 <= 0
    """
    "*** YOUR CODE HERE ***"
    if type(x) not in (int, float):
        raise TypeError('{0} is not a number'.format(x))
    elif x <= 0:
        raise ValueError("{0} <= 0".format(x))


class Branch(object):
    """A branch of a simple binary mobile."""

    def __init__(self, length, contents):
        if type(contents) not in (Weight, Mobile):
            raise TypeError(str(contents) + ' is not a Weight or Mobile')
        check_positive(length)
        self.length = length
        self.contents = contents

    @property
    def torque(self):
        """The torque on the branch"""
        return self.length * self.contents.weight


class Weight(object):
    """A weight."""
    def __init__(self, weight):
        check_positive(weight)
        self.weight = weight
        self.isbalanced = True


# Q2.
def interpret_mobile(s):
    """Return a Mobile described by string s by substituting a class
    Branch, Weight, or Mobile for each occurrence of the letter T.

    >>> simple = 'Mobile(T(2,T(1)), T(1,T(2)))'
    >>> interpret_mobile(simple).weight
    3
    >>> interpret_mobile(simple).isbalanced
    True
    >>> s = 'T(T(4,T(T(4,T(1)),T(1,T(4)))),T(2,T(10)))'
    >>> m = interpret_mobile(s)
    >>> m.weight
    15
    >>> m.isbalanced
    True
    """
    next_T = s.find('T')
    if next_T == -1: # The string 'T' was not found in s
        "*** YOUR CODE HERE ***"
        try:
            return eval(s)
        except TypeError:
            return None
    for t in ('Branch', 'Weight', 'Mobile'):
        substituted = s[:next_T] + t + s[next_T+1:]  # substitute 'T' with t
        "*** YOUR CODE HERE ***"
        x = interpret_mobile(substituted)
        if type(x) is Mobile:
            return x
            
    return None


# Q3.
def subsets(s):
    """Return a list of the subsets of s.

    >>> subsets({True, False})
    [{False, True}, {False}, {True}, set()]
    >>> counts = {x for x in range(10)} # A set comprehension
    >>> subs = subsets(counts)
    >>> len(subs)
    1024
    >>> counts in subs
    True
    >>> len(counts)
    10
    """
    assert type(s) == set, str(s) + ' is not a set.'
    "*** YOUR CODE HERE ***"
    s1 = set(s)
    if not s1:
        return [s1]
    else:
        s_first_set = set({s1.pop()})
        sub_of_rest = subsets(s1)
        return list(map(s_first_set.union, sub_of_rest)) + sub_of_rest

# Q4.

# Values for p, M, p', and M', indexed by problem part (a, b, ...)
p = {}
M = {}
p_prime = {}
M_prime = {}

# Q4a.
"*** YOUR CODE HERE ***"
#p['a'], M['a'], p_prime['a'], M_prime['a'] = *YOUR VALUES*
# Q4b.
"*** YOUR CODE HERE ***"
#p_prime['b'], M_prime['b'] = *YOUR VALUES*
# Q4c.
"*** YOUR CODE HERE ***"
#p['c'], M['c'] = *YOUR VALUES*

# Q5.
def calc_test():
    """Verify that operators work as expected."""
    examples = """
      calc> add(1, 2)
      3
      calc> add(1, mul(2, 3))
      7

      calc> word(12, 34)
      1234
      calc> word(-5, 67.8)
      -567.8
      calc> add(5, word(6, 7))
      72

      calc> word(1)
      TypeError: word requires exactly 2 arguments
      calc> word(-1, -1)
      TypeError: -1-1 is not a well-formed number
      calc> word(0.2, 0.2)
      TypeError: 0.20.2 is not a well-formed number
    """.split('\n')
    while examples:
        line = examples.pop(0).strip()
        if not line:
            continue
        assert line.startswith('calc> '), 'Malformed calc test ' + line
        calc_expression = line[6:]
        target = examples.pop(0).strip()
        # Construct what would have been printed by the Calculator's
        # read-eval-print loop.
        result = None 
        "*** YOUR CODE HERE ***"
        assert result == target, result + ' is not ' + target

from operator import mul

def read_eval_print_loop():
    """Run a read-eval-print loop for calculator."""
    while True:
        try:
            expression_tree = calc_parse(input('calc> '))
            print(calc_eval(expression_tree))
        except (SyntaxError, TypeError, ZeroDivisionError) as err:
            print(type(err).__name__ + ':', err)
        except (KeyboardInterrupt, EOFError):  # <Control>-D, etc.
            print('Calculation completed.')
            return

# Eval & Apply

class Exp(object):
    """A call expression in Calculator.
    
    >>> Exp('add', [1, 2])
    Exp('add', [1, 2])
    >>> str(Exp('add', [1, Exp('mul', [2, 3])]))
    'add(1, mul(2, 3))'
    """

    def __init__(self, operator, operands):
        self.operator = operator
        self.operands = operands

    def __repr__(self):
        return 'Exp({0}, {1})'.format(repr(self.operator), repr(self.operands))

    def __str__(self):
        operand_strs = ', '.join(map(str, self.operands))
        return '{0}({1})'.format(self.operator, operand_strs)

def calc_eval(exp):
    """Evaluate a Calculator expression.

    >>> calc_eval(Exp('add', [2, Exp('mul', [4, 6])]))
    26
    """
    if type(exp) in (int, float):
        return exp
    if type(exp) == Exp:
        arguments = list(map(calc_eval, exp.operands))
        return calc_apply(exp.operator, arguments)

def calc_apply(operator, args):
    """Apply the named operator to a list of args.
    
    >>> calc_apply('+', [1, 2, 3])
    6
    >>> calc_apply('-', [10, 1, 2, 3])
    4
    >>> calc_apply('*', [])
    1
    >>> calc_apply('/', [40, 5])
    8.0
    """
    if operator in ('add', '+'):
        return sum(args)
    if operator in ('sub', '-'):
        if len(args) == 0:
            raise TypeError(operator + 'requires at least 1 argument')
        if len(args) == 1:
            return -args[0]
        return sum(args[:1] + [-arg for arg in args[1:]])
    if operator in ('mul', '*'):
        return reduce(mul, args, 1)
    if operator in ('div', '/'):
        if len(args) != 2:
            raise TypeError(operator + ' requires exactly 2 arguments')
        numer, denom = args
        return numer/denom
    if operator == 'word':
        "*** YOUR CODE HERE ***"
    
# Parsing (NO CHANGES ARE REQUIRED TO THIS PART OF CALCULATOR)

def calc_parse(line):
    """Parse a line of calculator input and return an expression tree."""
    tokens = tokenize(line)
    expression_tree = analyze(tokens)
    if len(tokens) > 0:
        raise SyntaxError('Extra token(s): ' + ' '.join(tokens))
    return expression_tree

def tokenize(line):
    """Convert a string into a list of tokens.
    
    >>> tokenize('add(2, mul(4, 6))')
    ['add', '(', '2', ',', 'mul', '(', '4', ',', '6', ')', ')']
    """
    spaced = line.replace('(',' ( ').replace(')',' ) ').replace(',', ' , ')
    return spaced.strip().split()

known_operators = ['add', 'sub', 'mul', 'div', '+', '-', '*', '/', 'word']

def analyze(tokens):
    """Create a tree of nested lists from a sequence of tokens.

    Operand expressions can be separated by commas, spaces, or both.
    
    >>> analyze(tokenize('add(2, mul(4, 6))'))
    Exp('add', [2, Exp('mul', [4, 6])])
    >>> analyze(tokenize('mul(add(2, mul(4, 6)), add(3, 5))'))
    Exp('mul', [Exp('add', [2, Exp('mul', [4, 6])]), Exp('add', [3, 5])])
    """
    assert_non_empty(tokens)
    token = analyze_token(tokens.pop(0))
    if type(token) in (int, float):
        return token
    if token in known_operators:
        if len(tokens) == 0 or tokens.pop(0) != '(':
            raise SyntaxError('expected ( after ' + token)
        return Exp(token, analyze_operands(tokens))
    else:
        raise SyntaxError('unexpected ' + token)

def analyze_operands(tokens):
    """Analyze a sequence of comma-separated operands."""
    assert_non_empty(tokens)
    operands = []
    while tokens[0] != ')':
        if operands and tokens.pop(0) != ',':
            raise SyntaxError('expected ,')
        operands.append(analyze(tokens))
        assert_non_empty(tokens)
    tokens.pop(0)  # Remove )
    return operands

def assert_non_empty(tokens):
    """Raise an exception if tokens is empty."""
    if len(tokens) == 0:
        raise SyntaxError('unexpected end of line')

def analyze_token(token):
    """Return the value of token if it can be analyzed as a number, or token.
    
    >>> analyze_token('12')
    12
    >>> analyze_token('7.5')
    7.5
    >>> analyze_token('add')
    'add'
    """
    try:
        return int(token)
    except (TypeError, ValueError):
        try:
            return float(token)
        except (TypeError, ValueError):
            return token

# Q6.

def gaussian_solve(A, b):
    """Assuming A is an NxN array of numbers and b is an N-vector 
    of numbers, returns vector x such that Ax = b, if possible."""
    # Copy all the data into fresh lists.
    x = list(b)
    A = [ list(row) for row in A ]

    triangularize(A, x)
    diagonalize(A, x)
    return x

def times_by_dimension(N):
    """A tuple L, U, where L is asymptotically proportional to the
    minimum amount of time required to solve an NxN system using
    gaussian solve and U is proportional to the maximum amount."""
    "*** YOUR CODE HERE ***"

def times_by_size(S):
    """A tuple L, U, where L is asymptotically proportional to the
    minimum amount of time required to solve A x = b where S is
    the total amount of data in A and b, and U is proportional
    to the maximum amount."""
    "*** YOUR CODE HERE ***"

def triangularize(A, b):
    """Assuming A is an NxN mutable array of numbers and b is a
    mutable N-vector of numbers, modify A and b into A' and b' 
    so that any x satisfying Ux=b' also satisfies Ax=b, where U
    is the upper triangle of A'.  The contents of the lower triangle
    of A' are abitrary."""
    for i in range(len(A)):
        pivot(A, b, i)
        eliminate_lower(A, b, i)

def diagonalize(A, b):
    """Assuming A is an NxN mutable array of numbers and b is a
    mutable N-vector of numbers, modify A and modify b into x such
    that Ux=b', where U is the upper triangle of A. The final contents
    of A are unspecified."""
    for i in range(len(A)-1,-1,-1):
        backsolve(A, b, i)

def pivot(A, b, i):
    """Exchange rows i and k>=i of A and items i and k of b so as to 
    maximize the resulting absolute value of |A[i][i]|."""
    k = i
    for j in range(i+1,len(A)):
        if abs(A[j][i]) > abs(A[k][i]):
            k = j
    A[i], A[k], b[i], b[k] = A[k], A[i], b[k], b[i]

def eliminate_lower(A, b, i):
    for j in range(i+1, len(A)):
        c = A[j][i] / A[i][i]	    
        for k in range(i+1, len(A)):
            A[j][k] -= A[i][k] * c
        b[j] -= b[i] * c

def backsolve(A, b, i):
    for k in range(i+1, len(A)):
        b[i] -= b[k]*A[i][k]
    b[i] /= A[i][i]


# Q7. [Extra for experts]

from functools import reduce


def subsets_for_experts(s):
    """Return a list of the subsets of s.

    >>> counts = {x for x in range(10)} # A set comprehension
    >>> subs = subsets_for_experts(counts)
    >>> len(subs)
    1024
    >>> counts in subs
    True
    >>> len(counts)
    10
    """
    "*** YOUR CODE HERE ***"

    return reduce(lambda x, y: [z.union([y]) for z in x] + x, s, [set()])
