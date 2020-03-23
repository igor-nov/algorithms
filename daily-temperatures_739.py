"""
739. Daily Temperatures

Solution 1
Runtime: 480 ms, faster than 92.43% of Python3 online submissions for Daily Temperatures.
Memory Usage: 16.9 MB, less than 34.21% of Python3 online submissions for Daily Temperatures.

Solution 2 - reverse order
Runtime: 496 ms, faster than 69.99% of Python3 online submissions for Daily Temperatures.
Memory Usage: 16.9 MB, less than 34.21% of Python3 online submissions for Daily Temperatures.
Runtime: 476 ms, faster than 95.00% of Python3 online submissions for Daily Temperatures.
Memory Usage: 16.9 MB, less than 34.21% of Python3 online submissions for Daily Temperatures.

Solutions
[Java] Easy AC Solution with Stack - https://leetcode.com/problems/daily-temperatures/discuss/109832/Java-Easy-AC-Solution-with-Stack
javascript stack solution with explaination - https://leetcode.com/problems/daily-temperatures/discuss/157886/javascript-stack-solution-with-explaination
Python:4 different solutions, from easy to elegant - https://leetcode.com/problems/daily-temperatures/discuss/275884/Python%3A4-different-solutions-from-easy-to-elegant
"""

from typing import List


class Solution1:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack, res = [], [0] * len(T)
        # [] , [0, 0, 0, 0, 0, 0, 0, 0]

        # [73, 74, 75, 71, 69, 72, 76, 73]
        # [0] , [0, 0, 0, 0, 0, 0, 0, 0]
        # [1] , [1, 0, 0, 0, 0, 0, 0, 0]
        # [2] , [1, 1, 0, 0, 0, 0, 0, 0]
        # [2,3] , [1, 1, 0, 0, 0, 0, 0, 0]
        # [2,3,4] , [1, 1, 0, 0, 0, 0, 0, 0]
        # [2,3] , [1, 1, 0, 0, 1, 0, 0, 0] -> 4 : 5-4 =>1
        # [2,5] , [1, 1, 0, 2, 1, 0, 0, 0] -> 3 : 5-3 =>2
        # [2] , [1, 1, 0, 2, 1, 1, 0, 0] -> 5 : 6-5 =>1
        # [6] , [1, 1, 4, 2, 1, 1, 0, 0] -> 2 : 6-2 =>4

        for i in range(len(T)):
            while stack and T[stack[-1]] < T[i]:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)
        return res


class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack, res = [], [0] * len(T)
        # [] , [0, 0, 0, 0, 0, 0, 0, 0]

        # [73, 74, 75, 71, 69, 72, 76, 73]
        # [7], [0, 0, 0, 0, 0, 0, 0, 0]
        # [6], [0, 0, 0, 0, 0, 0, 0, 0]
        # [6,5], [0, 0, 0, 0, 0, 1, 0, 0] 72 < 76 => 6-5
        # [6,5,4], [0, 0, 0, 0, 1, 1, 0, 0] 69 < 72 => 5-4
        # [6,5,4], [0, 0, 0, 0, 1, 1, 0, 0] 4=>pop
        # [6,5,3], [0, 0, 0, 2, 1, 1, 0, 0] 71 < 72 => 5-3 => 2
        # [6,5,3], [0, 0, 0, 2, 1, 1, 0, 0] 3=>pop 75 > 71
        # [6], [0, 0, 0, 2, 1, 1, 0, 0] 5=>pop 75 > 72
        # [6,2], [0, 0, 4, 2, 1, 1, 0, 0] 75 < 76 => 6-2 =>4
        # [6,2], [0, 1, 4, 2, 1, 1, 0, 0] 74 < 75 => 2-1 =>1
        # [6,2], [1, 1, 4, 2, 1, 1, 0, 0] 73 < 74 => 1-0 =>1

        for i in range(len(T) - 1, -1, -1):
            while stack and T[stack[-1]] <= T[i]:
                stack.pop()
            if stack:
                res[i] = stack[-1] - i
            stack.append(i)
        return res


import unittest


class TestCase(unittest.TestCase):

    def test1(self):
        inp = [73, 74, 75, 71, 69, 72, 76, 73]
        out = [1, 1, 4, 2, 1, 1, 0, 0]
        res = Solution().dailyTemperatures(inp)
        self.assertEqual(res, out)

    def test2(self):
        inp = [89, 62, 70, 58, 47, 47, 46, 76, 100, 70]
        out = [8, 1, 5, 4, 3, 2, 1, 1, 0, 0]
        res = Solution().dailyTemperatures(inp)
        self.assertEqual(res, out)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
