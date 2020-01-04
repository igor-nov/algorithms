"""
647. Palindromic Substrings


Solution 1
Runtime: 244 ms, faster than 45.11% of Python3 online submissions for Palindromic Substrings.
Memory Usage: 20.5 MB, less than 50.00% of Python3 online submissions for Palindromic Substrings.

@todo - Approach #1: Expand Around Center
@todo - Approach #2: Manacher's Algorithm

"""


class Solution:
    def countSubstrings(self, s: str) -> int:

        if not s:
            return 0

        dp = [[0] * len(s) for _ in range(len(s))]

        p_nums = 0

        # diagonal
        for i in range(len(s)):
            dp[i][i] = 1
            p_nums += 1

        # len2
        for i in range(len(s) - 1):
            if s[i + 1] == s[i]:
                dp[i][i + 1] = 1
                p_nums += 1

        # len 2...len(s)
        for substr_len in range(2, len(s)):
            for start in range(0, len(s) - substr_len):
                end = substr_len + start
                if s[start] == s[end] and dp[start + 1][end - 1]:
                    dp[start][end] = 1
                    p_nums += 1

        return p_nums


################
import unittest


class TestCase(unittest.TestCase):

    # @unittest.skip
    def test1(self):
        inp = 'abc'
        out = 3
        res = Solution().countSubstrings(inp)
        self.assertEqual(res, out)

    def test2(self):
        inp = 'aba'
        out = 4
        res = Solution().countSubstrings(inp)
        self.assertEqual(res, out)

    def test3(self):
        inp = 'aba'
        out = 4
        res = Solution().countSubstrings(inp)
        self.assertEqual(res, out)

    def test4(self):
        inp = 'aaa'
        out = 6
        res = Solution().countSubstrings(inp)
        self.assertEqual(res, out)

    def test5(self):
        inp = 'aa'
        out = 3
        res = Solution().countSubstrings(inp)
        self.assertEqual(res, out)

    def test6(self):
        inp = 'abca'
        out = 4
        res = Solution().countSubstrings(inp)
        self.assertEqual(res, out)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
