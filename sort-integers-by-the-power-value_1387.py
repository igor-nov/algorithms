"""
1387. Sort Integers by The Power Value

Solution 1
Runtime: 812 ms, faster than 26.74% of Python3 online submissions for Sort Integers by The Power Value.
Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Sort Integers by The Power Value.

Solution 2
Runtime: 836 ms, faster than 24.30% of Python3 online submissions for Sort Integers by The Power Value.
Memory Usage: 13 MB, less than 100.00% of Python3 online submissions for Sort Integers by The Power Value.
Runtime: 808 ms, faster than 25.75% of Python3 online submissions for Sort Integers by The Power Value.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Sort Integers by The Power Value.

Solution 3
Runtime: 432 ms, faster than 51.49% of Python3 online submissions for Sort Integers by The Power Value.
Memory Usage: 74.9 MB, less than 100.00% of Python3 online submissions for Sort Integers by The Power Value.

Solutions
Just for fun - https://leetcode.com/problems/sort-integers-by-the-power-value/discuss/546573/Just-for-fun
Python Easy Solution Recursion and Sort with key= - https://leetcode.com/problems/sort-integers-by-the-power-value/discuss/548980/Python-Easy-Solution-Recursion-and-Sort-with-key
"""


class Solution1:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        hash_cache = {}
        for val in range(lo, hi + 1):
            hash_cache[val] = self.get_power(val)
        res = [val for val in sorted(hash_cache, key=lambda val: hash_cache[val])]
        return res[k - 1]

    def get_power(self, val):
        res = 0
        while val > 1:
            if val % 2:
                val = val * 3 + 1
            else:
                val = val / 2
            res += 1
        return res


import heapq


class Solution2:
    def getKth(self, lo: int, hi: int, k: int) -> int:

        power_cache = []
        for num in range(lo, hi + 1):
            power_cache.append((self.get_power(num), num))

        heapq.heapify(power_cache)
        while k:
            _, num = heapq.heappop(power_cache)
            k -= 1

        return num


    def get_power(self, val):
        res = 0
        while val > 1:
            if val % 2:
                val = val * 3 + 1
            else:
                val /= 2
            res += 1
        return res


from functools import lru_cache
class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:

        power_cache = []
        for num in range(lo, hi + 1):
            power_cache.append((self.get_power(num), num))

        heapq.heapify(power_cache)
        while k:
            _, num = heapq.heappop(power_cache)
            k -= 1

        return num

    @lru_cache(None)
    def get_power(self, val):
        if val == 1:
            return 0
        return 1 + (self.get_power(val*3+1) if val % 2 else self.get_power(val//2))



#############
import unittest


class TestCase(unittest.TestCase):

    def test1(self):
        lo = 12
        hi = 15
        k = 2
        out = 13
        res = Solution().getKth(lo, hi, k)
        self.assertEqual(res, out)

    def test2(self):
        lo = 1
        hi = 1
        k = 1
        out = 1
        res = Solution().getKth(lo, hi, k)
        self.assertEqual(res, out)

    def test3(self):
        lo = 7
        hi = 11
        k = 4
        out = 7
        res = Solution().getKth(lo, hi, k)
        self.assertEqual(res, out)

    def test4(self):
        lo = 10
        hi = 20
        k = 5
        out = 13
        res = Solution().getKth(lo, hi, k)
        self.assertEqual(res, out)

    def test5(self):
        lo = 1
        hi = 1000
        k = 777
        out = 570
        res = Solution().getKth(lo, hi, k)
        self.assertEqual(res, out)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
