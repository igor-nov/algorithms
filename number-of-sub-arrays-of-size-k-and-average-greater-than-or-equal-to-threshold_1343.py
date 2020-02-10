"""
1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

Solution 1
Runtime: 668 ms, faster than 76.55% of Python3 online submissions for Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold.
Memory Usage: 25.4 MB, less than 100.00% of Python3 online submissions for Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold.

"""
from typing import List

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        len_ar = len(arr)
        if len_ar == k:
            return int(sum(arr) // len_ar >= threshold)

        if len_ar < k:
            return 0

        sum_current = sum(arr[0:k])
        #print(arr[0:k])
        total = 1 if sum_current // k >= threshold else 0
        for i in range(k, len_ar):
            #print(sum_current, sum_current//k, threshold)

            sum_current = sum_current - arr[i-k] + arr[i]
            #print(sum_current, sum_current // k, threshold)
            if sum_current // k >= threshold:
                total += 1

        return total

#####################

import unittest


class TestCase(unittest.TestCase):

    def test1(self):
        inp = [2, 2, 2, 2, 5, 5, 5, 8]
        k = 3
        thr = 4
        out = 3
        res = Solution().numOfSubarrays(inp, k, thr)
        self.assertEqual(res, out)

    def test2(self):
        inp = [1, 1, 1, 1, 1]
        k = 1
        thr = 0
        out = 5
        res = Solution().numOfSubarrays(inp, k, thr)
        self.assertEqual(res, out)

    def test3(self):
        inp = [11, 13, 17, 23, 29, 31, 7, 5, 2, 3]
        k = 3
        thr = 5
        out = 6
        res = Solution().numOfSubarrays(inp, k, thr)
        self.assertEqual(res, out)

    def test4(self):
        inp = [7, 7, 7, 7, 7, 7, 7]
        k = 7
        thr = 7
        out = 1
        res = Solution().numOfSubarrays(inp, k, thr)
        self.assertEqual(res, out)

    def test5(self):
        inp = [4, 4, 4, 4]
        k = 4
        thr = 1
        out = 1
        res = Solution().numOfSubarrays(inp, k, thr)
        self.assertEqual(res, out)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
