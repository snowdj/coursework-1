"""
Time: O(n)
Space: O(1)

Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
"""


class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        mn, start = nums[len(nums)-1], -1
        mx, end = nums[0], -2
        for i in range(1, n):
            mn = min(mn, nums[n-1-i])
            if nums[n-1-i] > mn:
                start = n-1-i
            mx = max(mx, nums[i])
            if nums[i] < mx:
                end = i
        return end - start + 1


# O(nlg(n)) / O(n)
class Solution2(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ns = sorted(nums)
        i, j = 0, len(nums) - 1
        while i < len(nums) and nums[i] == ns[i]:
            i += 1
        while j > i and nums[j] == ns[j]:
            j -= 1
        return j - i + 1


# same as above, more pythonic
def findUnsortedSubarray(self, nums):
        is_same = [a == b for a, b in zip(nums, sorted(nums))]
        return 0 if all(is_same) else len(nums) - is_same.index(False) - is_same[::-1].index(False)
