class Solution(object):
    
    
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        lLen = len(nums)
        
        if lLen < 3:
            return []
        
        #we need to sort array ~ O(nLogn) in order to properly handle duplicates and 2 pointers approach
        nums.sort()
        triples = []
        
        for i in xrange(lLen-2):
            
            #since it's sorted array there's no reason to check sum 
            #if we got to element greater than 0
            #sum will be greater than 0 anycase
            if nums[i] > 0:
                break
                
            #in case if previous value the same as current 
            #sum will consists of the same elements 
            #so we need to skip current in order to avoid duplicates
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            lo = i + 1
            hi = lLen - 1
            
            while lo < hi:
                
                #check in case we move to num with same value as on previous step in order to remove dublicates
                if lo > i+1 and nums[lo] == nums[lo-1]:
                    lo += 1
                    continue              
                
                #check in case we move to num with same value as on previous step in order to remove dublicates
                if hi < lLen - 1 and nums[hi] == nums[hi+1]:
                    hi -= 1
                    continue

                sum3 = nums[i] + nums[lo] + nums[hi]

                if sum3 == 0:
                    triples.append([nums[i], nums[lo], nums[hi]])                    
                    lo += 1
                    hi -= 1
                    
                #since it's sorted array we can drive in what direction we can move
                elif sum3 < 0:                    
                    lo += 1
                else:
                    hi -= 1
                    
        return triples
                        
                
            
        
    
#nums = [-1, 0, 1, 2, -1, -4]
#nums = [0,0,0]
nums = [0,0,0,0]
#nums = [1,-1,-1,0]
#nums = [-2,0,0,2,2]
res = Solution().threeSum(nums)
print '------'
print res

nums = [-1, 0, 1, 2, -1, -4]
res = Solution().threeSum(nums)

print '------'
print res