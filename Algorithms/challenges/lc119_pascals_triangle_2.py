"""
Time: O(k^2)
Space: O(k)

Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
"""


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for _ in range(rowIndex):
            # row = map(lambda x, y: x + y, [0] + row, row + [0])
            row = [x + y for x, y in zip([0]+row, row+[0])]  # 30% faster than map()
        return row