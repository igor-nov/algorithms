"""
136. Single Number

Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
Input: [2,2,1]
Output: 1

Example 2:
Input: [4,1,2,1,2]
Output: 4

Solution:
https://leetcode.com/problems/single-number/solution/
"""
class Solution(object):
    
	"""
	Runtime: 28 ms, faster than 70.53% of Python online submissions for Single Number.
	Memory Usage: 12.9 MB, less than 100.00% of Python online submissions for Single Number.
	"""
    def singleNumber1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        dictNum = {}
        
        for num in nums:
            if num in dictNum:
                dictNum[num] += 1
            else:
                dictNum[num] = 1
                
        #print (dictNum)
        for num  in dictNum:
            #print(num)
            if dictNum[num] == 1:
                return num
            
    """
	Runtime: 32 ms, faster than 50.86% of Python online submissions for Single Number.
	Memory Usage: 12.6 MB, less than 100.00% of Python online submissions for Single Number.
	"""	
	def singleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #2 * (a + b + c) - (a + a + b + b + c) = c        
        def doSum(x, y):
            return x + y
        
        qnique_nums = set(nums)
        
        acc = 0
        res = reduce(lambda x,y : x+y, nums)
        return  2 * reduce(doSum, qnique_nums) - reduce(doSum, nums)
		
	"""
	Runtime: 24 ms, faster than 99.93% of Python online submissions for Single Number.
	Memory Usage: 12.6 MB, less than 100.00% of Python online submissions for Single Number.
	"""
	def singleNumber3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #2 * (a + b + c) - (a + a + b + b + c) = c        
        return 2 * sum(set(nums)) - sum(nums)
        
    """
	Runtime: 28 ms, faster than 70.53% of Python online submissions for Single Number.
	Memory Usage: 11.9 MB, less than 100.00% of Python online submissions for Single Number
	"""
	def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        
        for num in nums:
            a = a ^ num
            
        return a

	
########################################
import unittest


class TestSolution(unittest.TestCase):
            
    def test_1(self):        
        inp = [2,2,1]
        out = 1
        res = Solution().singleNumber(inp)
        self.assertEqual(res, out)
            
    def test_2(self):        
        inp = [4,1,2,1,2]
        out = 4
        res = Solution().singleNumber(inp)
        self.assertEqual(res, out)
        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)