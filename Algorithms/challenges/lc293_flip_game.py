"""
You are playing the following Flip Game with your friend: Given a string that
contains only these two characters: + and -, you and your friend take turns to
flip twoconsecutive "++" into "--". The game ends when a person can no longer
make a move and therefore the other person will be the winner.

Write a function to compute all possible states of the string after one valid
move.

For example, given s = "++++", after one move, it may become one of the
following states:

[ "--++", "+--+", "++--" ]

If there is no valid move, return an empty list [].
"""


# Time: O(c*n+m*n)  c: number of pattern occurence  m: length of pattern
# Space: O(c*n)
class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        return [s[:i] + '--' + s[i+2:]  # O(c*n) time and space for copy
                for i in range(len(s) - 1) if s[i:i+2] == '++']  # O(n * m)


# Time: O(c*n+1*n)  c: number of pattern occurence  m: length of pattern
# Space: O(c*n)
# This solution compares only once for the two consecutive '+'.
class Solution2(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        i = 0
        while i < len(s) - 1:  # aggregate O(n)
            if s[i] == '+':  # occurence of a series of '+'
                while i < len(s) - 1 and s[i+1] == '+':  # aggregate O(n)
                    res.append(s[:i] + '--' + s[i+2:])  # O(c*n) for copy
                    i += 1
            i += 1
        return res
