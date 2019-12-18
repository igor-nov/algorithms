"""
179. Largest Number

Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:
Input: [10,2]
Output: "210"

Example 2:
Input: [3,30,34,5,9]
Output: "9534330"

Note: The result may be very large, so you need to return a string instead of an integer.

Solutions
My 3-lines code in Java and Python - https://leetcode.com/problems/largest-number/discuss/53162/My-3-lines-code-in-Java-and-Python
Python different solutions (bubble, insertion, selection, merge, quick sorts). - https://leetcode.com/problems/largest-number/discuss/53298/Python-different-solutions-(bubble-insertion-selection-merge-quick-sorts).

"""

class Solution(object):
    
    def cmp_by_sum(selfm, x, y):
        return int(y + x) -  int(x + y)
    
    def sortByfirstChs(self, nums, st=0):
        nums = [str(num) for num in nums]
        nums = sorted(nums, cmp = self.cmp_by_sum)
        return nums
    
    
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        
        if not nums:
            return '0'
        nums = self.sortByfirstChs(nums)
        
        if nums[0] == '0':
            return '0'
        
        return ''.join(str(item) for item in nums)
        
#################### Solution 2
def cmp_by_sum(x, y):
    return int(y + x) -  int(x + y)

class LagestNumKey(object):
    
    def __init__(self, obj, *args):
        self.obj = obj
            
    def __lt__(self, other):
        return cmp_by_sum(self.obj, other.obj) < 0
    
class Solution(object):
    
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        
        if not nums:
            return '0'
    
        nums = sorted([str(num) for num in nums], key = LagestNumKey)
        
        if nums[0] == '0':
            return '0'
        
        return ''.join(nums)
        
        
###########################
import unittest

class TestSolution(unittest.TestCase):

    def test_1(self):
        inp = [3,30,34,5,9] #"9534330"
        out = '9534330'
        res = Solution().largestNumber(inp)
        self.assertEqual(res, out)
              
    def test_2(self):
        inp = [0] #"9534330"
        out = '0'
        res = Solution().largestNumber(inp)
        self.assertEqual(res, out)
   
    def test_3(self):
        inp = [0,0] #"9534330"
        out = '0'
        res = Solution().largestNumber(inp)
        self.assertEqual(res, out)
        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

 