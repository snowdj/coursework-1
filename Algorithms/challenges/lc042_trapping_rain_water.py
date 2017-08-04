"""
Time: O(n)
Space: O(1)

Given n non-negative integers representing an elevation map where the width of
each bar is 1, compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
http://www.leetcode.com/static/images/problemset/rainwatertrap.png
"""


# 2 pointers
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        area = 0
        l, r = 0, n-1
        while l < r:
            minh = min(height[l], height[r])  # highest level of current separation
            if minh == height[l]:
                l += 1
                while l < r and height[l] < minh:
                    area += minh - height[l]
                    l += 1
            else:
                r -= 1
                while l < r and height[r] < minh:
                    area += minh - height[r]
                    r -= 1
        return area


# Same as above, more concise
class Solution2(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        area = 0
        l, r = 0, n-1
        level = 0
        while l < r:
            if height[l] <= height[r]:
                lower = height[l]
                l += 1
            else:
                lower = height[r]
                r -= 1
            level = max(level, lower)
            area += level - lower
        return area


# Better 2-pointer
class Solution3(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        area = 0
        l, r = 0, n-1
        leftmax = rightmax = 0
        while l < r:
            leftmax = max(leftmax, height[l])
            rightmax = max(rightmax, height[r])
            if leftmax < rightmax:
                area += leftmax - height[l]
                l += 1
            else:
                area += rightmax - height[r]
                r -= 1
        return area
