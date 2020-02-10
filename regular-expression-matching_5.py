"""
10. Regular Expression Matching


Solution 1
Runtime: 52 ms, faster than 61.97% of Python3 online submissions for Regular Expression Matching.
Memory Usage: 12.6 MB, less than 100.00% of Python3 online submissions for Regular Expression Matching.

@todo - NFA
NFA simulation in Python - https://leetcode.com/problems/regular-expression-matching/discuss/414658/NFA-simulation-in-Python
Python NFA with detailed explanation, beats 96.74% - https://leetcode.com/problems/regular-expression-matching/discuss/333699/Python-NFA-with-detailed-explanation-beats-96.74
NFA implementation in Python - https://leetcode.com/problems/regular-expression-matching/discuss/178940/NFA-implementation-in-Python
Clean Python NFA solution - https://leetcode.com/problems/regular-expression-matching/discuss/5771/Clean-Python-NFA-solution
Java solution using NFA - https://leetcode.com/problems/regular-expression-matching/discuss/126062/Java-solution-using-NFA
My accepted solution based on Nondeterministic Finite Automata (NFA) - https://leetcode.com/problems/regular-expression-matching/discuss/5968/My-accepted-solution-based-on-Nondeterministic-Finite-Automata-(NFA)
Share a Java solution, just like a NFA regex engine - https://leetcode.com/problems/regular-expression-matching/discuss/5998/Share-a-Java-solution-just-like-a-NFA-regex-engine


Regular Expression Dynamic Programming  - https://www.youtube.com/watch?v=l3hda49XcDE
(https://github.com/mission-peace/interview/blob/master/src/com/interview/dynamic/RegexMatching.java)

https://leetcode.com/problems/regular-expression-matching/discuss/5651/Easy-DP-Java-Solution-with-detailed-Explanation
https://leetcode.com/problems/regular-expression-matching/discuss/5723/My-DP-approach-in-Python-with-comments-and-unittest
https://leetcode.com/problems/regular-expression-matching/discuss/5678/Fast-Python-solution-with-backtracking-and-caching-%2B-DP-solution
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        rows, cols = len(s), len(p)
        dp = [[False] * (cols + 1) for _ in range(rows + 1)]

        dp[0][0] = True
        for col in range(1, cols + 1):
            if p[col - 1] == '*':
                dp[0][col] = dp[0][col - 2]

        for row in range(1, rows + 1):
            for col in range(1, cols + 1):
                if s[row - 1] == p[col - 1] or p[col - 1] == '.':
                    dp[row][col] = dp[row - 1][col - 1]
                elif p[col - 1] == '*':
                    if dp[row][col - 2]:
                        dp[row][col] = True
                    elif p[col - 2] == '.' or p[col - 2] == s[row - 1]:
                        dp[row][col] = dp[row - 1][col]

        return dp[rows][cols]


#############
import unittest


class TestCase(unittest.TestCase):

    def test1(self):
        inp = 'aa'
        pat = 'a'
        out = False
        res = Solution().isMatch(inp, pat)
        self.assertEqual(res, out)

    def test2(self):
        inp = 'aa'
        pat = 'a*'
        out = True
        res = Solution().isMatch(inp, pat)
        self.assertEqual(res, out)

    def test3(self):
        inp = 'ab'
        pat = '.*'
        out = True
        res = Solution().isMatch(inp, pat)
        self.assertEqual(res, out)

    def test4(self):
        inp = 'aab'
        pat = 'c*a*b'
        out = True
        res = Solution().isMatch(inp, pat)
        self.assertEqual(res, out)

    def test5(self):
        inp = 'mississippi'
        pat = 'mis*is*p*'
        out = False
        res = Solution().isMatch(inp, pat)
        self.assertEqual(res, out)

    def test6(self):
        inp = ''
        pat = '.*'
        out = True
        res = Solution().isMatch(inp, pat)
        self.assertEqual(res, out)

    def test7(self):
        inp = ''
        pat = ''
        out = True
        res = Solution().isMatch(inp, pat)
        self.assertEqual(res, out)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
