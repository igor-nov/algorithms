"""
46. Permutations

Given a collection of distinct integers, return all possible permutations.

Example:
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

Runtime: 36 ms, faster than 99.63% of Python online submissions for Permutations. (permuteHelper1)

Solutions:
https://www.geeksforgeeks.org/write-a-c-program-to-print-all-permutations-of-a-given-string/
https://leetcode.com/problems/permutations/discuss/18296/Simple-Python-solution-(DFS).

O(n!) - time

string permutations - https://www.youtube.com/watch?v=nYFd7VHKyWQ
"""


class Solution(object):
   
    def permuteHelper1(self, nums, res, numPrefix = None):
        
        if len(nums) == 1:            
            numPrefix.append(nums[0])
            res.append(numPrefix)            
        else:            
            for i in xrange(len(nums)):
                
                newPref = []
                remains = nums[0:i]
                remains.extend(nums[i+1:])
                
                if numPrefix:                                    
                    newPref = numPrefix[:]
                    newPref.append(nums[i])                    
                else:
                    newPref = [nums[i]]                
                    
                self.permuteHelper(remains, res, newPref)
                
    def permute1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        if len(nums) <= 1:
            return [nums]
        else:          
            res = []
            self.permuteHelper(nums, res)            
            return res
        
                
    def permuteHelper2(self, nums, res, left, right):
        
        if left == right:
            res.append(nums[:])            
        else:            
            for i in xrange(left, right+1):                
                nums[left], nums[i] = nums[i], nums[left]
                self.permuteHelper2(nums, res, left + 1, right)
                nums[i], nums[left] = nums[left], nums[i]
                
    def permute2(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        if len(nums) <= 1:
            return [nums]
        else:          
            res = []
            self.permuteHelper2(nums, res, 0, len(nums)-1)
            return res
        
                
    def permuteHelper3(self, nums, res, path):        
        if not nums:      
            res.append(path)
        else:            
            for i in xrange(len(nums)):                
                self.permuteHelper3(nums[:i]+nums[i+1:], res, path + [nums[i]])                
          
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        if len(nums) <= 1:
            return [nums]
        else:          
            res = []
            self.permuteHelper3(nums, res, [])
            return res
    
