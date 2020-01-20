"""
560. Subarray Sum Equals K

Solution 1 - O(n) time , O(n) space
Runtime: 108 ms, faster than 91.57% of Python3 online submissions for Subarray Sum Equals K.
Memory Usage: 15 MB, less than 96.00% of Python3 online submissions for Subarray Sum Equals K

Solution 2 - O(n^2) time , O(1) space
Time Limit Exceeded

leetcode solution - https://leetcode.com/problems/subarray-sum-equals-k/solution/
Python O(n) Based on "running_sum" concept of "Cracking the coding interview" book - https://leetcode.com/problems/subarray-sum-equals-k/discuss/190674/Python-O(n)-Based-on-%22running_sum%22-concept-of-%22Cracking-the-coding-interview%22-book
Python clear explanation with code and example - https://leetcode.com/problems/subarray-sum-equals-k/discuss/341399/Python-clear-explanation-with-code-and-example
Python, Simple with Explanation - https://leetcode.com/problems/subarray-sum-equals-k/discuss/102111/Python-Simple-with-Explanation

"""

from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sub_array_count = 0
        rolling_sum = 0
        cache = {0:1}
        for num in nums:
            rolling_sum += num
            if (rolling_sum - k) in cache:
                sub_array_count += cache[rolling_sum-k]
            cache[rolling_sum] = cache.get(rolling_sum, 0) + 1
        return sub_array_count


class Solution2:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sub_array_count = 0
        for start in range(len(nums)):
            current_sum = 0
            for end in range(start, len(nums)):
                current_sum += nums[end]
                if current_sum == k:
                    sub_array_count += 1
        return sub_array_count




#############
import unittest


class TestCase(unittest.TestCase):

    def test1(self):
        inp = [1,1,1]
        k = 2
        out = 2
        res = Solution().subarraySum(inp, k)
        self.assertEqual(res, out)

    def test2(self):
        inp = [1,3]
        k = 2
        out = 0
        res = Solution().subarraySum(inp, k)
        self.assertEqual(res, out)

    def test3(self):
        inp = []
        k = 2
        out = 0
        res = Solution().subarraySum(inp, k)
        self.assertEqual(res, out)

    def test4(self):
        inp = [1,2,3]
        k = 3
        out = 2
        res = Solution().subarraySum(inp, k)
        self.assertEqual(res, out)

    def test5(self):
        inp = [1]
        k = 0
        out = 0
        res = Solution().subarraySum(inp, k)
        self.assertEqual(res, out)

    def test6(self):
        inp = [-1,-1,1]
        # -1 -2 1

        k = 0
        out = 1
        res = Solution().subarraySum(inp, k)
        self.assertEqual(res, out)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)