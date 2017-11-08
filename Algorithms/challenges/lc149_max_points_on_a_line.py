"""
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
"""


# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b


import collections
import numpy as np


# Use numpy.longdouble to store slope as hasing keys,
# otherwise failed on case: [[0,0],[94911151,94911150],[94911152,94911151]]
class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        n = len(points)
        res = 0

        for i in range(n):
            cnt = collections.Counter()
            dup = 1
            for j in range(i+1, n):
                pi, pj = points[i], points[j]
                if pi.x == pj.x and pi.y == pj.y:
                    dup += 1
                elif pi.x == pj.x:
                    cnt[float('inf')] += 1
                else:
                    slope = np.longdouble(pi.y - pj.y) / (pi.x - pj.x)
                    cnt[slope] += 1
            res = max(res, (cnt.most_common()[0][1] if cnt else 0) + dup)
        return res


# TLE. 28/34 passed.
# Determine if 3-points on 1-line by determinant:
# | x1 y1 1|
# | x2 y2 1| = 0
# | x3 y3 1|
class Solution2:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        n = len(points)
        res = 0
        for i in range(n):
            dup = 1
            for j in range(i+1, n):
                cnt = 0
                pi, pj = points[i], points[j]
                if pi.x == pj.x and pi.y == pj.y:
                    dup += 1
                    continue
                for k in range(n):
                    pk = points[k]
                    x1, y1, x2, y2, x3, y3 = pi.x, pi.y, pj.x, pj.y, pk.x, pk.y
                    if x1 * y2 + x2 * y3 + x3 * y1 - x3 * y2 - x2 * y1 - x1 * y3 == 0:
                        cnt += 1
                res = max(res, cnt)
            res = max(res, dup)
        return res
