"""
53. Maximum Subarray

Solution 1
Runtime: 68 ms, faster than 58.21% of Python3 online submissions for Maximum Subarray.
Memory Usage: 13.5 MB, less than 86.18% of Python3 online submissions for Maximum Subarray

Solution 2
Runtime: 68 ms, faster than 58.21% of Python3 online submissions for Maximum Subarray.
Memory Usage: 13.4 MB, less than 94.31% of Python3 online submissions for Maximum Subarray.

Solution 3
Runtime: 68 ms, faster than 58.21% of Python3 online submissions for Maximum Subarray.
Memory Usage: 13.6 MB, less than 70.73% of Python3 online submissions for Maximum Subarray.

Solutions:
This is Kadane's Algorithm
Max Contiguous Subarray Sum - Cubic Time To Kadane's Algorithm ("Maximum Subarray" on LeetCode) - https://www.youtube.com/watch?v=2MmGzdiKR9Y
Kadane's Algorithm to Maximum Sum Subarray Problem  https://www.youtube.com/watch?v=86CQq3pKSUw&feature=youtu.be&t=266

Solution 1
https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/

Solution 2
https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/ - Divide and Conquer
https://leetcode.com/problems/maximum-subarray/discuss/20372/How-to-solve-%22Maximum-Subarray%22-by-using-the-divide-and-conquer-approach
"""

from typing import List


class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if dp[i - 1] + nums[i] < nums[i]:
                dp[i] = nums[i]
            else:
                dp[i] = dp[i - 1] + nums[i]
        return max(dp)


class Solution2:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_sub = prev_sub = nums[0]
        for i in range(1, len(nums)):
            if prev_sub + nums[i] < nums[i]:
                prev_sub = nums[i]
            else:
                prev_sub += nums[i]
            max_sub = max(max_sub, prev_sub)
            # print(prev_sub, max_sub, nums[i])
        return max(max_sub, prev_sub)


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub = max_till_current = nums[0]
        for i in range(1, len(nums)):
            max_till_current = max(nums[i], max_till_current + nums[i])
            max_sub = max(max_till_current, max_sub)
        return max_sub


# # Divide and Conquer algorithm
# # https://leetcode.com/problems/maximum-subarray/discuss/20372/How-to-solve-%22Maximum-Subarray%22-by-using-the-divide-and-conquer-approach
# # ~O(n log n)
# def maxSubArray2(self, nums, lo=None, hi=None):
#     if lo is None:
#         lo = 0
#
#     if hi is None:
#         hi = len(nums) - 1
#
#     if lo >= hi:
#         return nums[lo]
#
#     med = (lo + hi) / 2
#
#     return max(self.maxSubArray(nums, lo, med),
#                self.maxSubArray(nums, med + 1, hi),
#                self.maxHelper(nums, lo, med, hi))

#############
import unittest


class TestCase(unittest.TestCase):

    def test1(self):
        inp = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        out = 6
        res = Solution().maxSubArray(inp)
        self.assertEqual(res, out)

    def test2(self):
        inp = [1, 2]
        out = 3
        res = Solution().maxSubArray(inp)
        self.assertEqual(res, out)

    def test3(self):
        inp = [-1, 0, -2]
        out = 0
        res = Solution().maxSubArray(inp)
        self.assertEqual(res, out)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
