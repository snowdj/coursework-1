"""
Time: O(9*9) = O(1)
Space: O(2*9*9+9) = O(1)

Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules. http://sudoku.com.au/TheRules.aspx

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

http://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png

A partially filled sudoku which is valid.

Note:
A valid Sudoku board (partially filled) is not necessarily solvable. Only the filled cells need to be validated.
"""


# My solution using sets. 75ms
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        st_cols = [set() for _ in range(9)]
        st_blks = [[set() for _ in range(3)] for _ in range(3)]
        for r in range(9):
            st_row = set()
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if any(board[r][c] in st for st in [st_row, st_cols[c], st_blks[r//3][c//3]]):
                    return False
                for st in st_row, st_cols[c], st_blks[r//3][c//3]:
                    st.add(board[r][c])
        return True
