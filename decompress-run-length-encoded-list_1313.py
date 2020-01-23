"""
1313. Decompress Run-Length Encoded List

Solution 1
Runtime: 60 ms, faster than 100.00% of Python3 online submissions for Decompress Run-Length Encoded List.
Memory Usage: 13.1 MB, less than 100.00% of Python3 online submissions for Decompress Run-Length Encoded List.
"""

from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(1, len(nums), 2):
            res += [nums[i]] * nums[i - 1]
        return res

#############
import unittest


class TestCase(unittest.TestCase):

    def test1(self):
        inp = [1, 2, 3, 4]
        out = [2, 4, 4, 4]
        res = Solution().decompressRLElist(inp)
        self.assertEqual(res, out)

    def test2(self):
        inp = [5, 2, 4, 1, 3, 2]
        out = [2, 2, 2, 2, 2, 1, 1, 1, 1, 2, 2, 2]
        res = Solution().decompressRLElist(inp)
        self.assertEqual(res, out)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
