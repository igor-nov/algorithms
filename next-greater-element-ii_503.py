"""
503. Next Greater Element II

Solution 1
Runtime: 228 ms, faster than 81.34% of Python3 online submissions for Next Greater Element II.
Memory Usage: 15.1 MB, less than 52.00% of Python3 online submissions for Next Greater Element II.

Solution 2 - same as above, but less space
Runtime: 232 ms, faster than 75.97% of Python3 online submissions for Next Greater Element II.
Memory Usage: 14.7 MB, less than 56.00% of Python3 online submissions for Next Greater Element II.

Solution 3 - even less space
Runtime: 220 ms, faster than 89.03% of Python3 online submissions for Next Greater Element II.
Memory Usage: 14.4 MB, less than 96.00% of Python3 online submissions for Next Greater Element II.

Solution 4
Runtime: 268 ms, faster than 33.29% of Python3 online submissions for Next Greater Element II.
Memory Usage: 14.4 MB, less than 96.00% of Python3 online submissions for Next Greater Element II.

Solution 4 - just duplicate stack
Runtime: 224 ms, faster than 85.16% of Python3 online submissions for Next Greater Element II.
Memory Usage: 14.5 MB, less than 84.00% of Python3 online submissions for Next Greater Element II.

Solution 5 - just
Runtime: 216 ms, faster than 92.84% of Python3 online submissions for Next Greater Element II.
Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for Next Greater Element II.
Runtime: 216 ms, faster than 92.84% of Python3 online submissions for Next Greater Element II.
Memory Usage: 14.3 MB, less than 100.00% of Python3 online submissions for Next Greater Element II.

Solutions
[Java/C++/Python] Loop Twice - https://leetcode.com/problems/next-greater-element-ii/discuss/98270/JavaC%2B%2BPython-Loop-Twice
Python solution with detailed explanation - https://leetcode.com/problems/next-greater-element-ii/discuss/98328/Python-solution-with-detailed-explanation
@todo - Python beats 100% https://leetcode.com/problems/next-greater-element-ii/discuss/145374/Python-beats-100


"""

from typing import List


class Solution1:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        cache, stack = {}, []
        for idx, num in enumerate(nums):
            while stack and stack[-1][1] < num:
                cache[(stack.pop())] = num
            stack.append((idx, num))

        for idx, num in enumerate(nums):
            while stack and stack[-1][1] < num:
                cache[stack.pop()] = num

        res = []
        for idx, num in enumerate(nums):
            res.append(cache.get((idx, num), -1))

        return res


class Solution2:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        cache, stack = {}, []

        for idx, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                cache[stack.pop()] = num
            stack.append(idx)

        for idx, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                cache[stack.pop()] = num

        res = []
        for idx, num in enumerate(nums):
            res.append(cache.get(idx, -1))

        return res


class Solution3:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        stack = []

        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                res[stack.pop()] = nums[i]
            stack.append(i)

        for i in range(len(nums)):
            if not stack:
                break
            while res[stack[-1]] == -1 and stack and nums[stack[-1]] < nums[i]:
                res[stack.pop()] = nums[i]


class Solution4:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res, stack = [-1] * len(nums), []

        for i in range(len(nums) * 2):
            idx = i % len(nums)
            while stack and nums[stack[-1]] < nums[idx]:
                res[stack.pop()] = nums[idx]
            stack.append(i % len(nums))

        return res


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res, stack = [-1] * len(nums), nums[::-1]

        for i in range(len(nums)-1, -1, -1):
            while stack and stack[-1] <= nums[i]:
                stack.pop()

            if stack:
                res[i] = stack[-1]

            stack.append(nums[i])

        return res



import unittest


class TestCase(unittest.TestCase):

    def test1(self):
        inp = [1, 2, 1]
        out = [2, -1, 2]
        res = Solution().nextGreaterElements(inp)
        self.assertEqual(res, out)

    def test2(self):
        inp = [100, 1, 11, 1, 120, 111, 123, 1, -1, -100]
        out = [120, 11, 120, 120, 123, 123, -1, 100, 100, 100]
        res = Solution().nextGreaterElements(inp)
        self.assertEqual(res, out)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
