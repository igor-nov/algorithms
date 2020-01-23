"""
46. Permutations

Complexity - CrackingTheCodinglnterview.com 16th Edition S1
What is the total runtime?
Since we are calling permutat ion 0 (n * n!) times (as an upper bound), and each one takes 0 (n) time,
the total runtime will not exceed O( n2 * n!).

Solution 1
Runtime: 44 ms, faster than 17.25% of Python3 online submissions for Permutations.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Permutations.

Solution 2 - using standard module
Runtime: 64 ms, faster than 6.20% of Python3 online submissions for Permutations.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Permutations.

Solution 3 (swap) - approx. same speed
Runtime: 40 ms, faster than 54.25% of Python3 online submissions for Permutations.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Permutations.

Solution 4 (swap) - approx same speed
Runtime: 40 ms, faster than 54.25% of Python3 online submissions for Permutations.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Permutations.

Solutions
Permutations - Backtracking - Algorithm - https://www.youtube.com/watch?v=AsxVqSKPo40
Permutations - Backtracking - Implementation - https://www.youtube.com/watch?v=eUnNw2lR01M


String Permutations - Understanding Recursion | Learn Algorithms with Phanto - https://www.youtube.com/watch?v=TnZHaH9i6-0
(string and array) - Interview Question: Permutations - https://www.youtube.com/watch?v=IPWmrjE1_MU&t=1010s
String permutation algorithm | All permutations of a string - https://youtu.be/GuTPwotSdYw?t=633
Permutations Of String | A Helpful Line-by-Line Code Tutorial - https://www.youtube.com/watch?v=KBHFyg2AcZ4


Simple Python solution (DFS). - https://leetcode.com/problems/permutations/discuss/18296/Simple-Python-solution-(DFS).
explanation + video https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/

"""

from typing import List


class Solution1:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.get_permutations(nums, res, [])
        return res

    def get_permutations(self, nums, res, permutation):
        if not nums:
            res.append(permutation)
        else:
            for i in range(len(nums)):
                self.get_permutations(nums[0:i] + nums[i + 1:], res, permutation + [nums[i]])


from itertools import permutations
class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return [list(permutation) for permutation in permutations(nums)]


class Solution4:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        self.get_permutations(nums, 0, res, [])
        return res

    def get_permutations(self, nums, pos, res, permutation):

        # print(f'input nums:{nums}, pos:{pos}, permutation:{permutation}')
        if pos == len(nums):
            res.append(permutation)
            # print(f'-->input nums:{nums}, pos:{pos}, permutation:{permutation}')
        else:
            for i in range(pos, len(nums)):
                nums[pos], nums[i] = nums[i], nums[pos]
                self.get_permutations(nums, pos + 1, res, permutation + [nums[pos]])
                nums[pos], nums[i] = nums[i], nums[pos]


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.get_permutations(nums, 0, res)
        return res

    def get_permutations(self, nums, pos, res):

        if pos == len(nums):
            res.append(nums[:])
        else:
            for idx in range(pos, len(nums)):
                nums[idx], nums[pos] = nums[pos], nums[idx]
                self.get_permutations(nums, pos + 1, res)
                nums[idx], nums[pos] = nums[pos], nums[idx]


inp = [1, 2, 3]
res = Solution().permute(inp)
print(res)

#############
import unittest


class TestCase(unittest.TestCase):

    def test1(self):
        inp = [1, 2, 3]
        out = [
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1]
        ]
        res = Solution().permute(inp)
        self.assertEqual(res, out)

    def test2(self):
        inp = [1, 2, 3, 4]
        out = [[1, 2, 3, 4], [1, 2, 4, 3], [1, 3, 2, 4], [1, 3, 4, 2], [1, 4, 2, 3], [1, 4, 3, 2], [2, 1, 3, 4],
               [2, 1, 4, 3], [2, 3, 1, 4], [2, 3, 4, 1], [2, 4, 1, 3], [2, 4, 3, 1], [3, 1, 2, 4], [3, 1, 4, 2],
               [3, 2, 1, 4], [3, 2, 4, 1], [3, 4, 1, 2], [3, 4, 2, 1], [4, 1, 2, 3], [4, 1, 3, 2], [4, 2, 1, 3],
               [4, 2, 3, 1], [4, 3, 1, 2], [4, 3, 2, 1]]
        res = Solution().permute(inp)
        self.assertEqual(res, out)

    def test3(self):
        inp = [0]
        out = [[0]]
        res = Solution().permute(inp)
        self.assertEqual(res, out)

    def test4(self):
        inp = []
        out = [[]]
        res = Solution().permute(inp)
        self.assertEqual(res, out)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
