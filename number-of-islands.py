"""
200. Number of Islands

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1


Example 2:

Input:
11000
11000
00100
00011

Output: 3


https://www.youtube.com/watch?v=o8S2bO3pmO4

Runtime: 152 ms, faster than 83.11% of Python3 online submissions for Number of Islands.
Memory Usage: 14.9 MB, less than 9.40% of Python3 online submissions for Number of Islands.

"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        num_islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    num_islands += self.dfs(grid, row, col)
                   
        return num_islands

    def dfs(self, grid, row, col):

        if row >= len(grid) or row < 0 or col >= len(grid[0]) or col < 0 or grid[row][col] == '0':
            return 0

        grid[row][col] = '0'
            
        self.dfs(grid, row + 1, col)
        self.dfs(grid, row - 1, col)
        self.dfs(grid, row, col + 1)
        self.dfs(grid, row, col - 1)
        
        return 1
        
