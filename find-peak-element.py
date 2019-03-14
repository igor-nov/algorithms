"""
162. Find Peak Element

A peak element is an element that is greater than its neighbors.
Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
You may imagine that nums[-1] = nums[n] = -∞.

Example 1:
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.

Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.
		
Note:

Your solution should be in logarithmic complexity.
		
"""


"""
Runtime: 16 ms, faster than 100.00% of Python online submissions for Find Peak Element.
Memory Usage: 10.8 MB, less than 73.01% of Python online submissions for Find Peak Element.
"""

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        peak = 0
        
        for i in xrange(1, len(nums)):
            if nums[i] > nums[peak]:
                peak = i
            else:
                break
                
        return peak
        
		
"""
Runtime: 16 ms, faster than 100.00% of Python online submissions for Find Peak Element.
Memory Usage: 10.8 MB, less than 67.47% of Python online submissions for Find Peak Element.
"""

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if len(nums) == 1:
        #     return 0
        
        lt = 0
        gt = len(nums)-1
        
        while  lt < gt:
            
            med = (lt + gt)/2
        
            if nums[med] > nums[med+1]:
                gt = med
            else:
                lt = med + 1
                
        return lt
		
		
####################################
import unittest


class TestSolution(unittest.TestCase):

              
    def test_1(self):
        out = 0
        nums =[2,1]
        res = Solution().findPeakElement(nums)
        self.assertEqual(res, out)
        
    def test_2(self):
        out = 2
        nums =[2,1,3]
        res = Solution().findPeakElement(nums)
        self.assertEqual(res, out)
        
    def test_3(self):
        out = 0
        nums =[1]
        res = Solution().findPeakElement(nums)
        self.assertEqual(res, out)
        
    def test_4(self):
        out = 5
        nums =[1,2,1,3,5,6,4]
        res = Solution().findPeakElement(nums)
        self.assertEqual(res, out)
        
    def test_5(self):
        out = 2
        nums =[1,2,3,1]
        res = Solution().findPeakElement(nums)
        self.assertEqual(res, out)
        
   
        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

    