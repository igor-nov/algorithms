"""
16. 3Sum Closest

Solution 1 - Time Limit Exceeded


Solution 2
Runtime: 156 ms, faster than 34.80% of Python3 online submissions for 3Sum Closest.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for 3Sum Closest.


Solutions
Python O(N^2) solution - https://leetcode.com/problems/3sum-closest/discuss/7871/Python-O(N2)-solution
C++ solution O(n^2) using sort - https://leetcode.com/problems/3sum-closest/discuss/7883/C%2B%2B-solution-O(n2)-using-sort
Python solution with detailed explanation - https://leetcode.com/problems/3sum-closest/discuss/7913/Python-solution-with-detailed-explanation
Python solution - https://leetcode.com/problems/3sum-closest/discuss/159459/Python-solution

3Sum closest | three sum closest | leetcode 16 | python solution - https://www.youtube.com/watch?v=bDjcWbHQvJE

"""

import math
from typing import List

# time limit
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        cache = {}
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                cache[(i, j)] = nums[i] + nums[j]

        min_sum = math.inf
        for i in range(len(nums)):
            for key in cache:
                if i not in key:
                    if abs(target - (cache[key] + nums[i])) < abs(target - min_sum):
                        min_sum = cache[key] + nums[i]

                    # min_sum = min(min_sum, abs(target - cache[key] + nums[i]))
                    # print(min_sum, key, i)

        return min_sum


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()

        closest_sum = math.inf
        for lo in range(len(nums) - 1):
            pointer, hi = lo + 1, len(nums) - 1
            while pointer < hi:
                current_sum = nums[lo] + nums[pointer] + nums[hi]

                if abs(target-current_sum) < abs(target-closest_sum):
                    closest_sum = current_sum

                #print((nums[lo], nums[pointer], nums[hi]), closest_sum, current_sum)
                if current_sum > target:
                    hi -= 1
                elif current_sum < target:
                    pointer += 1
                else:
                    return current_sum

        return closest_sum





#############
import unittest


class TestCase(unittest.TestCase):

    def test1(self):
        inp = [-1, 2, 1, -4]
        inp = [-4, -1, 1, 2]
        target = 1
        out = 2
        res = Solution().threeSumClosest(inp, target)
        self.assertEqual(res, out)

    def test2(self):
        inp = [0, 2, 1, -3]
        target = 1
        out = 0
        res = Solution().threeSumClosest(inp, target)
        self.assertEqual(res, out)

    def test3(self):
        inp = [2, 0, 1, -3]
        target = 1
        out = 0
        res = Solution().threeSumClosest(inp, target)
        self.assertEqual(res, out)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
