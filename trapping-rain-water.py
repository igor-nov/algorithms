"""
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

Solutions:

https://www.youtube.com/watch?v=KV-Eq3wYjxI
https://leetcode.com/problems/trapping-rain-water/discuss/151093/Python-O(n)-stack-solution-without-recursion
https://www.youtube.com/watch?v=qn-wuF24X1w
https://leetcode.com/problems/trapping-rain-water/discuss/178028/16ms-Java-Stack-with-Explanation
"""

class Solution(object):
    
    # O(n^2)
    def trap2(self, h):
        """
        :type height: List[int]
        :rtype: int
        """
        
        res = 0
        
        for i in xrange(1, len(h)):
            
            max_l = max_r = 0
            
            #left
            for j in xrange(i-1, 0-1, -1):
                max_l = max(max_l, h[j])
                
            #right
            for j in xrange(i+1, len(h)):
                max_r = max(max_r, h[j])
            
            curTrap = max(0, min(max_l, max_r) - h[i])            
            
            res += curTrap
            
        return res
    
    # O(n^2)
    def trap3(self, h):
        """
        :type height: List[int]
        :rtype: int
        """
        
        if not h:
            return 0
            
        #fill maxRight
        maxRight = 0        
        maxRights = [h[len(h)-1]] * (len(h))
        for i in xrange(len(h)-2, -1, -1):
            maxRights[i] = max(maxRights[i+1], h[i])
            
        
        maxLeft = 0        
        maxLefts = [h[0]] * (len(h))        
        res = 0
        
        for i in xrange(1, len(h)-1):
            curVal = max(0,min(maxLefts[i-1], maxRights[i+1]) - h[i])            
        
            #fill maxLefts for next iterations
            maxLefts[i] = max(maxLefts[i-1], h[i])
            res += curVal
            
        return res
    
    
    #stacks
    #stacks ???
    def trap(self, h):
        """
        :type height: List[int]
        :rtype: int
        """
        
        traps = []
        res = 0
        
        for i in xrange(0, len(h)):        
            while traps and h[i] > h[traps[-1]]:                
                top = traps.pop()                
                if not len(traps):
                    break                
                
                distance = i - traps[-1] - 1
                trap = min(h[i], h[traps[-1]]) - h[top]
                res += distance * trap
                #print 'i %i top %s trap %s distance %s traps %s' % (i, top, trap, distance, traps)
                 
            traps.append(i)            
                     
        return res
    
    
	#2 pointers solution
    def trap(self, h):
        """
        :type height: List[int]
        :rtype: int
        """
        
        maxL = maxR = 0
        left = 0
        right = len(h)-1        
        res = 0
        
        while left < right:
            
            if h[left] < h[right]:
                if h[left] >= maxL:
                    maxL = h[left]
                else:
                    res += maxL - h[left]
                    #print 'add %s left %s' % ((maxL - h[left]), left)
                left += 1                
            else:
                if h[right] >= maxR:
                    maxR = h[right]
                else:
                    res += maxR - h[right]
                    #print 'add %s right' % (maxR - h[right])
                right -= 1
                                
        return res
                
        
    
inp = [0,1,0,2,1,0,1,3,2,1,2,1] # 6
# inp = [1] # 0
# inp = [] # 0
# inp = [2,1,0,2] # 3
# inp = [2,0,2] # 2
#print inp
res = Solution().trap(inp)
print res