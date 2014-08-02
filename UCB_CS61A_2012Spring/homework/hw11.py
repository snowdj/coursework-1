"""Submission for CS61A Homework 11.

Name:
Login:
Collaborators:
"""

class Exp(object):
    """A call expression in Calculator or Brackulator.
    
    >>> Exp('add', [1, 2])
    Exp('add', [1, 2])
    """

    def __init__(self, operator, operands):
        self.operator = operator
        self.operands = operands

    def __repr__(self):
        return 'Exp({0}, {1})'.format(repr(self.operator), repr(self.operands))

"""All of your solutions should be defined in terms of the following
dictionaries of bracket types, which configure the parser to supply the
correct operator for each bracket.
"""

BRACKETS = {('[', ']'): 'add',
            ('(', ')'): 'sub',
            ('<', '>'): 'mul',
            ('{', '}'): 'div'}
LEFT_RIGHT = {left:right for left, right in BRACKETS.keys()}


# Q1.

def tokenize(line):
    """Convert a string into a list of tokens.

    >>> tokenize('<[2{12 6}](3 4 5)>')
    ['<', '[', '2', '{', '12', '6', '}', ']', '(', '3', '4', '5', ')', '>']
    """
    "*** YOUR CODE HERE ***"
    spaced = line.replace('(', ' ( ').replace(')', ' ) ').\
        replace('[', ' [ ').replace(']', ' ] ').\
        replace('<', ' < ').replace('>', ' > ').\
        replace('{', ' { ').replace('}', ' } ')
             
    return spaced.strip().split()


# Q2.

def coerce_to_number(token):
    """Coerce a string to a number or return None.
    
    >>> coerce_to_number('-2.3')
    -2.3
    >>> print(coerce_to_number('('))
    None
    """
    try:
        return int(token)
    except (TypeError, ValueError):
        try:
            return float(token)
        except (TypeError, ValueError):
            return None


def isvalid(tokens):
    """Return whether some prefix of tokens represent a valid Brackulator
    expression. Tokens in that expression are removed from tokens as a side
    effect.

    >>> isvalid(tokenize('([])'))
    True
    >>> isvalid(tokenize('([]')) # Missing right bracket
    False
    >>> isvalid(tokenize('[)]')) # Extra right bracket
    False
    >>> isvalid(tokenize('([)]')) # Improper nesting
    False
    >>> isvalid(tokenize('([GO BEARS])')) # Unrecognized token(s)
    False
    >>> isvalid(tokenize('')) # No expression
    False
    >>> isvalid(tokenize('100'))
    True
    >>> isvalid(tokenize('<(( [{}] [{}] ))>'))
    True
    >>> isvalid(tokenize('<[2{12 6}](3 4 5)>'))
    True
    >>> isvalid(tokenize('()()')) # More than one expression is ok
    True
    >>> isvalid(tokenize('[])')) # Junk after a valid expression is ok
    True
    """
    "*** YOUR CODE HERE ***"

    if tokens == []:
        return False

    val = tokens.pop(0)

    if type(coerce_to_number(val)) in [int, float]:
        return True

    if val in LEFT_RIGHT:
        while len(tokens) == 0 or LEFT_RIGHT[val] != tokens[0]:
            if not isvalid(tokens):
                return False
        tokens.pop(0)
        return True
    else:
        return False


# Q3.

def analyze(tokens):
    """Return an expression tree for the first well-formed Brackulator
    expression in tokens. Tokens in that expression are removed from tokens as
    a side effect.

    >>> analyze(tokenize('([])'))
    Exp('sub', [Exp('add', [])])
    >>> analyze(tokenize('([]')) # Missing right bracket
    Traceback (most recent call last):
        ...
    SyntaxError: unexpected end of line
    >>> analyze(tokenize('[)]')) # Extra right bracket
    Traceback (most recent call last):
        ...
    SyntaxError: unexpected )
    >>> analyze(tokenize('([)]')) # Improper nesting
    Traceback (most recent call last):
        ...
    SyntaxError: unexpected )
    >>> analyze(tokenize('([GO BEARS])')) # Unrecognized token(s)
    Traceback (most recent call last):
        ...
    SyntaxError: unexpected GO
    >>> analyze(tokenize('')) # No expression
    Traceback (most recent call last):
        ...
    SyntaxError: unexpected end of line
    >>> analyze(tokenize('100'))
    100
    >>> analyze(tokenize('(1)(1)')) # More than one expression is ok
    Exp('sub', [1])
    >>> analyze(tokenize('[])')) # Junk after a valid expression is ok
    Exp('add', [])
    >>> analyze(tokenize('<[2{12 6}](3 4 5)>'))
    Exp('mul', [Exp('add', [2, Exp('div', [12, 6])]), Exp('sub', [3, 4, 5])])
    >>> calc_eval(analyze(tokenize('<[2{12 6}](3 4 5)>')))
    -24.0
    """
    "*** YOUR CODE HERE ***"
                            

# Q4.


from urllib.request import urlopen
import re


def puzzle_4():
    """Return the soluton to puzzle 4."""
    "*** YOUR CODE HERE ***"


######################################################################

"""The Calculator/Brackulator evaluator from lecture is copied below.  No
changes are required. To run a Brackulator REPL, call read_eval_print_loop."""

from functools import reduce
from operator import mul
try:
    import readline  # Enables access to previous expressions in the REPL
except ImportError:
    pass # Readline is not necessary; it's just a convenience

def read_eval_print_loop():
    """Run a read-eval-print loop for calculator."""
    while True:
        try:
            expression_tree = brack_parse(input('Bra<[<u}at()r> '))
            print(calc_eval(expression_tree))
        except (SyntaxError, TypeError, ZeroDivisionError) as err:
            print(type(err).__name__ + ':', err)
        except (KeyboardInterrupt, EOFError):  # <Control>-D, etc.
            print('Calculation completed.')
            return

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

def brack_parse(line):
    """Parse a line of Brackulator input and return an expression tree."""
    tokens = tokenize(line)
    expression_tree = analyze(tokens)
    if len(tokens) > 0:
        raise SyntaxError('Extra token(s): ' + ' '.join(tokens))
    return expression_tree

