"""
Time: O(n)
Space: O(n)


Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

https://leetcode.com/static/images/problemset/histogram.png
Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].

https://leetcode.com/static/images/problemset/histogram_area.png
The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given heights = [2,1,5,6,2,3],
return 10.
"""


# TLE, 95/96 passed.
class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        maxarea = 0
        for i in range(n):
            if i < n - 1 and heights[i] < heights[i+1]:
                continue
            minh = heights[i]
            for j in reversed(range(i+1)):
                minh = min(minh, heights[j])
                maxarea = max(maxarea, minh*(i-j+1))
        return maxarea


# Stack
# http://www.cnblogs.com/lichen782/p/leetcode_Largest_Rectangle_in_Histogram.html
# https://discuss.leetcode.com/topic/27840/ac-python-clean-solution-using-stack-76ms
# http://www.cnblogs.com/grandyang/p/4322653.html
class Solution2:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        maxarea = 0
        stk = []
        heights.append(0)
        for i, h in enumerate(heights):
            while stk and stk[-1] > h:
                i_top = stk.pop()
                maxarea = max(maxarea, heights[i_top] * (i if not stk else i - stk[-1] - 1))
            stk.append(i)
        heights.pop()
        return maxarea

    def largestRectangleArea2(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        maxarea = 0
        stk = [-1]  # so you don't need to worry about empty stack
        heights.append(0)
        for i, h in enumerate(heights):
            while heights[stk[-1]] > h:
                i_top = stk.pop()
                maxarea = max(maxarea, heights[i_top] * (i - stk[-1] - 1))
            stk.append(i)
        heights.pop()
        return maxarea
