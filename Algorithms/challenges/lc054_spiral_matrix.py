"""
Time: O(m*n)
Space: O(min(m,n) * m*n) extra space for recursion, or O(m*n) iteratively.

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].
"""


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        return matrix and list(matrix.pop(0)) + self.spiralOrder(zip(*matrix)[::-1])  # list(zip) in Python3
