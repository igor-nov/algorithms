"""
238. Product of Array Except Self

Solution 1 - with usage of division - next step remove division
Runtime: 112 ms, faster than 98.56% of Python3 online submissions for Product of Array Except Self.
Memory Usage: 18.8 MB, less than 98.00% of Python3 online submissions for Product of Array Except Self.

Solution 2 - 2 additional lists without division
Runtime: 128 ms, faster than 52.94% of Python3 online submissions for Product of Array Except Self.
Memory Usage: 19.2 MB, less than 96.00% of Python3 online submissions for Product of Array Except Self.

Solution 3 - simplified version
Runtime: 140 ms, faster than 16.13% of Python3 online submissions for Product of Array Except Self.
Memory Usage: 19.1 MB, less than 98.00% of Python3 online submissions for Product of Array Except Self.

Solution 4 - one  additional list - @todo
Runtime: 120 ms, faster than 87.18% of Python3 online submissions for Product of Array Except Self.
Memory Usage: 19.5 MB, less than 96.00% of Python3 online submissions for Product of Array Except Self.

Solutions
https://leetcode.com/problems/product-of-array-except-self/solution/

"""
from typing import List


class Solution1:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        total_0 = sum([item + 1 for i, item in enumerate(nums) if not item])

        if total_0 > 1:
            nums = [0] * len(nums)
        else:
            total = 1
            for num in nums:
                total *= num if num else 1

            for i, num in enumerate(nums):
                if not total_0:
                    nums[i] = total // nums[i]
                else:
                    if not nums[i]:
                        nums[i] = total
                    else:
                        nums[i] = 0
        return nums


class Solution2:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        total_0 = sum([item + 1 for i, item in enumerate(nums) if not item])

        if total_0 > 1:
            nums = [0] * len(nums)
        else:
            """
            [1,2,3,4]
            
            [2,  3,   4,  5]
            2    6   24  120
            120  60  20   5
                        
            60   40  30   24
            
            [1,2,3,4]
            [1, 2, 6, 24]
            [24, 24, 12, 4]
            """
            mult_forward = [0] * len(nums)
            mult_forward[0] = nums[0]
            for i in range(1, len(nums)):
                mult_forward[i] = mult_forward[i - 1] * nums[i]

            mult_backward = [0] * len(nums)
            mult_backward[-1] = nums[-1]
            for i in range(len(nums) - 2, -1, -1):
                mult_backward[i] = mult_backward[i + 1] * nums[i]

            for i in range(len(nums)):
                if i:
                    lef_part = mult_forward[i - 1]
                else:
                    lef_part = 1

                if i < len(nums) - 1:
                    rigth_part = mult_backward[i + 1]
                else:
                    rigth_part = 1

                nums[i] = lef_part * rigth_part

        return nums


class Solution3:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
          [1, 2, 3,  4]
        -> 1, 1, 2, 6,
        <- 24, 12 , 4, 1
         [24, 12, 8, 6]
        """
        n_left = [1] * len(nums)
        n_right = [1] * len(nums)
        for i in range(1, len(n_right)):
            n_left[i] = n_left[i - 1] * nums[i - 1]

        for i in range(len(n_right) - 2, -1, -1):
            n_right[i] = n_right[i + 1] * nums[i + 1]

        for i in range(len(nums)):
            nums[i] = n_right[i] * n_left[i]

        return nums


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
          [1,  3,  2, 5]
        ->[1,  1,  3, 6]
        <-[30, 10, 5, 1]
          [30, 10, 15 6]
        """

        sup_nums = [1] * len(nums)
        for i in range(1, len(sup_nums)):
            sup_nums[i] = sup_nums[i - 1] * nums[i - 1]

        tmp_right = 1
        for i in reversed(range(len(nums))):
            sup_nums[i] = sup_nums[i] * tmp_right
            tmp_right *= nums[i]

        return sup_nums

#############
import unittest


class TestCase(unittest.TestCase):

    def test1(self):
        inp = [1, 2, 3, 4]
        out = [24, 12, 8, 6]
        res = Solution().productExceptSelf(inp)
        self.assertEqual(res, out)

    def test11(self):
        inp = [4, 5, 1, 8, 2]
        out = [80, 64, 320, 40, 160]
        res = Solution().productExceptSelf(inp)
        self.assertEqual(res, out)

    def test2(self):
        inp = [0, 0]
        out = [0, 0]
        res = Solution().productExceptSelf(inp)
        self.assertEqual(res, out)

    def test3(self):
        inp = [0, 0, 3, 2, 5, 0]
        out = [0, 0, 0, 0, 0, 0]
        res = Solution().productExceptSelf(inp)
        self.assertEqual(res, out)

    def test4(self):
        inp = [0, 3, 2, 5]
        out = [30, 0, 0, 0]
        res = Solution().productExceptSelf(inp)
        self.assertEqual(res, out)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
