"""
69. Sqrt(x)

Implement int sqrt(int x).
Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

-----
Example 1:
Input: 4
Output: 2

-----

Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.


https://leetcode.com/problems/sqrtx/discuss/25066/Solve-this-problem-with-Binary-Search
https://en.wikipedia.org/wiki/Integer_square_root#Using_only_integer_division
https://leetcode.com/problems/sqrtx/discuss/25057/3-4-short-lines-Integer-Newton-Every-Language
https://leetcode.com/problems/sqrtx/discuss/25048/Share-my-O(log-n)-Solution-using-bit-manipulation
https://leetcode.com/problems/sqrtx/discuss/25061/Python-binary-search-solution-(O(lgn)).
https://leetcode.com/problems/sqrtx/discuss/25258/Using-binary-search-accepted-but-one-question
https://leetcode.com/problems/sqrtx/discuss/25066/Solve-this-problem-with-Binary-Search
			 
"""

class Solution(object):
    
    def mySqrt1(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if x == 0:
            return 0
        elif x == 1:
            return 1
        else:

            res = x
            while True:
                tmpX = (res >> 1) * (res >> 1)
                if tmpX == x:
                    return res >> 1
                elif tmpX < x:
                    break
                else:
                    res = res >> 1

            resHi = res            
            resLo = res >> 1
            
            while True:                  
                midPoint = (resHi - resLo) >> 1
                #print res, resLo, midPoint, resHi, midPoint+resLo
                
                tmpX = (resLo + midPoint) * (resLo + midPoint)
                
                if tmpX == x:
                    return resLo + midPoint
                
                elif tmpX > x:
                    resHi -= midPoint
                else:
                    resLo += midPoint
                
                #print res, resLo, midPoint, resHi, midPoint+resLo
                
                if not midPoint:                    
                    #return max(resLo, res)
                    return resLo
                
                    
            return res
        
	#Newton's method
    def mySqrt2(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        r = x
        while r*r > x:
            r = (r + x/r) / 2
        return r
		
	#bianry search
	def mySqrt3(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if 0 == x: return 0
        
        lo, hi = 1, x
        
        while lo <= hi:            
            mid = lo + (hi-lo)/2            
            if mid <= x/mid:
                res = mid
                lo = mid + 1                
            else:
                hi = mid - 1
                
        return res
		
	
####-------------------

import unittest

class TestSolution(unittest.TestCase):
    
    def test_1(self):
        x =  1        
        out = 1
        res = Solution().mySqrt(x)
        self.assertEqual(res, out)
        
    def test_2(self):
        x =  4
        out = 2
        res = Solution().mySqrt(x)
        self.assertEqual(res, out)
        
    def test_3(self):
        x =  8        
        out = 2
        res = Solution().mySqrt(x)
        self.assertEqual(res, out)        
        
    def test_4(self):
        x =  9
        out = 3
        res = Solution().mySqrt(x)
        self.assertEqual(res, out)
        
    def test_5(self):
        x =  1        
        out = 1
        res = Solution().mySqrt(x)
        self.assertEqual(res, out)
        
    def test_6(self):
        x =  0
        out = 0
        res = Solution().mySqrt(x)
        self.assertEqual(res, out)
        
    def test_7(self):
        x =  1112768330       
        out = 33358
        res = Solution().mySqrt(x)
        self.assertEqual(res, out)
        
    def test_8(self):
        x =  6
        out = 2
        res = Solution().mySqrt(x)
        self.assertEqual(res, out)
        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)