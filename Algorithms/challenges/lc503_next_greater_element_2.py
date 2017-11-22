"""
Time: O(n)
Space: O(n)

Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number; 
The second 1's next greater number needs to search circularly, which is also 2.
Note: The length of given array won't exceed 10000.
"""


# Similar to 496, but loop over 2*n.
# Use list instead of hash table to get NGE for every element in nums.
class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        stk = []
        res = [-1] * n

        for i in range(2 * n):
            y = nums[i % n]
            while stk and nums[stk[-1]] < y:
                res[stk.pop()] = y
            if i < n:
                stk.append(i)
        return res
