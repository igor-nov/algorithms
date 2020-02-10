"""
62. Unique Paths

Solution 1
Runtime: 24 ms, faster than 90.65% of Python3 online submissions for Unique Paths.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Unique Paths.

Solution 2
Runtime: 24 ms, faster than 90.65% of Python3 online submissions for Unique Paths.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Unique Paths.

Solution 3 - top buttom
Runtime: 32 ms, faster than 36.89% of Python3 online submissions for Unique Paths.
Memory Usage: 13.5 MB, less than 5.77% of Python3 online submissions for Unique Path

@todo - implement using permutation approach

Solutions
Art of Problem Solving: Counting Paths on a Grid - https://www.youtube.com/watch?v=M8BYckxI8_U

Python easy to understand solutions (math, dp O(m*n) and O(n) space). - https://leetcode.com/problems/unique-paths/discuss/22975/Python-easy-to-understand-solutions-(math-dp-O(m*n)-and-O(n)-space).
8 lines Java DP solution, 0ms beats 100%, explained with graph - https://leetcode.com/problems/unique-paths/discuss/184248/8-lines-Java-DP-solution-0ms-beats-100-explained-with-graph

1. Math
Line Math Solution (Python) - https://leetcode.com/problems/unique-paths/discuss/23003/1-Line-Math-Solution-(Python)
Math solution, O(1) space - permutation https://leetcode.com/problems/unique-paths/discuss/22958/Math-solution-O(1)-space

2.
0ms, 5-lines DP Solution in C++ with Explanations - https://leetcode.com/problems/unique-paths/discuss/22954/0ms-5-lines-DP-Solution-in-C%2B%2B-with-Explanations
Python Solution with Detailed Explanation - https://leetcode.com/problems/unique-paths/discuss/23040/Python-Solution-with-Detailed-Explanation

3. bottom up
Python recursive solution with cache - https://leetcode.com/problems/unique-paths/discuss/23200/Python-recursive-solution-with-cache
C++ Top-Down Recursion and Bottom-Up DP - https://leetcode.com/problems/unique-paths/discuss/22965/C%2B%2B-Top-Down-Recursion-and-Bottom-Up-DP
Recursive, memoization and dynamic programming solutions - https://leetcode.com/problems/unique-paths/discuss/182143/Recursive-memoization-and-dynamic-programming-solutions
"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        if not m and not n:
            return 0

        if not m or not n:
            return 1

        dp = [[0] * n for _ in range(m)]
        dp[0][:] = [1] * n

        for row in range(m):
            dp[row][0] = 1

        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

        return dp[m - 1][n - 1]


class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:

        if not m and not n:
            return 0

        if not m or not n:
            return 1

        dp_top = [1] * n

        for row in range(1, m):
            for col in range(1, n):
                dp_top[col] += dp_top[col-1]
        return dp_top[-1]

        #or
        # for row in range(1, m):
        #     prev_left = 1
        #     for col in range(1, n):
        #         dp_top[col] = dp_top[col] + prev_left
        #         prev_left = dp_top[col]
        # return dp_top[-1]
        #



from functools import lru_cache
class Solution3:

    @lru_cache(maxsize=None)
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)


#############
import unittest


class TestCase(unittest.TestCase):

    def test1(self):
        m = 3
        n = 2
        out = 3
        res = Solution().uniquePaths(m, n)
        self.assertEqual(res, out)

    def test2(self):
        m = 3
        n = 3
        out = 6
        res = Solution().uniquePaths(m, n)
        self.assertEqual(res, out)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
