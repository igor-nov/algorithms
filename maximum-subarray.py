"""
Maximum Subarray - 
Solution 1 - Runtime: 24 ms, faster than 99.98% of Python online submissions for Maximum Subarray.

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

Examples:

Solution 1
https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/

Solution 2
https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/ - Divide and Conquer
"""

class Solution(object):
    
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #~O(n)
        maxSum = nextSum = nums[0]      
        for i in xrange(1, len(nums)):
        
            if nums[i] <= nextSum + nums[i]:
                nextSum += nums[i]
            else:
                nextSum = nums[i]
            
            if nextSum > maxSum:
                 maxSum = nextSum
        
        return maxSum if maxSum > nextSum else nextSum
		
		
		def maxHelper(self, nums, lo, med, hi):
                
        maxLeft = maxLeftNext =  nums[med]
        for i in xrange(med-1, -1, -1):
            maxLeftNext += nums[i]
            if maxLeftNext > maxLeft:
                maxLeft = maxLeftNext
            
        maxRight = maxRightNext = nums[med+1]        
        for i in xrange(med+2, hi+1):
            maxRightNext += nums[i]
            if maxRightNext > maxRight:
                maxRight = maxRightNext
        
        return maxLeft + maxRight
        
        
    #Divide and Conquer algorithm # time limit
    # ~O(n log n)
    def maxSubArray2(self, nums, lo=None, hi=None):
        
        if lo is None:
            lo = 0
            
        if hi is None:
            hi = len(nums) - 1 
            
        if lo >= hi:
            return nums[lo]
        
        med = (lo + hi)/2
        
        return max(self.maxSubArray(nums, lo, med),
                   self.maxSubArray(nums, med + 1, hi),
                   self.maxHelper(nums, lo, med, hi))
				   
		

