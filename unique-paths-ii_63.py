"""
63. Unique Paths II

Solution 1 - iterative
Runtime: 44 ms, faster than 72.32% of Python3 online submissions for Unique Paths II.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Unique Paths II.

Solution 2 - iterative
Runtime: 44 ms, faster than 72.32% of Python3 online submissions for Unique Paths II.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Unique Paths II.

Solution 3 - bottom top
Runtime: 44 ms, faster than 72.32% of Python3 online submissions for Unique Paths II.
Memory Usage: 13 MB, less than 86.67% of Python3 online submissions for Unique Paths II.

Solutions
Python DP beat 100% python submissions - https://leetcode.com/problems/unique-paths-ii/discuss/146073/Python-DP-beat-100-python-submissions
Python different solutions (O(m*n), O(n), in place). - https://leetcode.com/problems/unique-paths-ii/discuss/23410/Python-different-solutions-(O(m*n)-O(n)-in-place).

Python top-down dp - https://leetcode.com/problems/unique-paths-ii/discuss/310339/Python-top-down-dp
Python | Top-Down & Bottom-Up DP - https://leetcode.com/problems/unique-paths-ii/discuss/389966/Python-or-Top-Down-and-Bottom-Up-DP
Python top-down, minor change based on Unique_Paths_I - https://leetcode.com/problems/unique-paths-ii/discuss/317872/Python-top-down-minor-change-based-on-Unique_Paths_I


"""

from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        if not obstacleGrid or obstacleGrid[0][0]:
            return 0

        rows, cols = len(obstacleGrid), len(obstacleGrid[0])

        dp = [[None] * cols for _ in range(rows)]
        dp[0][0] = 1 if not obstacleGrid[0][0] else 0
        for col in range(1, cols):
            dp[0][col] = 0 if obstacleGrid[0][col] or not dp[0][col - 1] else 1
        for row in range(1, rows):
            dp[row][0] = 0 if obstacleGrid[row][0] or not dp[row - 1][0] else 1

        for row in range(1, rows):
            for col in range(1, cols):
                dp[row][col] = 0 if obstacleGrid[row][col] else dp[row - 1][col] + dp[row][col - 1]

        return dp[rows - 1][cols - 1]


class Solution2:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        if not obstacleGrid or obstacleGrid[0][0]:
            return 0

        rows, cols = len(obstacleGrid), len(obstacleGrid[0])

        dp = [None] * cols
        dp[0] = 1 if not obstacleGrid[0][0] else 0
        for col in range(1, cols):
            dp[col] = 0 if obstacleGrid[0][col] or not dp[col - 1] else 1

        for row in range(1, rows):
            for col in range(cols):
                if obstacleGrid[row][col]:
                    dp[col] = 0
                elif col > 0:
                    dp[col] += dp[col-1]

        return dp[-1]


from functools import lru_cache

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        if not obstacleGrid or obstacleGrid[0][0]:
            return 0

        @lru_cache(maxsize=None)
        def helper(row, col):
            if row < 0 or col < 0:
                return 0
            if row == 0 and col == 0:
                return 0 if obstacleGrid[row][col] else 1
            return 0 if obstacleGrid[row][col] else helper(row - 1, col) + helper(row, col - 1)

        return helper(len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1)


#############
import unittest


class TestCase(unittest.TestCase):

    def test1(self):
        inp = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
        out = 2
        res = Solution().uniquePathsWithObstacles(inp)
        self.assertEqual(res, out)

    def test2(self):
        inp = [[1]]
        out = 0
        res = Solution().uniquePathsWithObstacles(inp)
        self.assertEqual(res, out)

    def test3(self):
        inp = [[0]]
        out = 1
        res = Solution().uniquePathsWithObstacles(inp)
        self.assertEqual(res, out)

    def test4(self):
        inp = [[1, 0]]
        out = 0
        res = Solution().uniquePathsWithObstacles(inp)
        self.assertEqual(res, out)

    def test5(self):
        inp = [[0],[1]]
        out = 0
        res = Solution().uniquePathsWithObstacles(inp)
        self.assertEqual(res, out)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
