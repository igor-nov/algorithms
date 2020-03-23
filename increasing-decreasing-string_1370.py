"""
1370. Increasing Decreasing String

Solution 1
Runtime: 68 ms, faster than 58.45% of Python3 online submissions for Increasing Decreasing String.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Increasing Decreasing String.

Solution 2
Runtime: 208 ms, faster than 10.10% of Python3 online submissions for Increasing Decreasing String.
Memory Usage: 12.9 MB, less than 100.00% of Python3 online submissions for Increasing Decreasing String.

Solution 3/Solution 4
Runtime: 64 ms, faster than 70.72% of Python3 online submissions for Increasing Decreasing String.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Increasing Decreasing String.

Solutions
 "complement" operator ~ !!! [Python] Easy-to-understand solution explained - https://leetcode.com/problems/increasing-decreasing-string/discuss/531928/Python-Easy-to-understand-solution-explained
[Java/Python 3] Two clean codes w/ explanation and analysis. - https://leetcode.com/problems/increasing-decreasing-string/discuss/531811/JavaPython-3-Two-clean-codes-w-explanation-and-analysis.
Java Simple Beats 100 percent - https://leetcode.com/problems/increasing-decreasing-string/discuss/532281/Java-Simple-Beats-100-percent
@todo - do it using heap
[C++] Min and Max Heaps / Count Array
https://leetcode.com/problems/increasing-decreasing-string/discuss/531844/C%2B%2B-Min-and-Max-Heaps-Count-Array
Python Heap - https://leetcode.com/problems/increasing-decreasing-string/discuss/531863/Python-Heap
"""

class Solution1:
    def sortString(self, s: str) -> str:
        s_sorted = sorted(s)
        if s == s_sorted:
            return s

        res, counts  = [], {}

        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1

        is_asc = True
        unique_items = sorted(list(set(s)))
        while counts:
            if is_asc:
                for i in range(len(unique_items)):
                    item = unique_items[i]
                    if item in counts:
                        res.append(item)
                        counts[item] -= 1
                        if not counts[item]:
                            del counts[item]
            else:
                for i in range(len(unique_items)-1, -1, -1):
                    item = unique_items[i]
                    if item in counts:
                        res.append(item)
                        counts[item] -= 1
                        if not counts[item]:
                            del counts[item]

            is_asc = not is_asc

        return ''.join(res)


class Solution2:
    def sortString(self, s: str) -> str:
        s_sorted = sorted(s)
        if s == s_sorted:
            return s

        res, counts = [], {}

        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1

        is_asc = True
        unique_items = sorted(list(set(s)))
        remains = len(s)
        while remains:
            if is_asc:
                for i in range(len(unique_items)):
                    item = unique_items[i]
                    if counts[item]:
                        res.append(item)
                        counts[item] -= 1
            else:
                for i in range(len(unique_items) - 1, -1, -1):
                    item = unique_items[i]
                    if counts[item]:
                        res.append(item)
                        counts[item] -= 1

            is_asc = not is_asc
            remains -= 1

        return ''.join(res)

class Solution3:
    def sortString(self, s: str) -> str:
        s_sorted = sorted(s)
        if s == s_sorted:
            return s

        ord_to_ch = [0]*26
        for ch in s:
            ord_to_ch[ord(ch) - ord('a')] += 1

        res = []
        remains = len(s)
        while remains:
            for key, count in enumerate(ord_to_ch):
                if count == 0:
                    continue
                res.append(chr( ord('a') + key))
                ord_to_ch[key] -= 1
                remains -= 1

            for key in range(26-1, -1, -1):
                if ord_to_ch[key] == 0:
                    continue
                res.append(chr( ord('a') + key))
                ord_to_ch[key] -= 1
                remains -= 1
        return ''.join(res)

class Solution:
    def sortString(self, s: str) -> str:
        s_sorted = sorted(s)
        if s == s_sorted:
            return s

        ord_to_ch = [0]*26
        for ch in s:
            ord_to_ch[ord(ch) - ord('a')] += 1

        res = []
        remains = len(s)
        while remains:
            for key in range(26):
                if ord_to_ch[key] == 0:
                    continue
                res.append(chr( ord('a') + key))
                ord_to_ch[key] -= 1
                remains -= 1

            for key in range(26-1, -1, -1):
                if ord_to_ch[key] == 0:
                    continue
                res.append(chr( ord('a') + key))
                ord_to_ch[key] -= 1
                remains -= 1
        return ''.join(res)

#####################
import unittest


class TestSolution(unittest.TestCase):

    def test_1(self):
        inp = 'aaaabbbbcccc'
        out = 'abccbaabccba'
        res = Solution().sortString(inp)
        self.assertEqual(res, out)

    def test_2(self):
        inp = 'rat'
        out = 'art'
        res = Solution().sortString(inp)
        self.assertEqual(res, out)

    def test_3(self):
        inp = 'leetcode'
        out = 'cdelotee'
        res = Solution().sortString(inp)
        self.assertEqual(res, out)

    def test_4(self):
        inp = 'ggggggg'
        out = 'ggggggg'
        res = Solution().sortString(inp)
        self.assertEqual(res, out)

    def test_5(self):
        inp = 'spo'
        out = 'ops'
        res = Solution().sortString(inp)
        self.assertEqual(res, out)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
