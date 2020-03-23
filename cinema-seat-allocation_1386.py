"""

Solution1
# Time Limit Exceeded

Solution 2
Runtime: 1532 ms, faster than 20.00% of Python3 online submissions for Cinema Seat Allocation.
Memory Usage: 15.4 MB, less than 100.00% of Python3 online submissions for Cinema Seat Allocation.

Solution 3
Runtime: 688 ms, faster than 82.08% of Python3 online submissions for Cinema Seat Allocation.
Memory Usage: 16.6 MB, less than 100.00% of Python3 online submissions for Cinema Seat Allocation.

Solutions
[Python] Group reserved seats by row using hash map
https://leetcode.com/problems/cinema-seat-allocation/discuss/546495/Python-Group-reserved-seats-by-row-using-hash-map

Python BitMask - @todo bitmask
https://leetcode.com/problems/cinema-seat-allocation/discuss/547636/Python-BitMask

"""
from typing import List

import heapq


class Solution1:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:

        heapq.heapify(reservedSeats)
        res = 0

        for row in range(1, n + 1):
            row_reserved = [0] * 10

            while reservedSeats and reservedSeats[0][0] == row:
                curr_row, seat = heapq.heappop(reservedSeats)
                row_reserved[seat - 1] = 1

            res += self.getAllocations(row_reserved)

        return res

    def getAllocations(self, row):
        res = 0
        if sum(row[1:5]) == 0:
            res += 1
            row[1:5] = [1] * 4

        if sum(row[3:7]) == 0:
            res += 1
            row[3:7] = [1] * 4

        if sum(row[5:9]) == 0:
            res += 1
            row[5:9] = [1] * 4

        return res


class Solution2:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:

        heapq.heapify(reservedSeats)
        res = 0
        currrent_row = reservedSeats[0][0]
        if currrent_row > 1:
            res += (currrent_row - 1) * 2

        while reservedSeats:
            is_changed = False
            possible_seat1 = True
            possible_seat2 = True
            possible_seat3 = True
            while reservedSeats and reservedSeats[0][0] == currrent_row:
                is_changed = True
                curr_row, seat = heapq.heappop(reservedSeats)

                if seat in [2, 3] or seat in [4, 5]:
                    possible_seat1 = False
                if seat in [4, 5, 6, 7]:
                    possible_seat2 = False
                if seat in [8, 9] or seat in [6, 7]:
                    possible_seat3 = False

            if not is_changed:
                res += 2
            else:
                if possible_seat1:
                    res += 1
                if possible_seat3:
                    res += 1

                if possible_seat2 and not possible_seat1 and not possible_seat3:
                    res += 1

            currrent_row += 1

        res += (n - currrent_row + 1) * 2

        return res

from collections import defaultdict
class Solution3:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:

        reserved_hash = defaultdict(list)
        for row, seat in reservedSeats:
            reserved_hash[row].append(seat)

        res = n * 2

        for row_num, row in reserved_hash.items():

            possible_seat1 = possible_seat2 = possible_seat3 = True
            if 2 in row or 3 in row or 4 in row or 5 in row:
                possible_seat1 = False
            if 4 in row or 5 in row or 6 in row or 7 in row:
                possible_seat2 = False
            if 6 in row or 7 in row or 8 in row or 9 in row:
                possible_seat3 = False

            if not possible_seat1 and not possible_seat2:
                res -= 1
            if not possible_seat2 and not possible_seat3:
                res -= 1
            if possible_seat2 and (not possible_seat1 or not possible_seat3):
                res -= 1

        return res

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:

        reserved_hash = {}
        for row, seat in reservedSeats:
            if row not in reserved_hash:
                reserved_hash[row] = []
            reserved_hash[row].append(seat)

        res = n * 2

        for row_num, row in reserved_hash.items():

            possible_seat1 = possible_seat2 = possible_seat3 = True
            if 2 in row or 3 in row or 4 in row or 5 in row:
                possible_seat1 = False
            if 4 in row or 5 in row or 6 in row or 7 in row:
                possible_seat2 = False
            if 6 in row or 7 in row or 8 in row or 9 in row:
                possible_seat3 = False

            if not possible_seat1 and not possible_seat2:
                res -= 1
            if not possible_seat2 and not possible_seat3:
                res -= 1
            if possible_seat2 and (not possible_seat1 or not possible_seat3):
                res -= 1

        return res


#############
import unittest


class TestCase(unittest.TestCase):

    def test1(self):
        n = 3
        reservedSeats = [[1, 2], [1, 3], [1, 8], [2, 6], [3, 1], [3, 10]]
        out = 4
        res = Solution().maxNumberOfFamilies(n, reservedSeats)
        self.assertEqual(res, out)

    def test2(self):
        n = 2
        reservedSeats = [[2, 1], [1, 8], [2, 6]]
        out = 2
        res = Solution().maxNumberOfFamilies(n, reservedSeats)
        self.assertEqual(res, out)

    def test3(self):
        n = 4
        reservedSeats = [[4, 3], [1, 4], [4, 6], [1, 7]]
        out = 4
        res = Solution().maxNumberOfFamilies(n, reservedSeats)
        self.assertEqual(res, out)

    def test4(self):
        n = 2
        reservedSeats = [[2, 1], [1, 8], [2, 6]]
        out = 2
        res = Solution().maxNumberOfFamilies(n, reservedSeats)
        self.assertEqual(res, out)

    def test5(self):
        from testcases.input_test_cinema import rows
        n = 1000000000
        reservedSeats = rows
        out = 1999994439
        res = Solution().maxNumberOfFamilies(n, reservedSeats)
        self.assertEqual(res, out)



if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
