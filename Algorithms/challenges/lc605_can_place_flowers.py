"""
Time: O(n)
Space: O(1)

Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True
Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False
Note:
The input array won't violate no-adjacent-flowers rule.
The input array size is in the range of [1, 20000].
n is a non-negative integer which won't exceed the input array size.
"""


# For m continuous zeros, (m+1)//2-1 flowers can be planted, except at 2 ends.
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        zeros, m = 1, 0  # Add one more zero at the beginning
        for p in flowerbed:
            if p:
                m += (zeros + 1) // 2 - 1
                zeros = 0
            else:
                zeros += 1
        return (m + (zeros + 2) // 2 - 1) >= n  # Add one more zero at the end
