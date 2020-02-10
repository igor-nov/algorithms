"""
1342. Number of Steps to Reduce a Number to Zero

Solution 1
Runtime: 28 ms, faster than 66.67% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.

Solution 2
Runtime: 28 ms, faster than 66.83% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.

Solution 3
Runtime: 24 ms, faster than 87.42% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.

Solution 4
Runtime: 20 ms, faster than 96.09% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.

Solutions
just count number of 0 and 1 in binary - https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/discuss/502809/just-count-number-of-0-and-1-in-binary
Clean Python 3, count bits in 2 lines - https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/discuss/502703/Clean-Python-3-count-bits-in-2-lines
"""


class Solution1:
    def numberOfSteps(self, num: int) -> int:
        res = 0
        while num:
            if num % 2:
                num -= 1
            else:
                num //= 2
            res += 1
        return res


class Solution2:
    def numberOfSteps(self, num: int) -> int:
        res = 0
        while num:
            # 0110 & 1 => 0
            # print((num & 1))
            if (num & 1) == 1:
                num -= 1
            else:
                num >>= 1
            res += 1
        return res


class Solution3:
    def numberOfSteps(self, num: int) -> int:
        res = 0
        while num:
            res += 2 if num & 1 else 1
            num >>= 1
        return res - 1


class Solution:
    def numberOfSteps(self, num: int) -> int:
        dig = f'{num:b}'
        return dig.count('1') - 1 + len(dig)

#####################

import unittest


class TestCase(unittest.TestCase):

    def test1(self):
        inp = 14
        out = 6
        res = Solution().numberOfSteps(inp)
        self.assertEqual(res, out)

    def test2(self):
        inp = 8
        out = 4
        res = Solution().numberOfSteps(inp)
        self.assertEqual(res, out)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
