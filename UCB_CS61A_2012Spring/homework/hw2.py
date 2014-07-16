"""Submission for 61A Homework 2.

Name:
Login:
Collaborators:
"""



# Q1
def product(n, term):
    """Return the product of the first n terms in the sequence formed 
    by applying term to the integers 1, ..., n.
    
    term -- a function that takes one argument
    """
    "*** YOUR CODE HERE ***"

    k, prod = 1,1
    while k <= n:
        prod, k = prod * term(k), k+1
    return prod

def factorial(n):
    """Return n factorial by calling product.

    >>> factorial(4)
    24
    """
    "*** YOUR CODE HERE ***"

    def term(x):
        x = x
        return x

    return product(n, term)


# Q2
def accumulate(combiner, start, n, term):
    """Return the result of combining the first n terms in a sequence.
    
    *** YOUR DESCRIPTION HERE ***
    """
    "*** YOUR CODE HERE ***"
    k, accu = 1,start
    while k <= n:
        accu, k = combiner(accu, k, term), k+1
    return accu
    

def summation_using_accumulate(n, term):
    """An implementation of summation using accumulate."""
    "*** YOUR CODE HERE ***"
    def combiner_sum(accu, x, term):
        return accu+term(x)
    return accumulate(combiner_sum, 0, n, term)


def product_using_accumulate(n, term):
    """An implementation of product using accumulate."""
    "*** YOUR CODE HERE ***"
    def combiner_prod(prod, x, term):
        return prod * term(x)
    return accumulate(combiner_prod, 1, n, term)


# Q3
def double(f):
    """Return a function that applies f twice.
    
    f -- a function that takes one argument
    """
    "*** YOUR CODE HERE ***"
    def double_func(x):
        return f(f(x))
    return double_func


# Q4
def repeated(f, n):
    """Return the function that computes the nth application of f.
    
    f -- a function that takes one argument
    n -- a positive integer

    >>> repeated(square, 2)(5)
    625
    """
    "*** YOUR CODE HERE ***"
    def repeat_func(x):
        i, x_update = 1, x
        while i <= n:
            x_update, i = f(x_update), i+1
        return x_update
    return repeat_func

    # iterative 2
def repeated_2(f,n):
    i, func = 1, f
    while i < n:
        func, i = compose1(func,func), i+1
    return func
    

        
        
def square(x):
    """Return x squared."""
    return x * x

def compose1(f, g):
    """Return a function h, such that h(x) = f(g(x))."""
    def h(x):
        return f(g(x))
    return h


# Q5 (Extra)
def zero(f):
    """Church numeral 0."""
    return lambda x: x

def successor(n):
    return lambda f: lambda x: f(n(f)(x))

def one(f):
    """Church numeral 1."""
    "*** YOUR CODE HERE ***"

def two(f):
    """Church numeral 2."""
    "*** YOUR CODE HERE ***"

def add_church(m, n):
    """Return the Church numeral for m + n, for Church numerals m and n."""
    "*** YOUR CODE HERE ***"

def church_to_int(n):
    """Convert the Church numeral n to a Python integer.
    
    >>> church_to_int(zero)
    0
    >>> church_to_int(one)
    1
    >>> church_to_int(two)
    2
    >>> church_to_int(add_church(two, two))
    4
    """
    "*** YOUR CODE HERE ***"
