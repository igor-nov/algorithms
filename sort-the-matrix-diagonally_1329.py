"""
1329. Sort the Matrix Diagonally

Solution 1
Runtime: 460 ms, faster than 100.00% of Python3 online submissions for Sort the Matrix Diagonally.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Sort the Matrix Diagonally.

Solution 2
Runtime: 84 ms, faster than 100.00% of Python3 online submissions for Sort the Matrix Diagonally.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Sort the Matrix Diagonally.

[Java/Python] Straight Forward - https://leetcode.com/problems/sort-the-matrix-diagonally/discuss/489749/JavaPython-Straight-Forward
C++ bubble sort clean clear and easy - https://leetcode.com/problems/sort-the-matrix-diagonally/discuss/489737/C%2B%2B-bubble-sort-clean-clear-and-easy
Several Python solutions - https://leetcode.com/problems/sort-the-matrix-diagonally/discuss/489846/Several-Python-solutions

"""
from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:

        if not mat:
            return mat

        rows = len(mat)
        cols = len(mat[0])
        step = 0
        while step < cols-1:
            for row in range(rows-1, 0, -1):
                for col in range(1, cols):
                    if mat[row][col] < mat[row-1][col-1]:
                        mat[row][col], mat[row - 1][col - 1] = mat[row - 1][col - 1], mat[row][col]
            step += 1
        return mat

from collections import defaultdict
class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:

        diagonals = defaultdict(list)
        if not mat:
            return mat

        rows = len(mat)
        cols = len(mat[0])

        res = [[None]*cols for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                diagonals[col-row].append(mat[row][col])

        diagonals = { diag_key: sorted(diag_nums) for diag_key, diag_nums in diagonals.items()}

        for row in range(rows - 1, -1, -1):
            for col in range(cols - 1, -1, -1):
                res[row][col] = diagonals[col-row].pop()

        return res








#############
import unittest


class TestCase(unittest.TestCase):

    def test1(self):
        inp = [[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]
        out = [[1, 1, 1, 1], [1, 2, 2, 2], [1, 2, 3, 3]]
        res = Solution().diagonalSort(inp)
        self.assertEqual(res, out)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
