"""
172. Factorial Trailing Zeroes
Given an integer n, return the number of trailing zeroes in n!.

Example 1:
Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.

Example 2:
Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Note: Your solution should be in logarithmic time complexity.

Solutions:
4-lines 4ms C++ Solution with Explanations - https://leetcode.com/problems/factorial-trailing-zeroes/discuss/52470/4-lines-4ms-C%2B%2B-Solution-with-Explanations
My one-line solutions in 3 languages - https://leetcode.com/problems/factorial-trailing-zeroes/discuss/52371/My-one-line-solutions-in-3-languages
My explanation of the Log(n) solution - https://leetcode.com/problems/factorial-trailing-zeroes/discuss/52367/My-explanation-of-the-Log(n)-solution
My python solution in O(1) space O(logN) time - https://leetcode.com/problems/factorial-trailing-zeroes/discuss/52399/My-python-solution-in-O(1)-space-O(logN)-time

@todo - refresh explanation
"""


"""
Runtime: 24 ms, faster than 69.56% of Python online submissions for Factorial Trailing Zeroes.
Memory Usage: 11.7 MB, less than 5.21% of Python online submissions for Factorial Trailing Zeroes.
"""

class Solution(object):
    
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """      
        nums = 0
        while n:
            n = n/5
            nums += n
        return nums
		
		
		
"""
Runtime: 24 ms, faster than 69.56% of Python online submissions for Factorial Trailing Zeroes.
Memory Usage: 11.7 MB, less than 5.21% of Python online submissions for Factorial Trailing Zeroes.
"""

class Solution(object):
    
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """      
        res = n / 5
        return 0 if not res else res + self.trailingZeroes(res)