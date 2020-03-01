"""
324. Wiggle Sort II

Solution 1
Runtime: 176 ms, faster than 74.30% of Python3 online submissions for Wiggle Sort II.
Memory Usage: 15.6 MB, less than 11.11% of Python3 online submissions for Wiggle Sort II.

!!!! it should run in on(n) time although runs much slower than internal sorting which is nLog(n)
Solution 2
Runtime: 1972 ms, faster than 5.11% of Python3 online submissions for Wiggle Sort II.
Memory Usage: 15.5 MB, less than 11.11% of Python3 online submissions for Wiggle Sort II.

Solution 3
Runtime: 2408 ms, faster than 5.11% of Python3 online submissions for Wiggle Sort II.
Memory Usage: 15.5 MB, less than 11.11% of Python3 online submissions for Wiggle Sort II.

Solutions
Python 3 lines simplest solution for everyone to understand - https://leetcode.com/problems/wiggle-sort-ii/discuss/155764/Python-3-lines-simplest-solution-for-everyone-to-understand


@todo - do it O(n) time O(1) space
Summary of the various solutions to Wiggle Sort for your reference - https://leetcode.com/problems/wiggle-sort-ii/discuss/77684/Summary-of-the-various-solutions-to-Wiggle-Sort-for-your-reference
Step by step explanation of index mapping in Java - https://leetcode.com/problems/wiggle-sort-ii/discuss/77682/Step-by-step-explanation-of-index-mapping-in-Java

3 lines Python, with Explanation / Proof - https://leetcode.com/problems/wiggle-sort-ii/discuss/77678/3-lines-Python-with-Explanation-Proof
Small half:    4 . 3 . 2 . 1 . 0 .
Large half:    . 9 . 8 . 7 . 6 . 5
----------------------------------
Together:      4 9 3 8 2 7 1 6 0 5

O(n)+O(1) after median --- Virtual Indexing - https://leetcode.com/problems/wiggle-sort-ii/discuss/77677/O(n)%2BO(1)-after-median-Virtual-Indexing

O(n)-time O(1)-space solution with detail explanations - https://leetcode.com/problems/wiggle-sort-ii/discuss/77681/O(n)-time-O(1)-space-solution-with-detail-explanations

Python, deterministic O(n) time + O(1) memory, quick select + "median of medians"  - https://leetcode.com/problems/wiggle-sort-ii/discuss/333079/Python-deterministic-O(n)-time-%2B-O(1)-memory-quick-select-%2B-%22median-of-medians%22
"""
from typing import List


class Solution1:
    def wiggleSort(self, nums: List[int]) -> None:

        tmp_nums = sorted(nums)
        for i in range(1, len(nums), 2):
            nums[i] = tmp_nums.pop()

        for i in range(0, len(nums), 2):
            nums[i] = tmp_nums.pop()


class Solution2:
    def wiggleSort(self, nums: List[int]) -> None:

        tmp_nums = nums[:]
        self.reorder(tmp_nums)

        for i in range(1, len(nums), 2):
            nums[i] = tmp_nums.pop()

        for i in range(0, len(nums), 2):
            nums[i] = tmp_nums.pop()

    def reorder(self, nums):
        med = len(nums) // 2
        lo, hi = 0, len(nums) - 1
        while True:
            med_lo, med_hi = self.do_partitioning(nums, lo, hi)
            if med_lo <= med <= med_hi:
                break
            elif med > med_hi:
                lo = med_hi + 1
            else:
                hi = med_lo - 1

    # 3 2 5 3 4 6
    # 3 2 6 3 4 5
    # 3 2 4 3 6 5
    # 3 2 3 4 6 5
    #
    def do_partitioning(self, nums, lo, hi):
        comp_idx = lo
        lo += 1
        j = lo

        while j <= hi:
            # print(lo, j, hi)
            if nums[j] > nums[comp_idx]:
                nums[j], nums[hi] = nums[hi], nums[j]
                hi -= 1
            elif nums[j] == nums[comp_idx]:
                j += 1
            else:
                nums[lo], nums[j] = nums[j], nums[lo]
                lo += 1
                j += 1
            # print(nums, nums[comp_idx], lo, hi)
        nums[comp_idx], nums[lo - 1] = nums[lo - 1], nums[comp_idx]
        return lo - 1, j - 1


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:

        tmp_nums = nums[:]
        self.partitioning_by_middle(tmp_nums)
        # print(tmp_nums)
        # print(sorted(tmp_nums))

        for i in range(1, len(nums), 2):
            nums[i] = tmp_nums.pop()

        for i in range(0, len(nums), 2):
            nums[i] = tmp_nums.pop()

    def partitioning_by_middle(self, nums):
        med = len(nums) // 2
        lo, hi = 0, len(nums) - 1
        while True:
            med_lo, med_hi = self.do_partitioning(nums, lo, hi)
            if med_lo <= med <= med_hi:
                break
            elif med > med_hi:
                lo = med_hi + 1
            else:
                hi = med_lo - 1

    def do_partitioning(self, nums, lo, hi):
        elem = nums[lo]
        j = lo + 1
        #print(nums,'---')
        while j <= hi:
            # print(lo, j, hi)
            if nums[j] > elem:
                nums[j], nums[hi] = nums[hi], nums[j]
                hi -= 1
            elif nums[j] == elem:
                j += 1
            else:
                nums[lo], nums[j] = nums[j], nums[lo]
                lo += 1
                j += 1
            #print(nums, elem, lo, j, hi)
        return lo, j-1


###########
import unittest


class TestCase(unittest.TestCase):
    unittest.skip

    def test1(self):
        nums = [1, 5, 1, 1, 6, 4]

        out = [1, 4, 1, 5, 1, 6]
        out = [1, 6, 1, 5, 1, 4]
        # out = [1,5,1,6,1,4]
        #out = [1, 5, 1, 4, 1, 6]

        res = Solution().wiggleSort(nums)
        self.assertEqual(nums, out)

    def test2(self):
        nums = [1, 3, 2, 2, 3, 1]
        out = [2, 3, 1, 3, 1, 2]
        res = Solution().wiggleSort(nums)
        self.assertEqual(nums, out)

    def test3(self):
        nums = [1, 2, 2, 1, 2, 1, 1, 1, 1, 2, 2, 2]
        out = [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2]
        res = Solution().wiggleSort(nums)
        self.assertEqual(nums, out)

    def test4(self):
        nums = [5, 3, 1, 2, 6, 7, 8, 5, 5]
        out = [5, 8, 5, 7, 3, 6, 2, 5, 1]
        out = [5, 6, 5, 7, 1, 8, 3, 5, 2]  # v2
        out = [5, 6, 5, 7, 2, 8, 1, 5, 3]  # v3
        res = Solution().wiggleSort(nums)
        self.assertEqual(nums, out)

    def test5(self):
        nums = [2, 1]
        out = [1, 2]
        res = Solution().wiggleSort(nums)
        self.assertEqual(nums, out)

    def test6(self):
        nums = [3, 2, 1, 1, 3, 2]
        out = [2, 3, 1, 3, 1, 2]
        res = Solution().wiggleSort(nums)
        self.assertEqual(nums, out)

    def test7(self):
        nums = [1, 2, 3, 2, 3, 3]
        out = [2,3,2,3,1,3]
        res = Solution().wiggleSort(nums)
        self.assertEqual(nums, out)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
