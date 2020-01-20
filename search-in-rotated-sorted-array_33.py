"""
33. Search in Rotated Sorted Array

Solution 1 - search pivot On and binary search - wrong solution!!!
Runtime: 32 ms, faster than 96.30% of Python3 online submissions for Search in Rotated Sorted Array.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Search in Rotated Sorted Array.

Solution 2 - 2 nlog(n) -> one pass to find rotated idx, another - to find rotation position
Runtime: 36 ms, faster than 87.39% of Python3 online submissions for Search in Rotated Sorted Array.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Search in Rotated Sorted Array.


Solution 3 -one pass
Runtime: 32 ms, faster than 96.30% of Python3 online submissions for Search in Rotated Sorted Array.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Search in Rotated Sorted Array.

Solutions - @todo - check smart ideas below
The -INF and INF method but with a better explanation for dummies like me - https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/154836/The-INF-and-INF-method-but-with-a-better-explanation-for-dummies-like-me
Pretty short C++/Java/Ruby/Python - https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14419/Pretty-short-C%2B%2BJavaRubyPython
(check code in comment without xor) Pretty short C++/Java/Ruby/Python - https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14419/Pretty-short-C%2B%2BJavaRubyPython
(check comment with image) Revised Binary Search - https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14436/Revised-Binary-Search
Python binary search solution - O(logn) - 48ms - https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14437/Python-binary-search-solution-O(logn)-48ms
+https://leetcode.com/problems/search-in-rotated-sorted-array/solution/
"""

from typing import List


class Solution1:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        rot_pos = 0
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                rot_pos = i

        # print('rot_pos=', rot_pos)
        if nums[rot_pos] <= target <= nums[-1]:
            lo, hi = rot_pos, len(nums) - 1
        else:
            lo, hi = 0, rot_pos - 1

        res = self.binary_search(nums, lo, hi, target)
        return res

    def binary_search(self, nums, lo, hi, target):
        while lo < hi:
            med = (lo + hi) // 2
            # print(f'lo={lo},hi={hi},med={med}', nums[lo], nums[hi], nums[med], target)
            if nums[med] == target:
                return med
            elif nums[med] < target:
                lo = med + 1
            else:
                hi = med

        if lo == hi and nums[lo] == target:
            return lo

        return -1


class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        rotated_pos_st = self.get_rotated_pos(nums)

        if nums[rotated_pos_st] <= target <= nums[-1]:
            lo, hi = rotated_pos_st, len(nums) - 1
        else:
            # lo, hi = 0, max(rotated_pos_st - 1, 0)
            lo, hi = 0, rotated_pos_st - 1

        idx = self.binary_search(nums, lo, hi, target)
        return idx

    def get_rotated_pos(self, nums):
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            med = (lo + hi) // 2  # ->3(7) ; 4+6 // 2-> 5; 5+4// 2 ->4
            if nums[med] > nums[hi]:
                lo = med + 1  # 4
            else:
                hi = med  # -> 5 4
        return lo

    # reqursive
    def binary_search__(self, nums, lo, hi, target):
        if lo >= hi:
            return -1 if nums[lo] != target else lo

        med = lo + (hi - lo) // 2
        if nums[med] < target:
            return self.binary_search(nums, med + 1, hi, target)
            lo = med + 1
        elif nums[med] > target:
            return self.binary_search(nums, lo, med - 1, target)
        else:
            return med

    def binary_search(self, nums, lo, hi, target):
        while lo < hi:
            med = (lo + hi) // 2
            # print(f'lo {lo}: {nums[lo]}, med {med}: {nums[med]}, hi {hi}: {nums[hi]}')
            if nums[med] > target:
                hi = med - 1
            elif nums[med] < target:
                lo = med + 1
            else:
                return med

        return -1 if nums[lo] != target else lo


class Solution_variant2:
    def search(self, nums: List[int], target: int) -> int:

        if not nums:
            return -1

        lo, hi = 0, len(nums) - 1
        while lo < hi:
            med = (lo + hi) // 2
            # print(f'lo {lo}: {nums[lo]}, med {med}: {nums[med]}, hi {hi}: {nums[hi]}')
            if nums[med] == target:
                return med

            # 4, 5, 6, 7, 0, 1, 2 | med(7) search 6 -> target < med and med > nums[0]
            # 6, 7, 0, 1, 2 | med(0) search 7 -> target > med and med < nums[0]

            if nums[lo] <= nums[med]:
                if nums[lo] <= target < nums[med]:
                    hi = med - 1
                else:
                    lo = med + 1
            else:
                if nums[lo] <= target < nums[med]:
                    hi = med - 1
                else:
                    lo = med + 1

        # print(lo, hi, nums[lo], target, '\n')
        return lo if lo == hi and nums[lo] == target else -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        if not nums:
            return -1

        lo, hi = 0, len(nums) - 1
        while lo < hi:
            med = (lo + hi) // 2
            # print(f'lo {lo}: {nums[lo]}, med {med}: {nums[med]}, hi {hi}: {nums[hi]}')
            if nums[med] == target:
                return med

            # 4, 5, 6, 7, 0, 1, 2 | med(7) search 6 -> target < med and med > nums[0]
            # 6, 7, 0, 1, 2 | med(0) search 7 -> target > med and med < nums[0]

            if nums[lo] <= nums[med]:
                if nums[lo] <= target < nums[med]:
                    hi = med - 1
                else:
                    lo = med + 1
            else:
                if nums[med] < target <= nums[hi]:
                    lo = med + 1
                else:
                    hi = med - 1

        # print(lo, hi, nums[lo], target, '\n')
        return lo if lo == hi and nums[lo] == target else -1


#############
import unittest


class TestCase(unittest.TestCase):

    def test1(self):
        inp = [4, 5, 6, 7, 0, 1, 2]
        target = 0
        out = 4
        res = Solution().search(inp, target)
        self.assertEqual(res, out)

    def test2(self):
        inp = [0, 1, 2, 4, 5, 6, 7]
        target = 0
        out = 0
        res = Solution().search(inp, target)
        self.assertEqual(res, out)

    def test3(self):
        inp = [1, 2, 4, 5, 6, 7, 0]
        target = 0
        out = 6
        res = Solution().search(inp, target)
        self.assertEqual(res, out)

    def test4(self):
        inp = []
        target = 5
        out = -1
        res = Solution().search(inp, target)
        self.assertEqual(res, out)

    def test5(self):
        inp = [1, 3]
        target = 2
        out = -1
        res = Solution().search(inp, target)
        self.assertEqual(res, out)

    def test6(self):
        inp = [1]
        target = 0
        out = -1
        res = Solution().search(inp, target)
        self.assertEqual(res, out)

    def test7(self):
        inp = [5, 1, 3]
        target = 3
        out = 2
        res = Solution().search(inp, target)
        self.assertEqual(res, out)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
