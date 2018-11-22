"""
Pow(x, n)

Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:
Input: 2.00000, 10
Output: 1024.00000

Examples:
https://leetcode.com/problems/powx-n/discuss/19563/Iterative-Log(N)-solution-with-Clear-Explanation
https://leetcode.com/problems/powx-n/discuss/19566/Iterative-JavaPython-short-solution-O(log-n)
https://leetcode.com/problems/powx-n/discuss/19565/Iterative-C%2B%2B-solution
https://leetcode.com/problems/powx-n/discuss/19544/5-different-choices-when-talk-with-interviewers
https://leetcode.com/problems/powx-n/discuss/19560/Shortest-Python-Guaranteed

https://www.youtube.com/watch?v=4ivUTBDnki0
https://www.youtube.com/watch?v=wAyrtLAeWvI
"""

class Solution(object):
    
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        if n == 0:
            return 1
        
        if n < 0:
            n = -n
            x = 1.0/x   
            
        tmp = self.myPow(x, n/2)
        
        if n%2:
            return x * tmp * tmp
        else:
            return tmp * tmp
        
        
    
    def myPow2(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        
        if n < 0:
            n = -n
            x = 1.0/x   
            
        res = 1
        while n > 0:            
            if n&1:
                res *= x            
            x *= x
            n >>= 1
                

x = 2
n = -2
n = 2
n = 15
res = Solution().myPow(x, n)

print res
        
