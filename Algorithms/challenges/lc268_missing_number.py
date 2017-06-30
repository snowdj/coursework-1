"""
Time: O(n)
Space: O(1)

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find
the one that is missing from the array.

For example,
Given nums = [0, 1, 3] return 2.

Note:
Your algorithm should run in linear runtime complexity. Could you
implement it using only constant extra space complexity?
"""

# sum
def missingNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    return 0.5 * n * (n+1) - sum(nums)


# bit xor
def missingNumber2(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    res = 0
    for i, x in enumerate(nums):
        res ^= i+1 ^ x
    return res


# binary search. For sorted input, time O(log(n))
def missingNumber3(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()
    left, right = 0, len(nums)
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] > mid:
            right = mid
        else:
            left = mid + 1
    return right
