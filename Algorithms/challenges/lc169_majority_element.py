"""
Time: O(n)
Space: O(1) using Moore voting, or O(n) using hash table
https://en.wikipedia.org/wiki/Boyer–Moore_majority_vote_algorithm

Given an array of size n, find the majority element. The majority element is
the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always
exist in the array.
"""


import collections


# hash table
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lookup = collections.Counter(nums)
        return max(lookup, key=lookup.get)


# Moore voting
class Solution2(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        major = nums[0]
        count = 0
        for x in nums:
            if count == 0:
                major = x
                count = 1
            elif x == major:
                count += 1
            else:
                count -= 1
        return major
        # do second pass to count appearance numbers of the output
        # to determine if there actually exists a majority.
