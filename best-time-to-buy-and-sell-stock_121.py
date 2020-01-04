"""
121. Best Time to Buy and Sell Stock

Solution 1
Runtime: 60 ms, faster than 82.18% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 13.8 MB, less than 91.95% of Python3 online submissions for Best Time to Buy and Sell Stock.


Solution 2
Runtime: 56 ms, faster than 94.25% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 14 MB, less than 40.23% of Python3 online submissions for Best Time to Buy and Sell Stock.

"""

from typing import List
import math

class Solution1:
    def maxProfit(self, prices: List[int]) -> int:

        max_prof = 0
        if not prices:
            return max_prof

        min_price = prices[0]

        for i in range(1, len(prices)):
            max_prof = max(max_prof, prices[i] - min_price)
            min_price = min(min_price, prices[i])

        return max_prof


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_prof, min_price = 0, math.inf

        for price in prices:
            max_prof = max(max_prof, price - min_price)
            min_price = min(min_price, price)

        return max_prof


#############
import unittest


class TestCase(unittest.TestCase):

    def test1(self):
        inp = [7, 1, 5, 3, 6, 4]
        out = 5
        res = Solution().maxProfit(inp)
        self.assertEqual(res, out)

    def test2(self):
        inp = [7, 6, 4, 3, 1]
        out = 0
        res = Solution().maxProfit(inp)
        self.assertEqual(res, out)

    def test3(self):
        inp = []
        out = 0
        res = Solution().maxProfit(inp)
        self.assertEqual(res, out)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
