"""
256. Paint House

Solution 1 - iterative bottom-top
Runtime: 100 ms, faster than 5.04% of Python3 online submissions for Paint House.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Paint House.

Solution 2 - iterative bottom-top
Runtime: 56 ms, faster than 80.00% of Python3 online submissions for Paint House.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Paint House.

Solution 3 - top to bottom
Runtime: 72 ms, faster than 18.98% of Python3 online submissions for Paint House.
Memory Usage: 13.1 MB, less than 80.00% of Python3 online submissions for Paint House.

Solution 3 - top to bottom LRU cache
Runtime: 64 ms, faster than 34.49% of Python3 online submissions for Paint House.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Paint House.



Solutions
leetcode - https://leetcode.com/problems/paint-house/solution/

LINKEDIN - PAINT HOUSE (LeetCode) - https://www.youtube.com/watch?v=fZIsEPhSBgM
1+ lines Ruby, Python - https://leetcode.com/problems/paint-house/discuss/68209/1%2B-lines-Ruby-Python
"""

from typing import List


class Solution1:
    def minCost(self, costs: List[List[int]]) -> int:

        if not costs:
            return 0

        steps = [[None, None, None] for _ in range(len(costs))]
        steps[0] = costs[0]

        for i in range(1, len(costs)):
            cost = costs[i]
            steps[i][0] = min(steps[i - 1][1], steps[i - 1][2]) + cost[0]
            steps[i][1] = min(steps[i - 1][0], steps[i - 1][2]) + cost[1]
            steps[i][2] = min(steps[i - 1][0], steps[i - 1][1]) + cost[2]
        return min(steps[-1])


class Solution2:
    def minCost(self, costs: List[List[int]]) -> int:
        start_red, start_blue, start_green = 0, 0, 0
        for red, green, blue in costs:
            curr_red = min(start_blue, start_green) + red
            curr_green = min(start_blue, start_red) + green
            curr_blue = min(start_red, start_green) + blue
            start_red, start_blue, start_green = curr_red, curr_blue, curr_green
        return min(start_red, start_blue, start_green)


class Solution3:
    def __init__(self):
        self.memo = {}

    def minCost(self, costs: List[List[int]]) -> int:

        if not costs:
            return 0

        def miCostHelper(costs, pos, color_idx):

            if (pos, color_idx) in self.memo:
                total = self.memo[(pos, color_idx)]
            else:
                total = costs[pos][color_idx]
                if pos == 0:
                    pass
                elif color_idx == 0:
                    total += min(miCostHelper(costs, pos - 1, 1), miCostHelper(costs, pos - 1, 2))
                elif color_idx == 1:
                    total += min(miCostHelper(costs, pos - 1, 0), miCostHelper(costs, pos - 1, 2))
                else:
                    total += min(miCostHelper(costs, pos - 1, 0), miCostHelper(costs, pos - 1, 1))
                self.memo[(pos, color_idx)] = total
            return total

        return min(miCostHelper(costs, len(costs) - 1, 0), miCostHelper(costs, len(costs) - 1, 1),
                   miCostHelper(costs, len(costs) - 1, 2))

from functools import lru_cache
class Solution:

    def minCost(self, costs: List[List[int]]) -> int:

        if not costs:
            return 0

        @lru_cache(maxsize=None)
        def helper(pos, color_idx):

            total = costs[pos][color_idx]
            if pos == len(costs)-1:
                pass
            elif color_idx == 0:
                total += min(helper(pos + 1, 1), helper(pos + 1, 2))
            elif color_idx == 1:
                total += min(helper(pos + 1, 0), helper(pos + 1, 2))
            else:
                total += min(helper(pos + 1, 0), helper(pos + 1, 1))

            return total

        return min(helper(0, 0), helper(0, 1), helper(0, 2))


#############
import unittest


class TestCase(unittest.TestCase):

    def test1(self):
        inp = [[17, 2, 17], [16, 16, 5], [14, 3, 19]]
        out = 10
        res = Solution().minCost(inp)
        self.assertEqual(res, out)

    def test2(self):
        inp = []
        out = 0
        res = Solution().minCost(inp)
        self.assertEqual(res, out)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
