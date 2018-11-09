"""
Remove Duplicates from Sorted Array

Given a sorted array nums, remove the duplicates in-place such that 
each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by 
modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
"""

class Solution(object):
    
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return
        
        p = 0
        for i in xrange(1, len(nums)):
            if nums[i-1] != nums[i]:
                p += 1
                if i != p:
                    nums[p] = nums[i] 
        return p + 1
        
        
inp = [0,0,1,1,1,2,2,3,3,4]
res = Solution().removeDuplicates(inp)
print res