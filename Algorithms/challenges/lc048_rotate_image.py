"""
Time: O(n^2)
Space: O(1)

You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
"""


# 42ms
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for l in range(n//2):
            for i in range(l, n-l-1):
                matrix[i][n-1-l], matrix[n-1-l][n-1-i],\
                    matrix[n-1-i][l], matrix[l][i]\
                    = matrix[l][i], matrix[i][n-1-l],\
                    matrix[n-1-l][n-1-i], matrix[n-1-i][l]


# most pythonic 44ms
class Solution2:
    def rotate(self, A):
        A[:] = zip(*A[::-1])
        # A[:] = zip(*reversed(A))


# flip flip 40ms
class Solution3:
    def rotate(self, A):
        A.reverse()
        for i in range(len(A)):
            for j in range(i):
                A[i][j], A[j][i] = A[j][i], A[i][j]


# almost as direct 40ms
class Solution4:
    def rotate(self, A):
        n = len(A)
        for i in range(n/2):
            for j in range(n-n/2):
                for _ in '123':
                    A[i][j], A[~j][i], i, j = A[~j][i], A[i][j], ~j, ~i
                i = ~j
