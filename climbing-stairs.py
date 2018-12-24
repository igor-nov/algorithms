"""
70. Climbing Stairs

You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Note: Given n will be a positive integer.

Example 1:
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

------
Example 2:
Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


Solutions 
3-4 short lines in every language - https://leetcode.com/problems/climbing-stairs/discuss/25296/3-4-short-lines-in-every-language
Python different solutions (bottom up, top down). - https://leetcode.com/problems/climbing-stairs/discuss/25313/Python-different-solutions-(bottom-up-top-down).
Basically it's a fibonacci. (fix 0 case) - https://leetcode.com/problems/climbing-stairs/discuss/25299/Basically-it's-a-fibonacci.
Using the Fibonacci formular to get the answer directly - https://leetcode.com/problems/climbing-stairs/discuss/25436/Using-the-Fibonacci-formular-to-get-the-answer-directly
"""




#Runtime: 20 ms, faster than 98.02% of Python online submissions for Climbing Stairs.
class Solution(object):
    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if not n:
            return 1
        
        res = [None] * (n+1)        
        
        res[0] = 1
        res[1] = 1
        
        for i in xrange(2, n+1):
            res[i] = res[i-1] + res[i-2]
        
        return res[n]
		
		
##########################
import unittest

class TestSolution(unittest.TestCase):
    
    def test_1(self):
        inp =  2       
        out = 2
        res = Solution().climbStairs(inp)
        self.assertEqual(res, out)
        
    def test_2(self):
        inp =  4
        out = 5
        res = Solution().climbStairs(inp)
        self.assertEqual(res, out)
        
    def test_3(self):
        inp =  0
        out = 1
        res = Solution().climbStairs(inp)
        self.assertEqual(res, out)        
        
    def test_4(self):
        inp =  1
        out = 1
        res = Solution().climbStairs(inp)
        self.assertEqual(res, out)
        
    def test_5(self):
        inp =  324
        out = 37281903592600898879479448409585328515842582885579275203077366912825
        res = Solution().climbStairs(inp)
        self.assertEqual(res, out)
        
    def test_6(self):
        inp =  3
        out = 3
        res = Solution().climbStairs(inp)
        self.assertEqual(res, out)
        
    
        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)