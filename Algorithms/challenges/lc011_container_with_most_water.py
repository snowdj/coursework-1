"""
Time: O(n)
Space: O(1)

Given n non-negative integers a1, a2, ..., an, where each represents a point at
coordinate (i, ai). n vertical lines are drawn such that the two endpoints of
line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis
forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxarea = 0
        l, r = 0, len(height)-1
        while l < r:
            h = min(height[l], height[r])
            maxarea = max(maxarea, (r-l) * h)

            # keep moving shorter edge if next height is the same
            while l < r and h == height[l]:
                l += 1
            while l < r and h == height[r]:
                r -= 1
        return maxarea
