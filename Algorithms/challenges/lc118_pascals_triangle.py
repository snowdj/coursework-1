"""
Time: O(n^2)
Space: O(n^2)

Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""


# recursive
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []
        self.triangle = []

        def helper(n):
            if n == 1:
                row = [1]
            else:
                row_prv = helper(n-1)
                row = [row_prv[i] + row_prv[i+1] for i in range(len(row_prv)-1)]
            self.triangle.append(row)
            return [0] + row + [0]
        helper(numRows)
        return self.triangle


# iterative
class Solution2(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []
        row = [0, 1, 0]
        for r in range(numRows):
            row = [row[i] + row[i+1] for i in range(r+1)]
            triangle.append(row)
            row = [0] + row + [0]
        return triangle


# Any row can be constructed using the offset sum of the previous row. Example:
#     1 3 3 1 0
#  +  0 1 3 3 1
#  =  1 4 6 4 1
def generate(self, numRows):
        res = [[1]]
        for i in range(1, numRows):
            res += [map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1])]
        return res[:numRows]
