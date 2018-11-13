"""
Given two integers dividend and divisor, divide two integers without 
using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.
The integer division should truncate toward zero.

https://leetcode.com/problems/divide-two-integers/discuss/13407/Detailed-Explained-8ms-C%2B%2B-solution
https://leetcode.com/problems/divide-two-integers/discuss/13467/Very-detailed-step-by-step-explanation-(Java-solution)
https://leetcode.com/problems/divide-two-integers/discuss/13403/Clear-python-code
"""


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        multBy = 0
        sign = False
        
        minNum = -2147483648 #-2**31
        maxNum = 2147483647 #2**31 - 1
        
        if dividend == maxNum and divisor == -1:
            return maxNum
                
        if dividend < 0 and divisor > 0:
            dividend = abs(dividend)
            sign = True
            
        elif divisor < 0 and dividend > 0:
            divisor = abs(divisor)
            sign = True
        
        while dividend >= divisor:
            
            stepDivisor = divisor
            divisorMultiplication = 1
            
            while dividend >= stepDivisor:
                stepDivisor <<= 1
                divisorMultiplication <<= 1
            
            multBy += divisorMultiplication >> 1
            dividend -= stepDivisor >> 1
            
        if sign:
            multBy = -multBy
        
        return multBy
            
        
            
        
"""
class Solution(object):
    
    
    def divide(self, dividend, divisor):
                
        #specialcases
        min_r = -2**31
        max_r = 2**31 - 1
        
        if dividend == min_r and divisor == -1:
            return max_r
        
        #print min_r, max_r
        
        
        sign = False
        if dividend < 0 and divisor > 0:
            sign = True
        elif dividend > 0 and divisor < 0:
            sign = True
            
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        res = 0
        #print 'divisor %s vs %s' % (divisor, dividend)
        while divisor <= dividend:
            #print 'divisor %s vs %s -> %s' % (divisor, dividend, step)
        
            step = 1
            tmp = divisor
            #print 'divisor %s vs %s -> %s' % (divisor, dividend, step)
            while tmp <= dividend:
                tmp = tmp << 1
                step = step << 1
                
                #print divisor - dividend, step
                #print 'divisor %s vs %s -> %s' % (divisor, dividend, step)
                #print 'divisor %s vs %s -> %s' % (tmp, dividend, step)
#                 step += 1
#                 if step > 100:
#                     break

            step = step >> 1
            tmp = tmp >> 1
            dividend -= tmp
            res += step
            
        #res = 2 << step - 1
        #print 'res %s' % res
        if sign:
            res = -res
        
        return res
"""
        
        
dividend = 27
divisor = -3

#dividend = 9
#divisor = -3

res = Solution().divide(dividend, divisor)
print res