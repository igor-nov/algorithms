"""
70. Climbing Stairs

Solution 1
Runtime: 24 ms, faster than 83.95% of Python3 online submissions for Climbing Stairs.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Climbing Stairs.

Solution 2
Runtime: 16 ms, faster than 99.54% of Python3 online submissions for Climbing Stairs.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Climbing Stairs.

Interestingly if we change
 dp = [None] * (n + 1) to  dp = [0] * (n + 1) speed decrease to 40ms !!!

Solution 3
Runtime: 20 ms, faster than 96.68% of Python3 online submissions for Climbing Stairs.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Climbing Stairs.

Solutions
The Recursive Staircase - Top Down & Bottom Up Dynamic Programming ("Climbing Stairs" on LeetCode) - https://www.youtube.com/watch?v=NFJ3m9a1oJQ&feature=emb_title
3-4 short lines in every language - https://leetcode.com/problems/climbing-stairs/discuss/25296/3-4-short-lines-in-every-language
Python different solutions (bottom up, top down). - https://leetcode.com/problems/climbing-stairs/discuss/25313/Python-different-solutions-(bottom-up-top-down).
Basically it's a fibonacci. (fix 0 case) - https://leetcode.com/problems/climbing-stairs/discuss/25299/Basically-it's-a-fibonacci.
Using the Fibonacci formular to get the answer directly - https://leetcode.com/problems/climbing-stairs/discuss/25436/Using-the-Fibonacci-formular-to-get-the-answer-directly

"""


class Solution1:
    def climbStairs(self, n: int) -> int:
        prev, current = 1, 2
        for i in range(2, n + 1):
            prev, current = current, prev + current
        return prev


class Solution2:
    def climbStairs(self, n: int) -> int:
        if not n:
            return 1
        dp = [None] * (n + 1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]


from collections import defaultdict


class Solution:
    def __init__(self):
        self.memo = defaultdict(int)

    def climbStairs(self, n: int) -> int:
        if n in (0, 1):
            return 1

        if self.memo[n]:
            return self.memo[n]

        self.memo[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.memo[n]


##########################
import unittest


class TestSolution(unittest.TestCase):

    def test_1(self):
        inp = 2
        out = 2
        res = Solution().climbStairs(inp)
        self.assertEqual(res, out)

    def test_2(self):
        inp = 4
        out = 5
        res = Solution().climbStairs(inp)
        self.assertEqual(res, out)

    def test_3(self):
        inp = 0
        out = 1
        res = Solution().climbStairs(inp)
        self.assertEqual(res, out)

    def test_4(self):
        inp = 1
        out = 1
        res = Solution().climbStairs(inp)
        self.assertEqual(res, out)

    def test_5(self):
        inp = 324
        out = 37281903592600898879479448409585328515842582885579275203077366912825
        res = Solution().climbStairs(inp)
        self.assertEqual(res, out)

    def test_6(self):
        inp = 3
        out = 3
        res = Solution().climbStairs(inp)
        self.assertEqual(res, out)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
