"""
1007. Minimum Domino Rotations For Equal Row
Runtime: 1276 ms, faster than 79.72% of Python3 online submissions for Minimum Domino Rotations For Equal Row.
Memory Usage: 14.6 MB, less than 14.29% of Python3 online submissions for Minimum Domino Rotations For Equal Row.

Solution 4
Runtime: 1148 ms, faster than 98.22% of Python3 online submissions for Minimum Domino Rotations For Equal Row.
Memory Usage: 13.7 MB, less than 100.00% of Python3 online submissions for Minimum Domino Rotations For Equal Row.

[Java/C++/Python] Different Ideas - https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/discuss/252242/JavaC%2B%2BPython-Different-Ideas
"""

from typing import List


class Solution1:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:

        r_length = len(A)
        a_info = [set() for _ in range(6)]
        b_info = [set() for _ in range(6)]

        for i, dig in enumerate(A):
            a_info[dig - 1].add(i)

        for i, dig in enumerate(B):
            b_info[dig - 1].add(i)

        for i, dig_info in enumerate(a_info):
            if len(dig_info) == r_length or b_info[i] == r_length:
                return 0
            res = dig_info | b_info[i]
            if len(res) == r_length:
                return min(r_length - len(dig_info), r_length - len(b_info[i]))

        return -1


class Solution2:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        res = self.find_domino(A[0], A, B)

        if res != -1 or A[0] == B[0]:
            return res

        return self.find_domino(B[0], B, A)

    def find_domino(self, num, top, bot):
        rotations = 0
        num_in_row = 0

        for i in range(len(top)):
            if top[i] == num or bot[i] == num:
                if top[i] == num:
                    num_in_row += 1
                if bot[i] == num:
                    rotations += 1
            else:
                return -1

        return min(len(top) - num_in_row, len(top) - rotations)


class Solution3:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        res = self.find_domino(A[0], A, B)

        if res != -1 or A[0] == B[0]:
            return res

        return self.find_domino(B[0], B, A)

    def find_domino(self, num, top, bot):
        rotations_top = 0
        rotations_bot = 0

        for i in range(len(top)):

            if top[i] != num and bot[i] != num:
                return -1
            elif top[i] != num:
                rotations_top += 1
            elif bot[i] != num:
                rotations_bot += 1

        return min(rotations_bot, rotations_top)

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:

        a_rotations = self.numRotations(A, B)
        if not a_rotations:
            return 0

        if a_rotations != -1 and A[0] == B[0]:
            return a_rotations

        b_rotations = self.numRotations(B, A)
        #print('res=', a_rotations, b_rotations)
        return b_rotations if a_rotations == -1 else a_rotations

    def numRotations(self, nums_a, nums_b):
        num_to_find = nums_a[0]
        rot_top, num_in_row = 0, 0
        for i in range(len(nums_a)):
            if nums_a[i] != num_to_find and nums_b[i] != num_to_find:
                return -1
            if nums_a[i] == num_to_find:
                num_in_row += 1
            if nums_b[i] == num_to_find:
                rot_top += 1
        #print(rot_top, num_in_row)
        return min(len(nums_a) - rot_top, len(nums_a) - num_in_row)


############
import unittest


class TestSolution(unittest.TestCase):

    def test_1(self):
        A = [1, 1, 1, 1, 1, 1, 1, 1]
        B = [1, 1, 1, 1, 1, 1, 1, 1]
        out = 0
        res = Solution().minDominoRotations(A, B)
        self.assertEqual(res, out)

    def test_2(self):
        A = [1, 2, 3, 4, 5, 6, 2, 3]
        B = [1, 1, 1, 1, 1, 1, 1, 1]
        out = 0
        res = Solution().minDominoRotations(A, B)
        self.assertEqual(res, out)

    def test_3(self):
        A = [2, 2, 3, 4, 5, 6, 2, 1]
        B = [1, 1, 1, 1, 1, 1, 1, 1]
        out = 0
        res = Solution().minDominoRotations(A, B)
        self.assertEqual(res, out)

    def test_4(self):
        A = [2, 1, 3, 4, 5, 6, 2, 1]
        B = [1, 0, 1, 1, 1, 1, 1, 1]
        out = 1
        res = Solution().minDominoRotations(A, B)
        self.assertEqual(res, out)

    def test_5(self):
        A = [2, 1, 2, 4, 2, 2]
        B = [5, 2, 6, 2, 3, 2]
        out = 2
        res = Solution().minDominoRotations(A, B)
        self.assertEqual(res, out)

    def test_6(self):
        A = [5, 2, 6, 2, 3, 2]
        B = [2, 1, 2, 4, 2, 2]
        out = 2
        res = Solution().minDominoRotations(A, B)
        self.assertEqual(res, out)

    def test_7(self):
        A = [3, 5, 1, 2, 3]
        B = [3, 6, 3, 3, 4]
        out = -1
        res = Solution().minDominoRotations(A, B)
        self.assertEqual(res, out)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
