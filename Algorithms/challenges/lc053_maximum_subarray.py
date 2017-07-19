"""
Time: O(n)
Space: O(1)

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

More practice:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""


# kadane's algorithm. same as lc121.
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_here = max_sofar = nums[0]
        for x in nums[1:]:
            max_here = max(x, max_here + x)
            max_sofar = max(max_sofar, max_here)
        return max_sofar


# divide-and-conquer. CRLS 3ed, 4.1.
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def max_cross(nums, low, mid, high):
            left_sum = right_sum = -float('inf')
            summ = 0
            for i in reversed(range(low, mid)):
                summ += nums[i]
                left_sum = max(left_sum, summ)
            summ = 0
            for i in range(mid, high):
                summ += nums[i]
                right_sum = max(right_sum, summ)
            return left_sum + right_sum
        def max_subarray(nums, low, high):
            if low + 1 == high:
                return nums[low]
            else:
                mid = (low + high) // 2
                left_sum = max_subarray(nums, low, mid)
                right_sum = max_subarray(nums, mid, high)
                cross_sum = max_cross(nums, low, mid, high)
                return max(left_sum, right_sum, cross_sum)
        return max_subarray(nums, 0, len(nums))
