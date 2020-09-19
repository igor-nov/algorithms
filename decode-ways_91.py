"""
91. Decode Ways

Solution 3
Time Limit Exceeded

Solution 2
Runtime: 28 ms, faster than 83.15% of Python3 online submissions for Decode Ways.
Memory Usage: 12.8 MB, less than 100.00% of Python3 online submissions for Decode Ways.

Solution 3
Time Limit Exceeded

Solution 4 top-bottom
Runtime: 36 ms, faster than 27.06% of Python3 online submissions for Decode Ways.
Memory Usage: 15.3 MB, less than 12.00% of Python3 online submissions for Decode Ways.


Solutions

Total Ways To Decode A String - Recursive Dynamic Programming Approach ("Decode Ways" on LeetCode) - https://www.youtube.com/watch?v=YcJTyrG3bZs
FACEBOOK - DECODE WAYS (LeetCode) - https://www.youtube.com/watch?v=cQX3yHS0cLo
Programming Interview Question: Count Number of Encodings of a digit string - https://www.youtube.com/watch?v=aCKyFYF9_Bg

Review an answer - Decode Ways - https://stackoverflow.com/questions/20342462/review-an-answer-decode-ways
Count Possible Decodings of a given Digit Sequence - https://www.geeksforgeeks.org/count-possible-decodings-given-digit-sequence/
Python: Easy to understand explanation, bottom up dynamic programming https://leetcode.com/problems/decode-ways/discuss/253018/Python%3A-Easy-to-understand-explanation-bottom-up-dynamic-programming
Java clean DP solution with explanation https://leetcode.com/problems/decode-ways/discuss/30358/Java-clean-DP-solution-with-explanation
Java 2ms DP solution with detailed explanation and inline comments - https://leetcode.com/problems/decode-ways/discuss/30522/Java-2ms-DP-solution-with-detailed-explanation-and-inline-comments
A concise dp solution - https://leetcode.com/problems/decode-ways/discuss/30384/A-concise-dp-solution
Evolve from recursion to dp - https://leetcode.com/problems/decode-ways/discuss/30451/Evolve-from-recursion-to-dp

1-liner, O(1) space (check comments) - https://leetcode.com/problems/decode-ways/discuss/30379/1-liner-O(1)-space
"""


class Solution:  # Time Limit Exceeded
    def numDecodings(self, s: str) -> int:

        if not s:
            return 0

        res = []
        len_s = len(s)

        def helper(prefix, pos):
            if pos == len_s:
                res.append(prefix)
            else:
                if int(s[pos]) > 0:
                    helper(prefix[:] + [s[pos]], pos + 1)
                if 9 < int(s[pos:pos + 2]) < 27:
                    helper(prefix[:] + [s[pos:pos + 2]], pos + 2)

        helper([], 0)
        return len(res)


class Solution2:
    def numDecodings(self, s: str) -> int:

        if not s:
            return 0

        len_s = len(s)

        dp = [0] * (len_s + 1)
        dp[0] = 1
        for pos in range(1, len_s + 1):
            if int(s[pos - 1]) > 0:
                dp[pos] += dp[pos - 1]
            if pos > 1 and 9 < int(s[pos - 2:pos]) < 27:
                dp[pos] += dp[pos - 2]
        # print(dp)
        return dp[-1]


class Solution3:  # Time Limit Exceeded

    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        res = []
        self.helper(s, '', res)
        return len(res)

    def helper(self, st, pref, res):
        if not st:
            res.append(pref)
        else:
            if 0 < int(st[0]):
                self.helper(st[1:], pref + st[0], res)
            if len(st) > 1 and 9 < int(st[0:2]) < 27:
                self.helper(st[2:], pref + st[0:2], res)


class Solution4:

    def __init__(self):
        self.cache = {}

    def numDecodings(self, s: str) -> int:
        if not s:
            return 0

        return self.helper(s)

    def helper(self, st):
        if st in self.cache:
            return self.cache[st]
        if not st:
            return 1
        elif st == '0':
            return 0
        else:
            res = 0
            if 0 < int(st[0]):
                res += self.helper(st[1:])
            if len(st) > 1 and 9 < int(st[0:2]) < 27:
                res += self.helper(st[2:])
            self.cache[st] = res
        return res


# wont work for all cases
from functools import lru_cache
class Solution:

    @lru_cache(maxsize=None)
    def numDecodings(self, s: str) -> int:

        if not s:
            return 0

        if len(s) == 1:
            return 0 if s == '0' else 1

        res = 0

        if s[0] != '0':
            res += self.numDecodings(s[1:])
        if 9 < int(s[0:2]) < 27:
            res += self.numDecodings(s[2:])

        return res




################################
import unittest


class TestSolution(unittest.TestCase):

    def test_1(self):
        inp = '12'
        out = 2
        res = Solution().numDecodings(inp)
        self.assertEqual(res, out)

    def test_2(self):
        inp = '123'
        out = 3
        res = Solution().numDecodings(inp)
        self.assertEqual(res, out)

    def test_3(self):
        inp = '2267'
        out = 3
        res = Solution().numDecodings(inp)
        self.assertEqual(res, out)

    def test_4(self):
        inp = ''
        out = 0
        res = Solution().numDecodings(inp)
        self.assertEqual(res, out)

    def test_5(self):
        inp = '12321672356'
        out = 18
        res = Solution().numDecodings(inp)
        self.assertEqual(res, out)

    def test_6(self):
        inp = '12342343565623445456765'
        out = 12
        res = Solution().numDecodings(inp)
        self.assertEqual(res, out)

    def test_7(self):
        inp = '0'
        out = 0
        res = Solution().numDecodings(inp)
        self.assertEqual(res, out)

    def test_8(self):
        inp = '00'
        out = 0
        res = Solution().numDecodings(inp)
        self.assertEqual(res, out)

    def test_9(self):
        inp = '01'
        out = 0
        res = Solution().numDecodings(inp)
        self.assertEqual(res, out)

    def test_10(self):
        inp = '001'
        out = 0
        res = Solution().numDecodings(inp)
        self.assertEqual(res, out)

    def test_11(self):
        inp = '100'
        out = 0
        res = Solution().numDecodings(inp)
        self.assertEqual(res, out)

    def test_12(self):
        inp = '1'
        out = 1
        res = Solution().numDecodings(inp)
        self.assertEqual(res, out)

    def test_122(self):
        inp = '2'
        out = 1
        res = Solution().numDecodings(inp)
        self.assertEqual(res, out)

    def test_124(self):
        inp = '4757562545844617494555774581341211511296816786586787755257741178599337186486723247528324612117156948'
        out = 589824
        res = Solution().numDecodings(inp)
        self.assertEqual(res, out)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
