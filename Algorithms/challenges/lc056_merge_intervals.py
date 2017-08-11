"""
Time: O(nlg(n))
Space: O(1)

Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].
"""


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        n = len(intervals)
        res = []
        t = sorted([t.start, t.end] for t in intervals)
        m = t[0]
        for i in range(1, n):
            if t[i][0] > m[1]:
                res.append(Interval(m[0], m[1]))
                m = t[i]
            else:
                m[1] = max(m[1], t[i][1])
        return res + [m]


# Stefan uses out[-1] as m, and class attribute as sorting key.
def merge(self, intervals):
    out = []
    for i in sorted(intervals, key=lambda i: i.start):
        if out and i.start <= out[-1].end:
            out[-1].end = max(out[-1].end, i.end)
        else:
            out += i,
    return out
