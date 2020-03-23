"""
1385. Find the Distance Value Between Two Arrays
really strange issue

Solution 1
Runtime: 108 ms, faster than 16.67% of Python3 online submissions for Find the Distance Value Between Two Arrays.
Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Find the Distance Value Between Two Arrays.

Solution 2 - @todo - think about it
Runtime: 124 ms, faster than 16.67% of Python3 online submissions for Find the Distance Value Between Two Arrays.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Find the Distance Value Between Two Arrays.

Solution 3 - most officiant - @todo - think about it
Runtime: 72 ms, faster than 100.00% of Python3 online submissions for Find the Distance Value Between Two Arrays.
Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Find the Distance Value Between Two Arrays.


Solutions
[Python], two pointers O(n log n) - https://leetcode.com/problems/find-the-distance-value-between-two-arrays/discuss/546501/Python-two-pointers-O(n-log-n)



"""
from typing import List


class Solution1:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:

        res = 0
        for item1 in arr1:
            is_expected = True
            for item2 in arr2:
                abs_val = abs(item1 - item2)
                if abs_val <= d:
                    is_expected = False
                    break
            if is_expected:
                res += 1
        return res


import bisect


class Solution2:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:

        res = 0
        arr2.sort()
        print('\n----')
        print(f'arr1:{arr1}')
        print(f'arr2:{arr2}')
        print(f'd:{d}')
        for item1 in arr1:
            item_to_find = item1 - d
            idx = bisect.bisect_left(arr2, item_to_find)

            print(
                f'item1:{item1}, item1-d:{item_to_find}, idx to insert:{idx}, arr2[idx]:{arr2[idx] if idx < len(arr2) else "end"}')
            if idx >= len(arr2) or abs(item1 - arr2[idx]) > d:
                res += 1
                print('true')
        return res


class Solution3:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:

        arr1.sort()
        arr2.sort()

        hi_i, hi_j = len(arr1), len(arr2)
        i = j = res = 0
        while i < hi_i and j < hi_j:
            if arr1[i] >= arr2[j]:
                if arr1[i] - arr2[j] > d:
                    j += 1
                else:
                    i += 1
            else:
                if arr2[j] - arr1[i] > d:
                    i += 1
                    res += 1
                else:
                    i += 1

        res += hi_i - i
        return res


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:

        res = 0
        for item1 in arr1:
            is_expected = True
            for item2 in arr2:
                abs_val = abs(item1 - item2)
                if abs_val <= d:
                    is_expected = False
                    break
            if is_expected:
                res += 1
        return res


#############
import unittest


class TestCase(unittest.TestCase):

    def test1(self):
        arr1 = [4, 5, 8]
        arr2 = [10, 9, 1, 8]
        d = 2
        out = 2
        res = Solution().findTheDistanceValue(arr1, arr2, d)
        self.assertEqual(res, out)

    def test2(self):
        arr1 = [1, 4, 2, 3]
        arr2 = [-4, -3, 6, 10, 20, 30]
        d = 3
        out = 2
        res = Solution().findTheDistanceValue(arr1, arr2, d)
        self.assertEqual(res, out)

    def test3(self):
        arr1 = [2, 1, 100, 3]
        arr2 = [-5, -2, 10, -3, 7]
        d = 6
        out = 1
        res = Solution().findTheDistanceValue(arr1, arr2, d)
        self.assertEqual(res, out)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
