"""
https://leetcode.com/problems/two-sum/description/

Description

Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        remainings_by_value_key = {}

        for i in xrange(len(nums)): 

            if i > 0 and nums[i] in remainings_by_value_key:
                return [remainings_by_value_key[nums[i]],i]
                        
            remaining = target - nums[i]
            remainings_by_value_key[remaining] = i
            
        return []
           

class Solution2(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        #38 ms
        # dict = {}
        # for key, value in enumerate(nums):
        #     res = target - value
        #     if res in dict:
        #         return [dict[res], key]
        #     dict[value] = key
        
        nums_value_key_dict = {}
        for ix in xrange(len(nums)):  
             res = target - nums[ix]
             if res in nums_value_key_dict:
                 return [nums_value_key_dict[res],ix]
             nums_value_key_dict[nums[ix]] = ix

			 
			 
nums = [2, 7, 11, 15]
target = 22

resHelper = Solution2()
res = resHelper.twoSum(nums, target)

print res
            
            


