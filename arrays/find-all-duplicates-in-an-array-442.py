"""
442. Find All Duplicates in an Array

Solution 1
[4, 3, 2, 7, 8, 2, 3, 1]
[7, 3, 2, -7, 8, 2, 3, 1]
[3, 3, 2, -7, 8, 2, -3, 1]
[2, 3, -2, -7, 8, 2, -3, 1]
[3, -3, -2, -7, 8, 2, -3, 1]
[3, -3, -2, -7, 8, 2, -3, 1]
[3, -3, -2, -7, 8, 2, -3, 1]
[3, -3, -2, -7, 8, 2, -3, 1]
[3, -3, -2, -7, 8, 2, -3, 1]
[3, -3, -2, -7, 1, 2, -3, -1]
[-3, -3, -2, -7, 3, 2, -3, -1]
[-3, -3, -2, -7, 3, 2, -3, -1]
[-3, -3, -2, -7, 3, 2, -3, -1]
[-3, -3, -2, -7, 3, 2, -3, -1]
[-3, -3, -2, -7, 3, 2, -3, -1]
Runtime: 444 ms, faster than 26.62% of Python3 online submissions for Find All Duplicates in an Array.
Memory Usage: 20 MB, less than 35.71% of Python3 online submissions for Find All Duplicates in an Array.

Solution 2
[4, 3, 2, 7, 8, 2, 3, 1]
[7, 3, 2, -4, 8, 2, 3, 1]
[3, 3, 2, -4, 8, 2, -7, 1]
[2, 3, -3, -4, 8, 2, -7, 1]
[3, -2, -3, -4, 8, 2, -7, 1]
[3, -2, -3, -4, 8, 2, -7, 1]
[3, -2, -3, -4, 8, 2, -7, 1]
[3, -2, -3, -4, 8, 2, -7, 1]
[3, -2, -3, -4, 8, 2, -7, 1]
[3, -2, -3, -4, 1, 2, -7, -8]
[-1, -2, -3, -4, 3, 2, -7, -8]
[-1, -2, -3, -4, 3, 2, -7, -8]
[-1, -2, -3, -4, 3, 2, -7, -8]
[-1, -2, -3, -4, 3, 2, -7, -8]
[-1, -2, -3, -4, 3, 2, -7, -8]
Runtime: 468 ms, faster than 11.85% of Python3 online submissions for Find All Duplicates in an Array.
Memory Usage: 20 MB, less than 35.71% of Python3 online submissions for Find All Duplicates in an Array.


Solution 3
[4, 3, 2, -7, 8, 2, 3, 1]
[4, 3, -2, -7, 8, 2, 3, 1]
[4, -3, -2, -7, 8, 2, 3, 1]
[4, -3, -2, -7, 8, 2, -3, 1]
[4, -3, -2, -7, 8, 2, -3, -1]
[4, -3, -2, -7, 8, 2, -3, -1]
[4, -3, -2, -7, 8, 2, -3, -1]
[-4, -3, -2, -7, 8, 2, -3, -1]
Runtime: 376 ms, faster than 93.13% of Python3 online submissions for Find All Duplicates in an Array.
Memory Usage: 20.6 MB, less than 21.43% of Python3 online submissions for Find All Duplicates in an Array.

Solutions
Java Simple Solution - https://leetcode.com/problems/find-all-duplicates-in-an-array/discuss/92387/Java-Simple-Solution
Python O(n) time O(1) space - https://leetcode.com/problems/find-all-duplicates-in-an-array/discuss/92390/Python-O(n)-time-O(1)-space
Python solution with detailed explanation - https://leetcode.com/problems/find-all-duplicates-in-an-array/discuss/92444/Python-solution-with-detailed-explanation
"""

from typing import List


class Solution1:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        if not nums or len(nums) == 1:
            return []

        i = 0
        print(nums)
        while i < len(nums):

            idx = abs(nums[i]) - 1
            tmp = nums[idx]

            if nums[idx] < 0:
                i += 1
            else:
                nums[idx] *= -1
                if abs(nums[i]) != tmp:
                    nums[i] = tmp

            print(nums)

        res = [num for num in nums if num > 0]
        return res


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        i = 0
        print(nums)
        while i < len(nums):

            idx = abs(nums[i]) - 1
            tmp = nums[idx]

            if nums[idx] < 0:
                i += 1
            else:
                nums[idx] = -nums[i]
                if abs(nums[i]) != tmp:
                    nums[i] = tmp

            print(nums)

        res = [num for num in nums if num > 0]
        return res


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        res = []
        for i in range(len(nums)):
            idx = abs(nums[i]) - 1
            if nums[idx] < 0:
                res.append(idx + 1)
            else:
                nums[idx] *= -1

        return res


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i, num in enumerate(nums):
            cur_num = abs(num) - 1
            if nums[cur_num] < 0:
                res.append(abs(num))
            else:
                nums[cur_num] *= -1

        return res


#############
import unittest


class TestCase(unittest.TestCase):

    # @unittest.skip
    def test1(self):
        inp = [4, 3, 2, 7, 8, 2, 3, 1]
        out = [2, 3]
        # out = [3, 2]
        res = Solution().findDuplicates(inp)
        self.assertEqual(res, out)

    #@unittest.skip
    def test2(self):
        inp = [5,4,6,7,9,3,10,9,5,6]
        out = [9,5,6]
        out = [5, 6, 9]
        res = Solution().findDuplicates(inp)
        self.assertEqual(res, out)


    def test3(self):
        inp = [1]
        out = []
        res = Solution().findDuplicates(inp)
        self.assertEqual(res, out)

    def test4(self):
        inp = [1,1]
        out = [1]
        res = Solution().findDuplicates(inp)
        self.assertEqual(res, out)

    def test5(self):
        inp = [1,1,1]
        out = [1,1]
        res = Solution().findDuplicates(inp)
        self.assertEqual(res, out)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
