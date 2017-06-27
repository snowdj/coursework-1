#!/usr/bin/env python3
"""
Dynamic programming exercises.

5 easy steps to DP:
    Ref: MIT 6.006 Fall 2011, Lec. 20: Dynamic Programming II
    Video: https://www.youtube.com/watch?v=ENyox7kNKeY  5:50
    (1) define subproblems    --> # of subproblems
    (2) guess (part of solution)    --> # of choices for guess
    (3) relate subproblem solutions using recurrence    --> time/subproblem
    (4) recurse & memoize OR build DP table bottom-up   --> check subproblem recurrence is acyclic,
                                                            i.e., has topological order.
                                                        --> total time
    (5) solve original problem      --> extra time

Examples of Fibonacci and Shortest Paths to show 5 easy steps:
                                Fibonacci            Shortest Paths
(1) subproblems:             F_k for k=1,...,n      delta_k(s,v) for v in V
    # of subproblems           n                      V^2

(2) guess:                   nothing                edge into v (if any)
    # of choices               1                      indegree(v) + 1

(3) recurrence:              F_k = F_k-1 + F_k-2    delta_k(s,v) = min(\delta{k-1}(s,u) + w(u,v) | (u,v) in E)
    time / subproblem          Theta(1)               Theta(indegree(v) + 1)

(4) topological order:       for k = 1, ..., n      for k = 0, 1, ..., |V|-1 for v in V
    total time                 Theta(n)               Theta(VE)

(5) solve orig problem       F_n                    delta_(|V|-1)(s,v) for all v in V
    sometimes extra time
    to combine solutions:      Theta(1)               Theta(V)
"""


import operator


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


class text_justification:
    """
    Split text (list of words) into "good" lines.

    Ref: MIT 6.006 Fall 2011, Lec. 20: Dynamic Programming II
    Video: https://www.youtube.com/watch?v=ENyox7kNKeY  17:05 -> 38:50

    *** Lecture Notes ***
    Dynamic Programming Steps:
    (1) subproblems: suffixes, words[i:]
        -- number of subproblems: n
    (2) guess: where to start 2nd line
        -- number of guesses <= n-i = O(n)
    (3) recurrence: DP(i) = min(DP(j) + badness(i,j)
                                for j in range(i+1, n+1))
        -- j = n means no second line.
        -- time/subproblem = O(n)
        -- DP(n) = 0: base case, blank line, since words are in (0, n-1).
    (4) topological order: i = n, n-1, ..., 0
        -- total time: O(n^2)
    (5) Solve original problem: DP(0)

    Parent pointers: remember which guess was the best.
        -- Find the actual best solution, not just the cost of best solution.
        -- parent[i] = argmin(...) = best j value
        -- Reconstruct the best solution in linear time:
               0 -> parent[0] --> parent[parent[0]] -> ...

    """
    def __init__(self, text_file=None, page_width=1):
        self._words = []
        self._dp = []
        self._parents = []
        if text_file is not None:
            self.read(text_file)
        self._set_page_width(page_width)

    def _set_page_width(self, page_width):
        self._page_width = max(int(page_width), 1)

    def _badness(self, i, j):
        """
        The cost function of how bad to use words[i, j] as a line.
        Assume 0 <= i <= j <= n-1.

        badness(i, j) = (page width - total width) ^ 3, if fit.
                        INF, if don't fit.
        """
        total_width = sum(map(len, self._words[i:j]))
        if total_width > self._page_width:
            return float('inf')
        else:
            return (self._page_width - total_width) ** 3

    def read(self, text_file):
        with open(text_file) as f:
            self._words = f.read().replace('\n', ' ').split()

    def justify(self, page_width):
        """
        Justify words by bottom-up dynamic programming table.
        Second line starts at j-th word, j is from 1 to n.
        """
        if not self._words:  # no text or empty text
            return
        if self._dp and self._parents\
           and self._page_width == page_width:  # text has been justified.
            return

        self._set_page_width(page_width)
        n = len(self._words)
        parents = [n] * n  # parent pointers. possible values: 1 to n.
        dp = [float('inf')] * (n + 1)  # index from 0 to n
        dp[n] = 0
        for i in range(n-1, -1, -1):  # subproblem from dp[0] to dp[n-1].
            guesses = [(dp[j] + self._badness(i, j))
                       for j in range(i+1, n+1)]  # guess from i+1 to n.
            idx, dp[i] = min(enumerate(guesses), key=operator.itemgetter(1))
            parents[i] = i + 1 + idx
        self._dp = dp
        self._parents = parents

    def __str__(self):
        if not self._words:
            return 'Empty Text.'
        if not self._dp or not self._parents:
            return 'Text not justified:\n{}'.format(' '.join(self._words))
        justified = ''
        cost = []
        i = 0
        while i < len(self._words):
            j = self._parents[i]
            justified += '{}\n'.format(' '.join(self._words[i:j]))
            cost.append(self._dp[i])
            i = j
        cost = ', '.join(map(str, map(operator.sub, cost[:-1], cost[1:])))
        s = ('{}\n\nCost of each line:\n{}'.format(justified, cost))
        return s


class blackjack:
    """
    Ref: MIT 6.006 Fall 2011, Lec. 20: Dynamic Programming II
    Video: https://www.youtube.com/watch?v=ENyox7kNKeY  38:50
    """


def test(case):
    if 'just' in case.lower():
        tj = text_justification()
        print('Read news.txt.\n')
        tj.read('news.txt')
        print('Justify news.txt with page width 30:\n')
        tj.justify(30)
        print(tj)
        print('Justify news.txt with page width 50:\n')
        tj.justify(50)
        print(tj)


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        test(sys.argv[1])
    else:
        print('No test case specified.')
