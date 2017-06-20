"""
Time: O(n)
Space: O(n) for BFS, O(log(n)) for DFS.

Given a nested list of integers, return the sum of all integers in the
list weighted by their depth.

Each element is either an integer, or a list -- whose elements may
also be integers or other lists.

Example 1: Given the list [[1,1],2,[1,1]], return 10. (four 1's at depth 2,
one 2 at depth 1)

Example 2:
Given the list [1,[4,[6]]], return 27. (one 1 at depth 1, one 4 at depth 2,
and one 6 at depth 3; 1 + 4*2 + 6*3 = 27)
"""

# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation

# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """

#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """

#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


class Solution(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int

        Note: BFS tree walk.
        """
        current_level = nestedList
        total = 0
        depth = 0

        while current_level:
            next_level = []
            depth += 1
            for e in current_level:
                if e.isInteger():
                    total += e.getInteger() * depth
                else:
                    next_level.append(e.getList())
            current_level = sum(next_level, [])  # flatten out list of lists
        return total


class Solution2(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int

        Note: Recursive DFS tree walk.
        """
        def dfs(nestedList, depth):
            total = 0
            for e in nestedList:
                if e.isInteger():
                    total += e.getInteger() * depth
                else:
                    total += dfs(e.getList(), depth + 1)
            return total
        return dfs(nestedList, 1)


class Solution3(object):
    def depthSum(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int

        Note: More succinct BFS tree walk.
        """
        total, depth = 0, 1
        while nestedList:
            total += depth * sum(
                [e.getInteger() for e in nestedList if e.isInteger()])
            nestedList = sum(
                [e.getList() for e in nestedList if not e.isInteger()], [])
            depth += 1
        return total
