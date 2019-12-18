"""
448. Find All Numbers Disappeared in an Array

Solution 1
Runtime: 512 ms, faster than 5.43% of Python3 online submissions for Find All Numbers Disappeared in an Array.
Memory Usage: 20.5 MB, less than 46.43% of Python3 online submissions for Find All Numbers Disappeared in an Array.

Solution 2
Runtime: 380 ms, faster than 83.40% of Python3 online submissions for Find All Numbers Disappeared in an Array.
Memory Usage: 22.8 MB, less than 7.14% of Python3 online submissions for Find All Numbers Disappeared in an Array.

Solution 3
Runtime: 396 ms, faster than 70.08% of Python3 online submissions for Find All Numbers Disappeared in an Array.
Memory Usage: 20.4 MB, less than 46.43% of Python3 online submissions for Find All Numbers Disappeared in an Array.

Solution 4
Runtime: 424 ms, faster than 37.72% of Python3 online submissions for Find All Numbers Disappeared in an Array.
Memory Usage: 20.5 MB, less than 46.43% of Python3 online submissions for Find All Numbers Disappeared in an Array.
"""

from typing import List


class Solution1:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        i = 0
        while i < len(nums):
            if abs(nums[i]) != i + 1 and nums[i] > 0:
                val = nums[i]
                tmp = nums[val - 1]
                nums[val - 1] = -val
                nums[i] = tmp

                #nums[i], nums[nums[i] - 1] = -nums[i], nums[i]
                # nums[i], nums[val] = -nums[val], nums[i]
            else:
                i += 1

            #print(nums, i)

        res = []
        for i in range(len(nums)):
            if abs(nums[i]) != i + 1:
                res.append(i + 1)

        return res


class Solution2:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        if not nums:
            return []

        hash = set()

        for num in nums:
            if num not in hash:
                hash.add(num)

        res = []
        for i in range(1, len(nums)+1):
            if i not in hash:
                res.append(i)

        # if not res and len(hash) != len(nums):
        #     res = [max(nums) + 1]

        return res


class Solution3:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        i = 0

        for i, num in enumerate(nums):
            idx = abs(num) - 1
            if nums[idx] > 0:
                nums[idx] *= -1

        #print(nums, i)

        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)

        return res


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        # for i, num in enumerate(nums):
        for i in range(len(nums)):
            while nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        res = []
        for i, num in enumerate(nums):
            if i + 1 != num:
                res.append(i + 1)

        return res


#############
import unittest


class TestCase(unittest.TestCase):

    def test1(self):
        inp = [4, 3, 2, 7, 8, 2, 3, 1]
        out = [5, 6]
        res = Solution().findDisappearedNumbers(inp)
        self.assertEqual(res, out)

    def test2(self):
        inp = []
        out = []
        res = Solution().findDisappearedNumbers(inp)
        self.assertEqual(res, out)

    def test3(self):
        inp = [1, 1]
        out = [2]
        res = Solution().findDisappearedNumbers(inp)
        self.assertEqual(res, out)

    def test4(self):
        inp = [1, 2]
        out = []
        res = Solution().findDisappearedNumbers(inp)
        self.assertEqual(res, out)

    def test5(self):
        inp = [1, 1, 2, 2]
        out = [3, 4]
        res = Solution().findDisappearedNumbers(inp)
        self.assertEqual(res, out)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
