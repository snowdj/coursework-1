"""
Time: O(N)
Space: O(N)

There are N students in a class. Some of them are friends, while some are not. Their friendship is transitive in nature. For example, if A is a direct friend of B, and B is a direct friend of C, then A is an indirect friend of C. And we defined a friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class. If M[i][j] = 1, then the ith and jth students are direct friends with each other, otherwise not. And you have to output the total number of friend circles among all the students.

Example 1:
Input: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
Output: 2
Explanation:The 0th and 1st students are direct friends, so they are in a friend circle. 
The 2nd student himself is in a friend circle. So return 2.
Example 2:
Input: 
[[1,1,0],
 [1,1,1],
 [0,1,1]]
Output: 1
Explanation:The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends, 
so the 0th and 2nd students are indirect friends. All of them are in the same friend circle, so return 1.
Note:
N is in range [1,200].
M[i][i] = 1 for all students.
If M[i][j] = 1, then M[j][i] = 1.
"""


# union-find, weighted (O(lgN)), path compression (amortized O(1)). 110ms. O(n^2)/O(n)
# Sedgewick course and book:
# https://www.coursera.org/learn/algorithms-part1/lecture/RZW72/quick-union-improvements
class Solution:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        N = len(M)
        id = list(range(N))
        sz = [1] * N  # weighted-union

        # without path compression
        def find1(i):
            while i != id[i]:
                i = id[i]
            return i

        # Simple 1-pass every-other-node path compression
        def find(i):
            while i != id[i]:
                id[i] = id[id[i]]
                i = id[i]
            return i

        # full path compression
        def find3(i):
            if i != id[i]:
                id[i] = find(id[i])
            return id[i]

        def union_simple(p, q):
            i, j = find(p), find(q)
            if i != j:
                id[i] = j

        def union(p, q):
            i, j = find(p), find(q)
            if i == j:
                return
            if sz[i] < sz[j]:
                id[i] = j
                sz[i] += sz[j]
            else:
                id[j] = i
                sz[j] += sz[i]

        for x in range(N):
            for y in range(x+1, N):
                if M[x][y] == 1:
                    union(x, y)
        return sum(id[i] == i for i in range(N))


# DFS, flood fill algorithm. 85ms. O(n)/O(n)
class Solution2:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        N = len(M)
        cnt = 0  # connected group count
        vset = set()  # set of elements that have been counted into connected groups

        def dfs(i):
            for j in range(N):
                if M[i][j] == 1 and j not in vset:
                    vset.add(j)
                    dfs(j)

        for i in range(N):
            if i not in vset:
                cnt += 1  # increase group count
                dfs(i)
        return cnt


# BFS, flood fill algorithm. 85ms. O(n)/O(n)
class Solution3:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        N = len(M)
        cnt = 0  # connected group count
        vset = set()  # set of elements that have been counted into connected groups

        def bfs(i):
            q = [i]
            while q:
                i = q.pop(0)
                for j in range(N):
                    if M[i][j] == 1 and j not in vset:
                        vset.add(j)
                        bfs(j)

        for i in range(N):
            if i not in vset:
                cnt += 1  # increase group count
                bfs(i)
        return cnt


# compute the transitive closure of the (boolean) matrix and count the number
# of different rows. 270ms.
# http://www.ics.uci.edu/~irani/w15-6B/BoardNotes/MatrixMultiplication.pdf
import numpy as np
class Solution4:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        return len(set(map(tuple, (np.matrix(M, dtype='bool')**len(M)).A)))


# scipy.sparse.csgraph. 300ms
import scipy.sparse
class Solution5:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        return scipy.sparse.csgraph.connected_components(M)[0]


# Brute-force, Floyd-Warshall. TLE.
class Solution6:
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        N = len(M)
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    M[i][j] = M[i][j] or (M[i][k] and M[k][j])
        cnt = 0
        vset = set()
        for x in range(N):
            if x not in vset:
                cnt += 1
                for y in range(x + 1, N):
                    if M[x][y]:
                        vset.add(y)
        return cnt
