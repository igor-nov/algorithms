"""
556. Next Greater Element III

Solution 1
Runtime: 24 ms, faster than 82.03% of Python3 online submissions for Next Greater Element III.
Memory Usage: 12.5 MB, less than 100.00% of Python3 online submissions for Next Greater Element III.
Runtime: 32 ms, faster than 16.45% of Python3 online submissions for Next Greater Element III.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Next Greater Element III.

Solutions
Easy Python3 beats 100% - https://leetcode.com/problems/next-greater-element-iii/discuss/117208/Easy-Python3-beats-100
Simple Java solution (4ms) with explanation. - https://leetcode.com/problems/next-greater-element-iii/discuss/101824/Simple-Java-solution-(4ms)-with-explanation.
This problem is the same to Next Permutation, algorithm only. - https://leetcode.com/problems/next-greater-element-iii/discuss/101823/This-problem-is-the-same-to-Next-Permutation-algorithm-only.
"""


class Solution:
    def nextGreaterElement(self, n: int) -> int:

        # 12443322
        # 1 2 443322
        # 1 2 443 3 22
        # 1 3 443 2 22
        # 1 3 443222 -> 222344

        nums = list(map(int, str(n)))

        for i in range(len(nums) - 2, -1, -1):
            if nums[i + 1] > nums[i]:
                j = i + 1
                while j < len(nums) and nums[i] < nums[j]:
                    j += 1
                nums[i], nums[j - 1] = nums[j - 1], nums[i]
                nums[i + 1:] = nums[i + 1:][::-1]

                res = int(''.join(str(num) for num in nums))
                return res if res <= 2 ** 31 else -1

        return -1


import unittest


class TestCase(unittest.TestCase):

    def test1(self):
        inp = 12
        out = 21
        res = Solution().nextGreaterElement(inp)
        self.assertEqual(res, out)

    def test2(self):
        inp = 21
        out = -1
        res = Solution().nextGreaterElement(inp)
        self.assertEqual(res, out)

    def test3(self):
        inp = 4131
        out = 4311
        res = Solution().nextGreaterElement(inp)
        self.assertEqual(res, out)

    def test4(self):
        inp = 413166
        out = 413616
        res = Solution().nextGreaterElement(inp)
        self.assertEqual(res, out)

    def test5(self):
        inp = 230241
        out = 230412
        res = Solution().nextGreaterElement(inp)
        self.assertEqual(res, out)

    def test6(self):
        inp = 101
        out = 110
        res = Solution().nextGreaterElement(inp)
        self.assertEqual(res, out)

    def test7(self):
        inp = 12443322
        out = 13222344
        res = Solution().nextGreaterElement(inp)
        self.assertEqual(res, out)

    def test8(self):
        inp = 1999999999
        out = -1
        res = Solution().nextGreaterElement(inp)
        self.assertEqual(res, out)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
