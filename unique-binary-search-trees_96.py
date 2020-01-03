"""
96. Unique Binary Search Trees

Solution 1
Runtime: 28 ms, faster than 57.23% of Python3 online submissions for Unique Binary Search Trees.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Unique Binary Search Trees.

Solution 2
Runtime: 28 ms, faster than 57.23% of Python3 online submissions for Unique Binary Search Trees.
Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Unique Binary Search Trees.



Count Number of Binary Search Tree Possible given n keys Dynamic Programming - https://www.youtube.com/watch?v=YDf982Lb84o
Count Total Unique Binary Search Trees - The nth Catalan Number (Dynamic Programming) - https://www.youtube.com/watch?v=GgP75HAvrlY&feature=youtu.be&t=168


DP Solution in 6 lines with explanation. F(i, n) = G(i-1) * G(n-i) - https://leetcode.com/problems/unique-binary-search-trees/discuss/31666/DP-Solution-in-6-lines-with-explanation.-F(i-n)-G(i-1)-*-G(n-i)
Fantastic Clean Java DP Solution with Detail Explaination - https://leetcode.com/problems/unique-binary-search-trees/discuss/31707/Fantastic-Clean-Java-DP-Solution-with-Detail-Explaination
Python solutions (DP + Catalan number) - https://leetcode.com/problems/unique-binary-search-trees/discuss/31826/Python-solutions-(DP-%2B-Catalan-number)
"""


"""
t[1] -> 1 => 1
t[2] -> 1, 2 => 2
t[3] -> 1,2,3 => t[2] + t[1]*t[1] + t[2] => 2 + 1 + 2 => 5
t[4] -> 1,2,3,4 => t[3] + t[1]*t[2] + t[2]*t[1] + t[3] => 5 + 2 + 2 + 4 => 14 
t[5] -> 1,2,3,4,5 => t[4] + t[1]*t[3] + t[2]*t[2] + t[3]*t[1] + t[4] => 14 + 5 + 4 + 5 + 14 => 42 
"""
class Solution1:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            for j in range(0, i):
                dp[i] += dp[j] * dp[i-j-1]

        return dp[n]

"""
G(3) = f(1,3) + f(2,3) + f(3,3)
     G(0)*G(2) + G(1)*G(1) + G(2)*G(0)
"""

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n+1): # 2,3
            for j in range(1, i+1): # 1,2
                dp[i] += dp[j-1] * dp[i-j] # dp[1]*dp[1] +

        #print(dp)
        return dp[n]

#############
import unittest


class TestCase(unittest.TestCase):

    def test1(self):
        inp = 3
        out = 5
        res = Solution().numTrees(inp)
        self.assertEqual(res, out)

    def test2(self):
        inp = 4
        out = 14
        res = Solution().numTrees(inp)
        self.assertEqual(res, out)

    def test3(self):
        inp = 2
        out = 2
        res = Solution().numTrees(inp)
        self.assertEqual(res, out)

    def test4(self):
        inp = 5
        out = 42
        res = Solution().numTrees(inp)
        self.assertEqual(res, out)

    def test4(self):
        inp = 6
        out = 132
        res = Solution().numTrees(inp)
        self.assertEqual(res, out)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
