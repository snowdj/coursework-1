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


# DFS
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

        def dfs(r, c, i):
            if i == k:  # all the characters are checked
                return True
            if r < 0 or r >= m or c < 0 or c >= n or word[i] != board[r][c]:
                return False
            tmp = board[r][c]
            board[r][c] = "#"  # avoid duplicate visit
            res = dfs(r+1, c, i+1) or dfs(r-1, c, i+1) \
                or dfs(r, c+1, i+1) or dfs(r, c-1, i+1)
            board[r][c] = tmp
            return res

        for r in range(m):
            for c in range(n):
                if dfs(r, c, 0):
                    return True
        return False
