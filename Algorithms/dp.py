#!/usr/bin/env python3
"""
Dynamic programming exercises.
"""


def static_vars(**kwargs):
    """
    Decorator to define static variables in a function.
    https://stackoverflow.com/questions/279561/what-is-the-python-equivalent-of-static-variables-inside-a-function  # noqa
    """
    def decorate(func):
        for k in kwargs:
            setattr(func, k, kwargs[k])
        return func
    return decorate


@static_vars(memo={})
def fib(n):
    """
    Use dynamic programming to compute Fibonacci numbers.
    Ref: MIT 6.006 Fall 2011 Lec 19. 5:00.
    https://www.youtube.com/watch?v=OQ5jsbhAv_M
    """
    if n in fib.memo:
        return fib.memo[n]
    if n <= 2:
        f = 1
    else:
        f = fib(n-1) + fib(n-2)
    fib.memo[n] = f
    return f


def fib_bottomup(n):
    """
    Use bottom-up dynamic programming to compute Fibonacci numbers.
    Ref: MIT 6.006 Fall 2011 Lec 19. 23:20.
    https://www.youtube.com/watch?v=OQ5jsbhAv_M
    """
    fib = {}
    for k in range(1, n+1):
        if k <= 2:
            f = 1
        else:
            f = fib[k-1] + fib[k-2]
        fib[k] = f
    return fib[n]
