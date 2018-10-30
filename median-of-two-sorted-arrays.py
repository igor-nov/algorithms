"""
https://www.geeksforgeeks.org/median-two-sorted-arrays-different-sizes-ologminn-m/
https://www.youtube.com/watch?v=LPFhl65R7ww
"""


from decimal import Decimal

class Solution(object):
    
    def findMedianSortedArrays(self, nums1, nums2):
        
        l1 = len(nums1)
        l2 = len(nums2)
        
        if l1 > l2:            
            return self.findMedianSortedArrays(nums2, nums1)            
            
        minX = 0
        maxX = l1
        
        while minX <= maxX:
            
            partX = (minX + maxX)/2
            partY = (l1 + l2 + 1)/2 - partX
            
            print partX, partY
            
            minRightX = nums1[partX] if partX < l1 else Decimal('+Infinity')
            minRightY = nums2[partY] if partY < l2 else Decimal('+Infinity')
            
            maxLeftX = nums1[partX-1] if partX > 0 else Decimal('-Infinity')
            maxLeftY = nums2[partY-1] if partY > 0 else Decimal('-Infinity')
            
            if maxLeftX <= minRightY and maxLeftY <= minRightX:                
                if (l1 + l2) % 2:
                    return max(maxLeftX, maxLeftY)                    
                else:
                    return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY))/2.0                                       
                
            elif maxLeftX > minRightY:
                maxX -= 1
            else:
                minX += 1
            
        
num1 = [1,3, 5, 6]
num2 = [2, 3]
solution = Solution()
res = solution.findMedianSortedArrays(num1, num2)
print res


