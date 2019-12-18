"""
41. First Missing Positive

Solution1
Runtime: 28 ms, faster than 97.82% of Python3 online submissions for First Missing Positive.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for First Missing Positive.


Solutiuon 2
Runtime Error

Solution 3
Runtime: 44 ms, faster than 43.04% of Python3 online submissions for First Missing Positive.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for First Missing Positive.


Solution 4
Runtime: 32 ms, faster than 91.40% of Python3 online submissions for First Missing Positive.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for First Missing Positive.

Examples
https://www.cnblogs.com/EdwardLiu/p/3811206.html
http://n00tc0d3r.blogspot.com/2013/03/find-first-missing-positive.html
"""


class Solution1(object):

    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums or max(nums) <= 0 or min(nums) > 1:
            return 1

        for i, num in enumerate(nums):
            if num < 0:
                nums[i] = 0

        nums.sort()
        res = False
        for i in range(1, len(nums)):
            if nums[i] > 0 and nums[i - 1] >= 0 and nums[i] - nums[i - 1] > 1:
                res = nums[i - 1] + 1
                break

        return res if res else nums[-1] + 1


class Solution2(object):

    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 1

        nums = nums
        max_num = max(nums)

        if max_num <= 0:
            return 1

        nums_by_idx = [True] * max_num

        for pledge in nums:
            if pledge > 0:
                nums_by_idx[pledge - 1] = False

        for i, pledge in enumerate(nums_by_idx):
            if pledge:
                return i + 1

        return max_num + 1


from typing import List


class Solution3:
    def firstMissingPositive(self, nums: List[int]) -> int:

        if not nums or max(nums) < 1 or 1 not in nums:
            return 1

        if max(nums) == 1:
            return 2

        nums_len = len(nums)

        for i, num in enumerate(nums):
            if num > nums_len or num <= 0:
                # if num > nums_len - 1  or num <= 0:
                nums[i] = 1

        for i, num in enumerate(nums):
            if abs(num) == nums_len:
                if nums[0] > 0:
                    nums[0] *= -1
            elif nums[abs(num)] > 0:
                nums[abs(num)] *= -1

        for i in range(1, nums_len):
            if nums[i] > 0:
                return i

        if nums[0] > 0:
            return nums_len

        return nums_len + 1


from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        for i in range(len(nums)):
            while nums[i] > 0 and nums[i] < len(nums) and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i in range(len(nums)):
            if nums[i] - 1 != i:
                return i + 1

        return len(nums) + 1


# class Solution:
#
#     def firstMissingPositive(self, nums: List[int]) -> int:
#
#         for i in range(len(nums)):
#             while len(nums) > nums[i] > 0 and nums[nums[i] - 1] != nums[i]:
#                 nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
#
#         for i, num in enumerate(nums):
#             if i + 1 != num:
#                 return i + 1
#
#         return len(nums) + 1

#
# class Solution:
#
#     def firstMissingPositive(self, nums: List[int]) -> int:
#
#         if not nums or 1 not in nums:
#             return 1
#
#         for i, num in enumerate(nums):
#             if num <= 0 or i > len(nums):
#                 nums[i] = 1
#
#         for i, num in enumerate(nums):
#             idx = abs(num)
#             if idx == len(nums):
#                 nums[0] = -abs(nums[0])
#             else:
#                 nums[idx] = -abs(nums[idx])
#
#         for i in range(1, len(nums)):
#             if nums[i] > 0:
#                 return i
#
#         if nums[0] > 0:
#             return len(nums)
#
#         return len(nums) + 1


#############################

import unittest


# @unittest.skip
class TestCase(unittest.TestCase):

    def test1(self):
        inp = [1, 2, 0]
        out = 3
        res = Solution().firstMissingPositive(inp)
        self.assertEqual(res, out)

    def test2(self):
        inp = [3, 4, -1, 1]
        out = 2
        res = Solution().firstMissingPositive(inp)
        self.assertEqual(res, out)

    def test3(self):
        inp = [7, 8, 9, 11, 12]
        out = 1
        res = Solution().firstMissingPositive(inp)
        self.assertEqual(res, out)

    def test4(self):
        inp = []
        out = 1
        res = Solution().firstMissingPositive(inp)
        self.assertEqual(res, out)

    def test5(self):
        inp = [3, 4, 1, 1, 1, 5, 1, 1, 2, 1]
        out = 6
        res = Solution().firstMissingPositive(inp)
        self.assertEqual(res, out)

    def test6(self):
        inp = [1000, -1]
        out = 1
        res = Solution().firstMissingPositive(inp)
        self.assertEqual(res, out)

    def test7(self):
        inp = [2, 1]
        out = 3
        res = Solution().firstMissingPositive(inp)
        self.assertEqual(res, out)

    def test8(self):
        inp = [1, 3, 3]
        out = 2
        res = Solution().firstMissingPositive(inp)
        self.assertEqual(res, out)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
