"""
Time: O(1)
Space: O(1)

The Hamming distance between two integers is the number of positions
at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note: 0 ≤ x, y < 2^31.

Example:

Input: x = 1, y = 4

Output: 2

Explanation:
1 (0 0 0 1)
4 (0 1 0 0)
     ↑   ↑

The above arrows point to positions where the corresponding bits are
different.
"""


class Solution:
    def hamming_distance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        z = x ^ y
        count = 0
        while z:
            count += 1
            z &= z - 1  # set the right-most bit "1" to "0"

        return count

    def hamming_distance2(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x ^ y).count('1')
