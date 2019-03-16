"""
169. Majority Element

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:
Input: [3,2,3]
Output: 3

Example 2:
Input: [2,2,1,1,1,2,2]
Output: 2

Solutions:
Boyer-Moore Voting Algorithm - https://leetcode.com/problems/majority-element/solution/
"""

"""
Runtime: 48 ms, faster than 33.26% of Python online submissions for Majority Element.
Memory Usage: 12.1 MB, less than 14.52% of Python online submissions for Majority Element.
"""
# Solution 1 - space O(n), time O(n)
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return
        
        appearances = {nums[0]:1}
        max_el = nums[0]
        max_appearances = 1
        
        for i in xrange(1, len(nums)):
            
            if nums[i] in appearances:
                appearances[nums[i]] += 1
            else:
                appearances[nums[i]] = 1
                
            if nums[i] != max_el and appearances[nums[i]] > appearances[max_el]:
                max_el = nums[i]
                max_appearances = appearances[nums[i]]
            
            #print(max_el, i, appearances[nums[i]], len(nums), appearances[nums[i]])
            if appearances[max_el] > len(nums)/2:
                print '!!!!!!'
                break
                
        return max_el
        

		
#Solution 2  - space O(1), time O(n)   
"""
Runtime: 32 ms, faster than 78.35% of Python online submissions for Majority Element.
Memory Usage: 12 MB, less than 17.49% of Python online submissions for Majority Element.
"""

class Solution(object):
    
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        majorityElementIdx = 0
        count = 1

        for i in xrange(1, len(nums)):

            if nums[i] == nums[majorityElementIdx]:
                count +=1
            else:
                count -= 1

            if count == 0:
                majorityElementIdx = i
                count = 1

        return nums[majorityElementIdx]
                
				
#############################33
import unittest


class TestSolution(unittest.TestCase):
          
    def test_1(self):
        out = 4
        nums = [4,5,4]
        res = Solution().majorityElement(nums)
        self.assertEqual(res, out)
    
    def test_2(self):
        out = 2
        nums = [2,2,1,1,1,2,2]
        res = Solution().majorityElement(nums)
        self.assertEqual(res, out)
        
    
    def test_3(self):
        out = 3
        nums = [3,2,3]
        res = Solution().majorityElement(nums)
        self.assertEqual(res, out)
        
    
        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

    