"""
1. Two Sum

Solution
Runtime: 52 ms, faster than 53.97% of Python3 online submissions for Two Sum.
Memory Usage: 14.2 MB, less than 60.23% of Python3 online submissions for Two Sum.
Runtime: 48 ms, faster than 77.79% of Python3 online submissions for Two Sum.
Memory Usage: 14.2 MB, less than 56.97% of Python3 online submissions for Two Sum.
....
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        remaining_to_find = {}
        for i, num in enumerate(nums):
            if num in remaining_to_find:
                return [remaining_to_find[num], i]
            remaining_to_find[target - num] = i


#############
import unittest


class TestCase(unittest.TestCase):

    def test1(self):
        inp = [2, 7, 11, 15]
        target = 9
        out = [0, 1]
        res = Solution().twoSum(inp, target)
        self.assertEqual(res, out)

    def test2(self):
        inp = [2, 7, 11, 15]
        target = 22
        out = [1, 3]
        res = Solution().twoSum(inp, target)
        self.assertEqual(res, out)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
