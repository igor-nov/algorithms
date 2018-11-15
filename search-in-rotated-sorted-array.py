"""
Search in Rotated Sorted Array

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
Your algorithm's runtime complexity must be in the order of O(log n).

examples:
https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14437/Python-binary-search-solution-O(logn)-48ms

https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14436/Revised-Binary-Search
https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14419/Pretty-short-C%2B%2BJavaRubyPython
??7
https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/154836/The-INF-and-INF-method-but-with-a-better-explanation-for-dummies-like-me

"""

class Solution(object):
    
    def getMedian(self, lo, hi):
        return (lo + hi) / 2
    
    def binarySearch(self, nums, target, lo, hi):        
        while lo <= hi:
            med = self.getMedian(lo, hi)
#             print 'lo %s , med %s hi %s' % (lo, med, hi)
#             print '%s - %s - %s' % (nums[lo], nums[med], nums[hi])
            if nums[med] == target:
                return med
            elif nums[med] < target:
                lo = med + 1
            else:
                hi = med - 1
				
        return -1
        
    
    
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        lo = 0
        hi = len(nums) - 1
        
        if hi < 0:
            return -1
        
        #if its sorted from the begining
        if nums[lo] < nums[hi]:
            return self.binarySearch(nums, target, lo, hi)
        else:
            while lo < hi:                
                med = self.getMedian(lo, hi)
                
#                 print '%s %s %s' % (lo, med, hi)
#                 print '%s-%s-%s' % (nums[lo], nums[med], nums[hi])
                
                if nums[med] == target:
                    return med
                
                #if left part is sorted
                if nums[lo] <= nums[med]:
                    
                    #if target in that part
                    if nums[lo] <= target < nums[med]:
                        return self.binarySearch(nums, target, lo, med - 1)
                    
                    #otherwise move to righ part
                    else:
                        lo = med + 1            
                        
                #if right part is sorted
                else: #nums[med] <= nums[hi]
                    
                    #if target in that part
                    if nums[med] < target <= nums[hi]:                        
                        return self.binarySearch(nums, target, med + 1, hi)
                    
                    #otherwise move to left part
                    else:
                        hi = med - 1
                        
                        
        #if we exeded and from main loop
        if nums[lo] == target:
            return lo
        else:
            return -1
                    
                
        
        
        
nums = [0,1,2, 4,5,6,7]
target = 0

nums = [4,5,6,7,0,1,2]
target = 0

nums =[9,0,2,7,8]
target = 3

nums =[1,3]
target = 0

nums =[1,3]
target = 3

nums =[1,3]
target = 4

nums = [3,1]
target = 0

nums = [4,5,6,7,8,1,2,3]
target = 8

nums = []
target = 5

nums = [5,1,3]
target = 3

res = Solution().search(nums, target)
print 'res = %s' % res