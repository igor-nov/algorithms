"""
1399. Count Largest Group

Solution 1
Runtime: 132 ms, faster than 11.11% of Python3 online submissions for Count Largest Group.
Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Count Largest Group

Solution 2
Runtime: 132 ms, faster than 11.11% of Python3 online submissions for Count Largest Group.
Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Count Largest Group.
"""


class Solution1:
    def countLargestGroup(self, n: int) -> int:

        groups = {}
        for i in range(1, n+1):
            key = self.get_n_sum(i)
            if key in groups:
                groups[key] += 1
            else:
                groups[key] = 1

        max_group = 1
        for key, val in groups.items():
            if val > max_group:
                max_group = val

        res = 0
        for key, val in groups.items():
            if val == max_group:
                res += 1

        return res


    def get_n_sum(self, num):
        return sum([int(i) for i in str(num)])



class Solution:
    def countLargestGroup(self, n: int) -> int:

        groups = {}
        for i in range(1, n+1):
            key = sum([int(i) for i in str(i)])
            groups[key] = groups[key] + 1 if key in groups else 1

        res, max_value = 0, 1

        for key, val in groups.items():
            if max_value == val:
                res += 1
            elif val > max_value:
                max_value = val
                res = 1

        return res


    def get_n_sum(self, num):
        return sum([int(i) for i in str(num)])




#############
import unittest


class TestCase(unittest.TestCase):

    def test1(self):
        inp = 13
        out = 4
        res = Solution().countLargestGroup(inp)
        self.assertEqual(res, out)

    def test2(self):
        inp = 2
        out = 2
        res = Solution().countLargestGroup(inp)
        self.assertEqual(res, out)

    def test3(self):
        inp = 15
        out = 6
        res = Solution().countLargestGroup(inp)
        self.assertEqual(res, out)

    def test4(self):
        inp = 24
        out = 5
        res = Solution().countLargestGroup(inp)
        self.assertEqual(res, out)



if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
