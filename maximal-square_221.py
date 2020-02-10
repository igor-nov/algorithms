"""
221. Maximal Square

Solution 1 - uses (m+1)*(n+1) matrix
Runtime: 220 ms, faster than 43.64% of Python3 online submissions for Maximal Square.
Memory Usage: 13.8 MB, less than 95.45% of Python3 online submissions for Maximal Square.

Solution 2 - same but uses m*n dp matrix

Solution 3 - O(m) - dp matrix
Runtime: 192 ms, faster than 90.21% of Python3 online submissions for Maximal Square.
Memory Usage: 13.8 MB, less than 90.91% of Python3 online submissions for Maximal Square.

@todo - implement Solution_0
Solutions
Maximum Sub Square Matrix Dynamic Programming - https://www.youtube.com/watch?v=_Lf1looyJMU
Largest Square of 1's in A Matrix (Dynamic Programming) - https://www.youtube.com/watch?v=FO7VXDfS8Gk

C++ space-optimized DP - https://leetcode.com/problems/maximal-square/discuss/61803/C%2B%2B-space-optimized-DP
6 lines, Visual Explanation, O(mn) - https://leetcode.com/problems/maximal-square/discuss/61935/6-lines-Visual-Explanation-O(mn)
"""

from typing import List


class Solution_0:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        if not matrix:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        dp = [[int(matrix[row][col]) for col in range(cols)] for row in range(rows)]
        area = 1 if sum(dp[0]) > 0 else 0

        for row in range(1, rows):
            for col in range(cols):
                if dp[row][col] == 1:
                    dp[row][col] += dp[row - 1][col]

        for row in dp:
            print(row)

        for row in range(rows - 1, -1, -1):
            area = max(area, self.getMaxArea(dp[row][:]))

        return area

    def getMaxArea(self, row):
        # if row == [0, 3, 1, 2, 2, 1, 1, 0, 1]:
        #     print(1)
        #     pass
        area = 0
        queue = [(row[0], 0)]
        for col in range(1, len(row)):
            if row[col] < queue[-1][0]:
                while queue and row[col] < queue[0][0]:
                    height, idx = queue.pop(0)
                    area = max(area, min(col - idx, height) ** 2)
                    # if row == [0, 3, 1, 2, 2, 1, 1, 0, 1]:
                    # print(f'area={area}, queue={queue},  row={row},  height = {height}, col={col}, idx={idx}, col-idx={col - idx}')
            queue.append((row[col], col))

        col = len(row) - 1
        while queue:
            height, idx = queue.pop(0)
            area = max(area, min(col - idx, height) ** 2)
            if row == [3, 1, 3, 3, 3]:
                print(f'area={area}, queue={queue},  row={row},  height = {height}, col-idx={col - idx}')

        return area


class Solution1:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        if not matrix:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        dp = [[1 if (row and col) and matrix[row - 1][col - 1] == '1' else 0 for col in range(cols + 1)] for row in
              range(rows + 1)]

        area = 0
        for row in range(1, rows + 1):
            for col in range(1, cols + 1):
                if dp[row][col]:
                    dp[row][col] += min(dp[row - 1][col], dp[row - 1][col - 1], dp[row][col - 1])
                    area = max(area, dp[row][col] ** 2)

        return area


class Solution2:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        if not matrix:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        dp = [[1 if matrix[row][col] == '1' else 0 for col in range(cols)] for row in range(rows)]

        area = 1 if sum(dp[0]) > 0 else 0
        for row in range(1, rows):
            for col in range(1, cols):
                if dp[row][col]:
                    dp[row][col] += min(dp[row - 1][col], dp[row - 1][col - 1], dp[row][col - 1])
                    area = max(area, dp[row][col] ** 2)

        return area


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:

        if not matrix:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        dp_top_row = [1 if matrix[0][col] == '1' else 0 for col in range(cols)]
        area = 1 if sum(dp_top_row) > 0 else 0


        for row in range(1, rows):
            prev_left = 0
            for col in range(0, cols):
                if matrix[row][col] == '1':
                    prev_left_tmp = dp_top_row[col]
                    dp_top_row[col] = min(dp_top_row[col], dp_top_row[col - 1], prev_left) + 1
                    area = max(area, dp_top_row[col] ** 2)
                    prev_left = prev_left_tmp
                else:
                    dp_top_row[col] = 0

        return area


################################
import unittest


