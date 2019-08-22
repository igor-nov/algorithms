"""
202. Happy Number
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Runtime: 40 ms, faster than 74.30% of Python3 online submissions for Happy Number.
Memory Usage: 13.7 MB, less than 5.26% of Python3 online submissions for Happy Number.
Next challenges:
"""

class Solution:

    def isHappy(self, n: int) -> bool:
        faced_nums = set()
        while True:
            next_num = self.getSquareRes(n)
            
            if next_num in faced_nums:
                return False
            
            if next_num == 1:
                return True
            
            faced_nums.add(next_num)
            n = next_num
        
        
    # 13 - > 13 % 10 = 3 >> 1 % 10 = 1 
    def getSquareRes(self, n: int) -> int:
        res = 0
        while n:
            digit = n % 10
            res += digit ** 2
            n = n // 10
        return res
			
		
		
		
		
		
#18 -> 1**2 + 8**2 = 1 + 64 = 65 | 6**2 + 5**2 = 36 + 25 = 61 | 6**2 + 1**2 = 36 + 1 = 35|
3**2 + 5**2 = 9 + 25 = 36 | 3**2 + 6**2 -> 9 + 36 = 45 | 

#31 / 13 
#68 / 86
 