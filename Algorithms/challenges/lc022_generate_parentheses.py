"""
Time: O(4^n / n^(3/2)) ~= Catalan numbers
Space: O(n)

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


# DFS recursion
# Idea: at each step, either add '(' or ')', forking two sub-paths,
# but a path is legal only if right >= left.
#                                      "" 3,3
#                                   /            \
#                                ( 2,3            ) 3,2 illegal
#                           /                \
#                         ( 1,3                 ) 2,2
#                     /        \                 /           \
#                   ( 0,3      ) 1,2            ( 1,2       2,1 illegal
#                   \        /    \              /       \
#                    ) 0,2  ( 0,2  ) 1,1        ( 0,2       ) 1,1
#                    \      \     /    \          \       /    \
#                   ) 0,1  ) 0,1 ( 0,1  )1,0     ) 0,1  (0,1   )1,0 illegal
#                   \      \      /     illegal   \      \
#                   )0,0   )0,0   )0,0            )0,0   )0,0
#               ((()))   (()())  (())()         ()(())   ()()()
class Solution1(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def dfs(left, right, s, res):
            if left > right:
                # More unused '(' than ')' means illegal in s.
                # Give up this route.
                return
            if left == right == 0:
                res.append(s)
            if left > 0:
                dfs(left-1, right, s+'(', res)
            if right > 0:
                dfs(left, right-1, s+')', res)

        res = []
        dfs(n, n, '', res)
        return res


# Same as above.
# https://discuss.leetcode.com/topic/17510/4-7-lines-python/2
def generateParenthesis(self, n):
    def generate(p, left, right):
        if right >= left >= 0:
            if right == 0:  # and left == 0
                yield p
            for q in generate(p + '(', left-1, right): yield q  # yield from generate(...), coroutine in Python3
            for q in generate(p + ')', left, right-1): yield q
    return list(generate('', n, n))


# Go over all strings at level n-1, and scan each string,
# and every '(' means an insertion position of the new '()',
# plus the position at the very beginning of the string.
# Ref: career cup book, http://www.cnblogs.com/grandyang/p/4444160.html
class Solution2(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = set()
        if n == 0:
            res.add('')
        else:
            pre = self.generateParenthesis(n-1)
            for s in pre:
                for i in range(len(s)):
                    if s[i] == '(':
                        res.add(s[:i+1] + '()' + s[i+1:])
                res.add('()'+s)
        return list(res)


# Another way of recursion, but not dp.
# https://discuss.leetcode.com/topic/28374/clean-python-dp-solution
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        dp = [[] for i in range(n + 1)]
        dp[0].append('')
        for i in range(n + 1):
            for j in range(i):
                dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
        return dp[n]
