"""
15. 3Sum

Solution 1
Runtime: 2336 ms, faster than 6.34% of Python3 online submissions for 3Sum.
Memory Usage: 17 MB, less than 25.00% of Python3 online submissions for 3Sum.

Solution 2 - optimized 1
Runtime: 1384 ms, faster than 28.46% of Python3 online submissions for 3Sum.
Memory Usage: 16.1 MB, less than 100.00% of Python3 online submissions for 3Sum.

Solution 3 - optimized 2
Runtime: 632 ms, faster than 95.53% of Python3 online submissions for 3Sum.
Memory Usage: 16.2 MB, less than 100.00% of Python3 online submissions for 3Sum.

Solution

My Python solution based on 2 sum, 200 ms beat 93.37% - https://leetcode.com/problems/3sum/discuss/7384/My-Python-solution-based-on-2-sum-200-ms-beat-93.37

Best Python Solution (Explained) - https://leetcode.com/problems/3sum/discuss/232712/Best-Python-Solution-(Explained)
Python solution with detailed explanation - https://leetcode.com/problems/3sum/discuss/7498/Python-solution-with-detailed-explanation

"""

from typing import List


class Solution1:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for lo in range(len(nums) - 2):
            pointer, hi = lo + 1, len(nums) - 1
            while pointer < hi:
                current_sum = nums[lo] + nums[pointer] + nums[hi]
                if current_sum == 0:
                    res.add((nums[lo], nums[pointer], nums[hi]))
                    hi -= 1
                elif current_sum > 0:
                    hi -= 1
                else:
                    pointer += 1

        return [list(item) for item in res]


class Solution2(object):

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        lLen = len(nums)

        if lLen < 3:
            return []

        # we need to sort array ~ O(nLogn) in order to properly handle duplicates and 2 pointers approach
        nums.sort()
        triples = []

        for i in range(lLen - 2):

            # since it's sorted array there's no reason to check sum
            # if we got to element greater than 0
            # sum will be greater than 0 any case
            if nums[i] > 0:
                break

            # in case if previous value the same as current
            # sum will consists of the same elements
            # so we need to skip current in order to avoid duplicates
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            lo = i + 1
            hi = lLen - 1

            while lo < hi:

                # check in case we move to num with same value as on previous step in order to remove duplicates
                if lo > i + 1 and nums[lo] == nums[lo - 1]:
                    lo += 1
                    continue

                # check in case we move to num with same value as on previous step in order to remove duplicates
                if hi < lLen - 1 and nums[hi] == nums[hi + 1]:
                    hi -= 1
                    continue

                sum3 = nums[i] + nums[lo] + nums[hi]

                if sum3 == 0:
                    triples.append([nums[i], nums[lo], nums[hi]])
                    lo += 1
                    hi -= 1

                # since it's sorted array we can drive in what direction we can move
                elif sum3 < 0:
                    lo += 1
                else:
                    hi -= 1

        return triples


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for x in range(len(nums) - 2):

            if x and nums[x] == nums[x - 1]:
                continue

            if nums[x] > 0:
                break

            target = -nums[x]
            y, z = x + 1, len(nums) - 1

            while y < z:
                sum2 = nums[y] + nums[z]

                if sum2 == target:
                    res.append([nums[x], nums[y], nums[z]])

                    while y < z and nums[y] == nums[y + 1]:
                        y += 1

                    while y < z and nums[z] == nums[z - 1]:
                        z -= 1

                    y += 1
                    z -= 1

                elif sum2 > target:
                    z -= 1

                else:
                    y += 1

        return res


class Solution_:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        # res = []

        for x in range(len(nums) - 2):
            # next_ = [nums[i] - nums[x] for i, val in enumerate(nums[x + 1:])]
            # next_ = nums[x + 1:]
            val_x = nums[x]
            cache = {}
            for y in range(x + 1, len(nums)):
                # print(-nums[y],cache)
                if -nums[y] in cache:
                    item = tuple(list(cache[-nums[y]]) + [nums[y]])
                    # print('item=', item)
                    res.add(item)
                    # res.append( (list(cache[-nums[y]]) + [nums[y]]) )
                cache[nums[x] + nums[y]] = tuple([nums[x], nums[y]])

        """
        [-2, 0, 1, 1, 2]
             2  3  3  4
             
             0 1 1 2 
        """
        # for x in range(len(nums) - 2):
        #     next_ = [nums[i] - nums[x] for i, val in enumerate(nums[x + 1:])]
        #     #next_ = nums[x + 1:]
        #     val_x = nums[x]
        #     cache = {}
        #     for y in range(len(next_)):
        #         if -next_[y] in cache:
        #             res.add(cache[-next_[y]].add(y))
        #         cache[next_[y]+val_x] = set([x,y])
        #

        # print(res)
        return [list(item) for item in res]


#############
import unittest


class TestCase(unittest.TestCase):

    def test1(self):
        inp = [-1, 0, 1, 2, -1, -4]
        out = [

            [-1, -1, 2],
            [-1, 0, 1],
        ]
        res = Solution().threeSum(inp)
        self.assertEqual(res, out)

    def test2(self):
        inp = [-2, 0, 1, 1, 2]
        #out = [[-2, 1, 1], [-2, 0, 2]]
        out = [[-2, 0, 2], [-2, 1, 1]]
        res = Solution().threeSum(inp)
        self.assertEqual(res, out)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
