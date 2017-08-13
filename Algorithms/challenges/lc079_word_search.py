"""
Time: O(m*n*l)  l = len(word)
Space: O(l)


Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
"""


# Brute-force recursion. Time limit exceeded.
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        k = len(word)
        m = len(board)
        n = m and len(board[0])

        def search(r, c, i):
            if board[r][c] == word[i]:
                if i == k-1:
                    return True
                tmp = board[r][c]
                board[r][c] = '#'
                goodpath = \
                    (r > 0) and search(r-1, c, i+1) or\
                    (r < m-1) and search(r+1, c, i+1) or\
                    (c > 0) and search(r, c-1, i+1) or\
                    (c < n-1) and search(r, c+1, i+1)  # time limit exceeded if using any() here.
                board[r][c] = tmp
                return goodpath
            else:
                return False

        for r in range(m):
            for c in range(n):
                if search(r, c, 0):
                    return True
        return False