# @unittest.skip
class TestCase(unittest.TestCase):

    def test1(self):
        inp = [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"]]
        out = 4
        res = Solution().maximalSquare(inp)
        self.assertEqual(res, out)

    def test2(self):
        inp = [
            ["1", "0", "1", "0", "0"],
            ["1", "0", "0", "1", "1"],
            ["1", "1", "1", "0", "1"],
            ["1", "0", "0", "1", "0"]]
        out = 1
        res = Solution().maximalSquare(inp)
        self.assertEqual(res, out)

    def test3(self):
        inp = [
            ["1", "0", "1", "1", "1"],
            ["1", "0", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "0", "0", "1", "0"]]
        out = 9
        res = Solution().maximalSquare(inp)
        self.assertEqual(res, out)

    def test4(self):
        inp = [
            ["1", "1", "1", "1", "0"],
            ["1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "1"],
            ["1", "1", "1", "1", "0"]]
        out = 16
        res = Solution().maximalSquare(inp)
        self.assertEqual(res, out)

    def test5(self):
        inp = [
            ["1", "0", "1", "0"],
            ["1", "0", "1", "1"],
            ["1", "0", "1", "1"],
            ["1", "1", "1", "1"]
        ]
        out = 4
        res = Solution().maximalSquare(inp)
        self.assertEqual(res, out)

    def test6(self):
        inp = [
            ["1", "0", "1", "0", "0", "1", "1", "1", "0"],
            ["1", "1", "1", "0", "0", "0", "0", "0", "1"],
            ["0", "0", "1", "1", "0", "0", "0", "1", "1"],
            ["0", "1", "1", "0", "0", "1", "0", "0", "1"],
            ["1", "1", "0", "1", "1", "0", "0", "1", "0"],
            ["0", "1", "1", "1", "1", "1", "1", "0", "1"],
            ["1", "0", "1", "1", "1", "0", "0", "1", "0"],
            ["1", "1", "1", "0", "1", "0", "0", "0", "1"],
            ["0", "1", "1", "1", "1", "0", "0", "1", "0"],
            ["1", "0", "0", "1", "1", "1", "0", "0", "0"]
        ]
        out = 4
        res = Solution().maximalSquare(inp)
        self.assertEqual(res, out)

    def test7(self):
        inp = [["0", "0", "1", "0"], ["1", "1", "1", "1"], ["1", "1", "1", "1"], ["1", "1", "1", "0"],
               ["1", "1", "0", "0"], ["1", "1", "1", "1"], ["1", "1", "1", "0"]]
        out = 9
        res = Solution().maximalSquare(inp)
        self.assertEqual(res, out)

    def test8(self):
        inp = [["0", "0", "0", "1", "0", "1", "0"], ["0", "1", "0", "0", "0", "0", "0"],
               ["0", "1", "0", "1", "0", "0", "1"], ["0", "0", "1", "1", "0", "0", "1"],
               ["1", "1", "1", "1", "1", "1", "0"], ["1", "0", "0", "1", "0", "1", "1"],
               ["0", "1", "0", "0", "1", "0", "1"], ["1", "1", "0", "1", "1", "1", "0"],
               ["1", "0", "1", "0", "1", "0", "1"], ["1", "1", "1", "0", "0", "0", "0"]]
        out = 4
        res = Solution().maximalSquare(inp)
        self.assertEqual(res, out)

    def test9(self):
        inp = [
            ["0", "1", "1", "0", "1"],
            ["1", "1", "0", "1", "0"],
            ["0", "1", "1", "1", "0"],
            ["1", "1", "1", "1", "0"],
            ["1", "1", "1", "1", "1"],
            ["0", "0", "0", "0", "0"]
        ]
        out = 9
        res = Solution().maximalSquare(inp)
        self.assertEqual(res, out)

    def test10(self):
        inp = [["1"]]
        out = 1
        res = Solution().maximalSquare(inp)
        self.assertEqual(res, out)

    def test11(self):
        inp = [["0", "0", "0", "0", "0"], ["1", "0", "0", "0", "0"], ["0", "0", "0", "0", "0"],
               ["0", "0", "0", "0", "0"]]
        out = 1
        res = Solution().maximalSquare(inp)
        self.assertEqual(res, out)


    def test12(self):
        inp = [["0"]]
        out = 0
        res = Solution().maximalSquare(inp)
        self.assertEqual(res, out)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
