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
import random


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
        Assume 0 <= i <= j <= n.

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


class BlackJack:
    """
    Perfect-information blackjack game, solved by DP.
    - given entire deck order: c0, c1, ..., c_n-1
    - 1 player game vs. stand-on-17 dealer
    - when should you hit or stand? Guess
    - goal: maximize winnings for fixed bet $1 bet/hand
    - may benefit from losing one hand to improve future hands!

    Ref: MIT 6.006 Fall 2011, Lec. 20: Dynamic Programming II
    Lec Note: https://courses.csail.mit.edu/6.006/fall11/lectures/lecture20.pdf
    Video: https://www.youtube.com/watch?v=ENyox7kNKeY  38:50
           https://www.youtube.com/watch?v=jZbkToeNK2g

    *** Lecture Notes ***
    Dynamic Programming Steps:
    (1) subproblems: suffix c_i:, where to start new hand?
        BJ(i) = best play of c_i,..., c_n-1 (remaining cards)
        -- i: # cards already played
        -- # of subproblems: n
    (2) guess: how many times player hits?
        -- # of choices: <= n
    (3) recurrence:
        BJ(i) = max(
                    outcome in {-1,0,1} + BJ(i + #cards used)    <-- O(n)
                    for #hits in range(0, n) if valid play(don't hit after bust))  <-- O(n)
        #cards used: 4 + #hits + #dealer hits
        -- base case: BJ(i) = 0 for n-i < 4
        -- time/subproblem: \theta(n^2), n choices * run dealer strategy
    (4) topological order: i = n, ..., 0
        -- total time: \theta(n^3)
    (5) solution: BJ(0)
    """
    def __init__(self):
        self._deck = list(range(1, 14)) * 4
        random.shuffle(self._deck)

    def bj(self, i):
        """
        After i cards played, find the max possible winnings by DP.
        Pseudocode in lecture note.
        """
        n = len(self._deck)
        if n - i < 4:  # Base case: not enough cards.
            return 0

        options = []
        for p in range(2, n-i-1):  # Number of cards taken by player.
            player_cards = self._deck[i:i+4:2] + self._deck[i+4:i+p+2]
            ace = player_cards.count(1)
            player = sum(player_cards)
            while ace > 0 and (21-player)//10 > 0:  # decide ace is 1 or 11
                player += 10
                ace -= 1
            if player > 21:  # bust
                options.append(-1+self.bj(i+p+2))  # -$1 since last p bust
                break

            for d in range(2, n-i-p+1):  # run dealer strategy
                dealer_cards = self._deck[i+1:i+5:2] + self._deck[i+p+2:i+p+d]
                dealer = sum(dealer_cards) + dealer_cards.count(1) * 10
                if dealer >= 17:
                    break  # dealer stand
            if dealer > 21:
                dealer = 0  # bust
            options.append(
                ((player > dealer) - (dealer > player)) + self.bj(i+p+d))
        return max(options)


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
    elif 'blackjack' in case.lower():
        bj = BlackJack()
        print("Deck:\n{}".format(bj._deck))
        print("Max profit:\n{}".format(bj.bj(0)))


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        test(sys.argv[1])
    else:
        print('No test case specified.')
