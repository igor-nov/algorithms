"""
42. Trapping Rain Water

##Array     ##Two Pointers    ##Stack


Solution 1 - O(n) time - O(n) space (2n)
Runtime: 56 ms, faster than 39.27% of Python3 online submissions for Trapping Rain Water.
Memory Usage: 13.2 MB, less than 100.00% of Python3 online submissions for Trapping Rain Water.

Solution 2 - just one suplementary array
Runtime: 56 ms, faster than 39.27% of Python3 online submissions for Trapping Rain Water.
Memory Usage: 13.3 MB, less than 97.67% of Python3 online submissions for Trapping Rain Water.

Solution 3 O(n) time O(1) space
Runtime: 48 ms, faster than 83.23% of Python3 online submissions for Trapping Rain Water.
Memory Usage: 13.2 MB, less than 100.00% of Python3 online submissions for Trapping Rain Water.

Solution 4 - easy to read solution 3
Runtime: 52 ms, faster than 61.99% of Python3 online submissions for Trapping Rain Water.
Memory Usage: 13.3 MB, less than 100.00% of Python3 online submissions for Trapping Rain Water

Solution 5 -- !!!!!!!
Runtime: 40 ms, faster than 98.68% of Python3 online submissions for Trapping Rain Water.
Memory Usage: 13.4 MB, less than 97.67% of Python3 online submissions for Trapping Rain Water.

Solution 6 - stack
Runtime: 44 ms, faster than 95.49% of Python3 online submissions for Trapping Rain Water.
Memory Usage: 13.3 MB, less than 97.67% of Python3 online submissions for Trapping Rain Water.

Solutions
Programming Interview Question: Trapping Rain Water between Towers Problem - https://www.youtube.com/watch?v=KV-Eq3wYjxI
Trapping Rain Water Python Walkthrough (Leetcode #42) - https://www.youtube.com/watch?v=qn-wuF24X1w
(photo in comments) Share my short solution. - https://leetcode.com/problems/trapping-rain-water/discuss/17391/Share-my-short-solution.
Java, O(n) time and O(1) space (with explanations). - https://leetcode.com/problems/trapping-rain-water/discuss/153992/Java-O(n)-time-and-O(1)-space-(with-explanations).

stack
This is just same as LC84. Monotonic stack - https://leetcode.com/problems/trapping-rain-water/discuss/201541/This-is-just-same-as-LC84.-Monotonic-stack
https://leetcode.com/problems/trapping-rain-water/solution/
A stack based solution for reference, inspired by Histogram - https://leetcode.com/problems/trapping-rain-water/discuss/17414/A-stack-based-solution-for-reference-inspired-by-Histogram
Stack with Explanation (Java / Python / Scala) - https://leetcode.com/problems/trapping-rain-water/discuss/178028/Stack-with-Explanation-(Java-Python-Scala)
"""
from typing import List


class Solution1:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        left_max = [None] * len(height)
        right_max = [None] * len(height)

        for i in range(len(height)):
            left_max[i] = max(height[i], left_max[i - 1]) if i else height[i]

        for i in range(len(height) - 1, -1, -1):
            right_max[i] = max(height[i], right_max[i + 1]) if i < len(height) - 1 else height[i]

        total_sum = 0
        for i in range(1, len(height) - 1):
            total_sum += max(0, min(left_max[i - 1], right_max[i + 1]) - height[i])

        return total_sum


class Solution2:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        right_max = [None] * len(height)
        for i in range(len(height) - 1, -1, -1):
            right_max[i] = max(height[i], right_max[i + 1]) if i < len(height) - 1 else height[i]

        total_sum = 0
        left_max = height[0]
        for i in range(1, len(height) - 1):
            total_sum += max(0, min(left_max, right_max[i + 1]) - height[i])
            left_max = max(left_max, height[i])

        return total_sum

class Solution3:
    def trap(self, height: List[int]) -> int:
        if len(height) < 3:
            return 0

        left_max, right_max = height[0], height[-1]
        lo, hi = 0, len(height) - 1
        sum_total = 0

        while lo < hi:

            if height[lo] < height[hi]:
                if height[lo] > left_max:
                    left_max = height[lo]
                else:
                    sum_total += left_max - height[lo]
                lo += 1
            else:
                if height[hi] > right_max:
                    right_max = height[hi]
                else:
                    #sum_total += min(left_max, right_max) - height[hi]
                    sum_total += right_max - height[hi]
                hi -= 1


        return sum_total

class Solution4:
    def trap(self, height: List[int]) -> int:

        lo, hi = 0, len(height)-1
        left_max, right_max = 0, 0
        sum_total = 0
        while lo < hi:
            left_max = max(left_max, height[lo])
            right_max = max(right_max, height[hi])

            if left_max < right_max:
                sum_total += max(left_max - height[lo+1], 0)
                lo += 1
            else:
                sum_total += max(right_max - height[hi - 1], 0)
                hi -= 1

        return sum_total

class Solution5:
    def trap(self, height: List[int]) -> int:

        lo, hi = 0, len(height)-1
        left_max, right_max = 0, 0
        sum_total = 0

        while lo < hi:
            left_max = max(left_max, height[lo])
            right_max = max(right_max, height[hi])
            if left_max < right_max:
                sum_total += left_max - height[lo]
                lo += 1
            else:
                sum_total += right_max - height[hi]
                hi -= 1
        return sum_total


class Solution:
    def trap(self, height: List[int]) -> int:
        # [0,1,0,2,1,0,1,3,2,1,2,1]
        # [0(0)]
        # 1
        # [] -> 0(0)
        # top = 0(0)
        # st empty -> continue
        # 1[1(1)]
        # 2 [1(1), 2(0)]
        # 3(2) [1(1), 2(0)] -> 2 > 0 ? ->
        # top -> 2(0)
        # [1(1)]
        # dist -> current(3) - st[-1](1)-1 = 1
        #area = min(h[st[-1], h[current]) * 1 -> 1
        stack, res = [], 0
        for right_idx in range(len(height)):
            while stack and height[stack[-1]] < height[right_idx]:
                current_idx = stack.pop()
                if not stack:
                    break
                dist = right_idx - stack[-1] - 1 # stack[-1]  -> left boundary
                current_height = min(height[right_idx], height[stack[-1]]) - height[current_idx]
                res += dist * current_height
            stack.append(right_idx)
        return res

#####################
import unittest


class TestSolution(unittest.TestCase):

    def test_1(self):
        inp = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        out = 6
        res = Solution().trap(inp)
        self.assertEqual(res, out)

    def test_2(self):
        inp = []
        out = 0
        res = Solution().trap(inp)
        self.assertEqual(res, out)

    def test_3(self):
        inp = [2, 0, 2]
        out = 2
        res = Solution().trap(inp)
        self.assertEqual(res, out)

    def test_4(self):
        inp = [2, 1, 0, 2]
        out = 3
        res = Solution().trap(inp)
        self.assertEqual(res, out)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
