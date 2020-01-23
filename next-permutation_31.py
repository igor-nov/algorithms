"""
31. Next Permutation

Solution 1
Runtime: 76 ms, faster than 6.53% of Python3 online submissions for Next Permutation.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Next Permutation.

Solution 2 - same with explanations
Runtime: 64 ms, faster than 6.53% of Python3 online submissions for Next Permutation.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Next Permutation.

with manual reverse function !!!
Runtime: 36 ms, faster than 87.52% of Python3 online submissions for Next Permutation.
Memory Usage: 12.5 MB, less than 100.00% of Python3 online submissions for Next Permutation.

Solutions
https://leetcode.com/problems/next-permutation/solution/

C++ from Wikipedia - https://leetcode.com/problems/next-permutation/discuss/13867/C%2B%2B-from-Wikipedia
1 Find the largest index k such that nums[k] < nums[k + 1]. If no such index exists, just reverse nums and done.
2 Find the largest index l > k such that nums[k] < nums[l].
3 Swap nums[k] and nums[l].
4 Reverse the sub-array nums[k + 1:].

Share my O(n) time solution - https://leetcode.com/problems/next-permutation/discuss/13866/Share-my-O(n)-time-solution
Readable code without confusing i/j, and with explanation - https://leetcode.com/problems/next-permutation/discuss/13994/Readable-code-without-confusing-ij-and-with-explanation
Next lexicographical permutation algorithm - https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
Python solution with comments. - https://leetcode.com/problems/next-permutation/discuss/14054/Python-solution-with-comments.

Compute The Next Permutation of A Numeric Sequence - Case Analysis ("Next Permutation" on Leetcode) - https://www.youtube.com/watch?v=quAS1iydq7U
Coding Interview Problem: Permutation Generator - https://www.youtube.com/watch?v=V7hHupttzVk&t=211s

"""

## 1 find strongly decreasing sequence
## 2 prev character is our root to switch
## 3 find next character to switch in 1st sequence
## 4 swap 2 and 3
## 5 reverse - 1st sequence -> do it strongly increasing

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        root = None
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                root = i
                break

        if root is not None:
            replace_el = None
            for i in range(root + 1, len(nums)):
                if nums[i] > nums[root]:
                    replace_el = i
                    #break
            nums[replace_el], nums[root] = nums[root], nums[replace_el]
            nums[root+1:] = nums[root+1:][::-1]
        else:
            #nums.sort(reverse=True)
            nums.sort()


"""
1. 6 2 1 5 4 3
find  1
2. find 3 (smallest element in [5 4 3] which is bigger than 1)
3. swap 1 and 3 - > 6 2 3 5 4 1
4 . reverse 5 4 1 ->  6 2 3 1 4 5

"""
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:

        # find place where sequence is not increasing in ascending order from right to left
        next_permutation_pos = None
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i+1]:
                next_permutation_pos = i
                break
        if next_permutation_pos is not None:
            for i in range(next_permutation_pos+1, len(nums)):
                if nums[next_permutation_pos] < nums[i]:
                    swap_with = i
            nums[swap_with], nums[next_permutation_pos] = nums[next_permutation_pos], nums[swap_with]

            #nums[next_permutation_pos+1:] = nums[next_permutation_pos+1:][::-1]
            self.reverse_part(nums, next_permutation_pos+1, len(nums)-1)

        else:
            #all elements descending order
            nums.sort()

    def reverse_part(self, nums, st, end):
        while st < end:
            nums[st], nums[end] = nums[end], nums[st]
            st += 1
            end -= 1


#############
import unittest


class TestCase(unittest.TestCase):

    def test1(self):
        inp = [1, 2, 3]
        out = [1, 3, 2]
        Solution().nextPermutation(inp)
        self.assertEqual(inp, out)

    def test2(self):
        inp = [3, 2, 1]
        out = [1, 2, 3]
        Solution().nextPermutation(inp)
        self.assertEqual(inp, out)

    def test3(self):
        inp = [1, 1, 5]
        out = [1, 5, 1]
        Solution().nextPermutation(inp)
        self.assertEqual(inp, out)

    def test4(self):
        inp = [1,2]
        out = [2, 1]
        Solution().nextPermutation(inp)
        self.assertEqual(inp, out)


    def test5(self):
        inp = [1,3,2]
        out = [2,1,3]
        Solution().nextPermutation(inp)
        self.assertEqual(inp, out)


    def test6(self):
        inp = [2,3,1]
        out = [3,1,2]
        Solution().nextPermutation(inp)
        self.assertEqual(inp, out)


    def test7(self):
        inp = [6, 2, 1, 5, 4, 3]
        out = [6, 2, 3, 1, 4, 5]
        Solution().nextPermutation(inp)
        self.assertEqual(inp, out)

    def test8(self):
        inp = [6, 2, 1, 5, 4, 3, 0]
        out = [6, 2, 3, 0, 1, 4, 5]
        Solution().nextPermutation(inp)
        self.assertEqual(inp, out)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
