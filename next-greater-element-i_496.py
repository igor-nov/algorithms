"""
496. Next Greater Element I

Solution 1
Runtime: 156 ms, faster than 9.79% of Python3 online submissions for Next Greater Element I.
Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Next Greater Element I.

Solution 2
Runtime: 48 ms, faster than 66.32% of Python3 online submissions for Next Greater Element I.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Next Greater Element I.
Runtime: 44 ms, faster than 86.81% of Python3 online submissions for Next Greater Element I.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Next Greater Element I

Solution 3 - same as 2 but without defaultdict
Runtime: 40 ms, faster than 96.87% of Python3 online submissions for Next Greater Element I.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Next Greater Element I.
Runtime: 48 ms, faster than 66.32% of Python3 online submissions for Next Greater Element I.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Next Greater Element I.

Solutions
next greater element (use of stack) - https://www.youtube.com/watch?v=uFso48YRRao
Next greater element in an array - https://www.youtube.com/watch?v=8P-Z7Oc8x9I
LeetCode Next Greater Element I Solution Explained - Java - https://www.youtube.com/watch?v=8BDKB2yuGyg
Java 10 lines linear time complexity O(n) with explanation -https://leetcode.com/problems/next-greater-element-i/discuss/97595/Java-10-lines-linear-time-complexity-O(n)-with-explanation
Python solution with detailed explanation - https://leetcode.com/problems/next-greater-element-i/discuss/97620/Python-solution-with-detailed-explanation


"""

from typing import List


class Solution1:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)

        for idx, num1 in enumerate(nums1):
            is_next = False
            for num2 in nums2:
                if is_next and num2 > num1:
                    res[idx] = num2
                    break
                if num1 == num2:
                    is_next = True

        return res


from collections import defaultdict


class Solution2:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # [2, 4, 1, 5]
        # [2] < 4 -> 2 : 4 ===> [4]
        # [4] > 1 => [4,1]
        # [4,1] < 5 => 1:4; [4] < 5 => 4:5 ===> [5]
        # [5]
        next_great_elem = defaultdict(lambda: -1)
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                next_great_elem[stack.pop()] = num
            stack.append(num)

        res = []
        for num in nums1:
            res.append(next_great_elem[num])

        return res


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater_elem = {}
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater_elem[stack.pop()] = num
            stack.append(num)

        res = []
        for num in nums1:
            res.append(next_greater_elem.get(num, -1))
        return res


import unittest


class TestCase(unittest.TestCase):

    def test1(self):
        nums1 = [4, 1, 2]
        nums2 = [1, 3, 4, 2]
        out = [-1, 3, -1]
        res = Solution().nextGreaterElement(nums1, nums2)
        self.assertEqual(res, out)

    def test2(self):
        nums1 = [2, 4]
        nums2 = [1, 2, 3, 4]
        out = [3, -1]
        res = Solution().nextGreaterElement(nums1, nums2)
        self.assertEqual(res, out)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
