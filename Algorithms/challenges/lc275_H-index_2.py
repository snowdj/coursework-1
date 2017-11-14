"""
Time: O(lg(n))
Space: O(1)

Follow up for 274. H-Index: What if the citations array is sorted in ascending
order? Could you optimize your algorithm?

Hint:
Expected runtime complexity is in O(log n) and the input is sorted.
"""


# https://discuss.leetcode.com/topic/23394/o-logn-time-o-1-space-easy-solution-with-detailed-explanations-c-java-python/2
# In fact, using count step first mid is the standard implement way of C++,
# so I do not think there are better ways to implement the binary search.
class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        first, count = 0, n
        while count > 0:
            step = count // 2
            mid = first + step
            if citations[mid] < n - mid:
                first = mid + 1
                count -= step + 1
            else:
                count = step
        return n - first
