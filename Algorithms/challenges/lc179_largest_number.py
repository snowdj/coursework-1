"""
Time: O(nlg(n))
Space: O(n)

Given a list of non negative integers, arrange them such that they form the largest number.

For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.

Note: The result may be very large, so you need to return a string instead of an integer.
"""


# 3|30 but 34|3
class Comparable:
    def __init__(self, num):
        self.value = str(num)
    def __lt__(self, other):
        return self.value + other.value < other.value + self.value
    def __gt__(self, other):
        return self.value + other.value > other.value + self.value
    def __eq__(self, other):
        return self.value + other.value == other.value + self.value

class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums_str = sorted((Comparable(x) for x in nums), reverse=True)
        res = ''.join((ns.value for ns in nums_str))
        return res.lstrip('0') or '0'
