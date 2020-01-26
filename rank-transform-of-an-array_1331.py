"""
1331. Rank Transform of an Array

Solution 1
Runtime: 620 ms, faster than 100.00% of Python3 online submissions for Rank Transform of an Array.
Memory Usage: 40 MB, less than 100.00% of Python3 online submissions for Rank Transform of an Array.

Solution 2
Runtime: 384 ms, faster than 100.00% of Python3 online submissions for Rank Transform of an Array.
Memory Usage: 30.6 MB, less than 100.00% of Python3 online submissions for Rank Transform of an Array.

Solution 3
Runtime: 372 ms, faster than 100.00% of Python3 online submissions for Rank Transform of an Array.
Memory Usage: 33.2 MB, less than 100.00% of Python3 online submissions for Rank Transform of an Array.

Solution 4

Python set+sorted+dict - https://leetcode.com/problems/rank-transform-of-an-array/discuss/489824/Python-set%2Bsorted%2Bdict
Clean Python 3 two lines - https://leetcode.com/problems/rank-transform-of-an-array/discuss/489733/Clean-Python-3-two-lines


"""
from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        if not arr:
            return arr

        cache = {}
        for idx, val in enumerate(arr):
            cache[val] = idx

        tmp = sorted(arr)
        # res = [1] * len(arr)
        res = {tmp[0]: 1}
        prev = 1
        for i in range(1, len(arr)):
            if tmp[i - 1] != tmp[i]:
                prev += 1
            res[tmp[i]] = prev

        for idx, val in enumerate(arr):
            arr[idx] = res[val]

        return arr


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        cache = {}
        idx = 1
        for num in sorted(arr):
            if not num in cache:
                cache[num] = idx
                idx += 1

        return [cache[num] for num in arr]


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        cache = {val: idx + 1 for idx, val in enumerate(sorted(set(arr)))}
        return [cache[val] for val in arr]

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        cache = {val: idx+1 for idx, val in enumerate(sorted(set(arr)))}
        return list(map(cache.get, arr))
        #return map(cache.get, arr)

#############
import unittest


class TestCase(unittest.TestCase):

    def test1(self):
        inp = [40, 10, 20, 30]
        out = [4, 1, 2, 3]
        res = Solution().arrayRankTransform(inp)
        self.assertEqual(res, out)

    def test2(self):
        inp = [100, 100, 100]
        out = [1, 1, 1]
        res = Solution().arrayRankTransform(inp)
        self.assertEqual(res, out)

    def test3(self):
        inp = [37, 12, 28, 9, 100, 56, 80, 5, 12]
        out = [5, 3, 4, 2, 8, 6, 7, 1, 3]
        res = Solution().arrayRankTransform(inp)
        self.assertEqual(res, out)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
