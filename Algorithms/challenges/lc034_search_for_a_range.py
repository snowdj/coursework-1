"""
Time: O(lg(n))
Space: O(1)

Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

For example,
Given [5, 7, 7, 8, 8, 10] and target value 8,
return [3, 4].
"""


# Searching for left and right boundaries separately
class Solution1(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = [-1, -1]
        if not nums:
            return res

        # search left boundary
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right-left) // 2
            if target <= nums[mid]:
                right = mid  # Critical: move right to left even if mid == target
            else:
                left = mid + 1
        if nums[right] != target:
            return res
        res[0] = right

        # search right boundary
        right = len(nums)
        while left < right:
            mid = left + (right-left) // 2
            if target >= nums[mid]:
                left = mid + 1  # Critical: move right to left even if mid == target
            else:
                right = mid
        res[1] = left - 1

        return res


# Same as Solution 1, but recursively and shorter.
# Solution 1 on https://discuss.leetcode.com/topic/16486/9-11-lines-o-log-n
class Solution2(object):
    def searchRange(self, nums, target):
        def search(lo, hi):
            if nums[lo] == nums[hi] == target:
                return [lo, hi]
            if nums[lo] <= target <= nums[hi]:
                mid = (lo + hi) // 2
                l, r = search(lo, mid), search(mid+1, hi)
                return max(l, r) if -1 in l+r else [l[0], r[1]]
            return [-1, -1]
        return search(0, len(nums)-1) if nums else [-1, -1]


# Search left boundary only for the target, and then search the left boundary
# of target+1, which is 1 index behind the right boundary of target.
class Solution3(object):
    def searchRange(self, nums, target):
        def search(n):
            lo, hi = 0, len(nums)
            while lo < hi:
                mid = (lo + hi) / 2
                if nums[mid] >= n:
                    hi = mid
                else:
                    lo = mid + 1
            return lo
        lo = search(target)
        return [lo, search(target+1)-1] if target in nums[lo:lo+1] else [-1, -1]


# Best. Same as Solution 3, but use Python standard libary bisect.
class Solution4(object):
    def searchRange(self, nums, target):
        lo = bisect.bisect_left(nums, target)
        return [lo, bisect.bisect_right(nums, target)-1] if target in nums[lo:lo+1] else [-1, -1]
