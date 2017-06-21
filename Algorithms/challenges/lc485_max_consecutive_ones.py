"""
Time: O(n)
Space: O(1)

Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive
1s. The maximum number of consecutive 1s is 3.

Note:
The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""


class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == 1:
                start = i
                while i < n and nums[i] == 1:
                    i += 1
                res = max(i - start, res)
            i += 1
        return res


class Solution2(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        cnt = 0
        for x in nums:
            cnt = cnt + 1 if x == 1 else 0
            res = max(cnt, res)
        return res


class Solution3(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        sum = 0
        for x in nums:
            sum = (sum + x) * x  # * x to reset sum to 0
            res = max(sum, res)
        return res
