"""
152. Maximum Product Subarray

Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


Solutions:

Maximum Product Subarray - https://www.youtube.com/watch?v=vtJvbRlHqTA

Possibly simplest solution with O(n) time complexity - https://leetcode.com/problems/maximum-product-subarray/discuss/48230/Possibly-simplest-solution-with-O(n)-time-complexity

In Python, can it be more concise? - https://leetcode.com/problems/maximum-product-subarray/discuss/48243/In-Python-can-it-be-more-concise


"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxTotal = minCurrent = maxCurrent = nums[0]
        
        for i in xrange(1, len(nums)):
            
            nextMax = maxCurrent * nums[i]
            nextMin = minCurrent * nums[i]
            
            maxCurrent = max(nextMax, nextMin, nums[i])
            minCurrent = min(nextMax, nextMin, nums[i])
            
            
            #print '{} nextMax, {} nextMin, {} maxCurrent, {} minCurrent'.format(nextMax, nextMin, maxCurrent, minCurrent)
            
            maxTotal = max(maxTotal, maxCurrent)
                
        return maxTotal
		
		
###############################3
import unittest


class TestSolution(unittest.TestCase):
          
    def test_1(self):
        inp = [2,3,-2,4]
        out = 6
        res = Solution().maxProduct(inp)
        self.assertEqual(res, out)
        
    def test_2(self):
        inp = [-2,0,-1]
        out = 0
        res = Solution().maxProduct(inp)
        self.assertEqual(res, out)
        
    def test_3(self):
        inp = [0]
        out = 0
        res = Solution().maxProduct(inp)
        self.assertEqual(res, out)
        
    def test_4(self):
        inp = [-1, 0, 1]
        out = 1
        res = Solution().maxProduct(inp)
        self.assertEqual(res, out)
     
    def test_5(self):
        inp = [-1, -1]
        out = 1
        res = Solution().maxProduct(inp)
        self.assertEqual(res, out)
     
    def test_6(self):
        inp = [0, 2]
        out = 2
        res = Solution().maxProduct(inp)
        self.assertEqual(res, out)
     
    def test_7(self):
        inp = [-2,3,-4]
        out = 24
        res = Solution().maxProduct(inp)
        self.assertEqual(res, out)
        
        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

    
