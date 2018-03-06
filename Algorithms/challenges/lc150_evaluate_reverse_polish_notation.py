"""
Time: O(n)
Space: O(n)

Evaluate the value of an arithmetic expression in Reverse Polish Notation
 (http://en.wikipedia.org/wiki/Reverse_Polish_notation).

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
"""


class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for t in tokens:
            if t not in ["+", "-", "*", "/"]:
                stack.append(t)
            else:
                r, l = stack.pop(), stack.pop()
                stack.append(str(int(eval(l+t+r))))
        return int(stack.pop())
