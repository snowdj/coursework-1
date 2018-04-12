"""
Time: O(m*n)
Space: O(m*n)

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

11110
11010
11000
00000
Answer: 1

Example 2:

11000
11000
00100
00011
Answer: 3
"""


class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        n = 0 if m == 0 else len(grid[0]) 
        visited = [[False] * n for _ in range(m)]
        
        def dfs(i, j):
            if 0 <= i < m and 0 <= j < n and grid[i][j] == '1' and not visited[i][j]:
                visited[i][j] = True
                dfs(i-1, j)
                dfs(i+1, j)
                dfs(i, j-1)
                dfs(i, j+1)
            
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and not visited[i][j]:
                    dfs(i, j)
                    res += 1
        return res
