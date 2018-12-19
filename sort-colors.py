"""

75. Sort Colors

Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]


Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?


Solutions:

https://en.wikipedia.org/wiki/Dutch_national_flag_problem
https://leetcode.com/problems/sort-colors/discuss/26474/Sharing-C%2B%2B-solution-with-Good-Explanation
https://leetcode.com/problems/sort-colors/discuss/26481/Python-O(n)-1-pass-in-place-solution-with-explanation
https://leetcode.com/problems/sort-colors/discuss/26760/C%2B%2B-solution-in-8-lines%3A-an-instance-of-the-Dutch-national-flag-problem-by-Edsger-Dijkstra
https://leetcode.com/problems/sort-colors/discuss/26479/AC-Python-in-place-one-pass-solution-O(n)-time-O(1)-space-no-swap-no-count
https://leetcode.com/problems/sort-colors/discuss/26500/Four-different-solutions

"""

class Solution(object):


	def sortColors1(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

		#Runtime: 20 ms, faster than 100.00% of Python online submissions for Sort Colors.
        start = 0        
        for colorId, colorCounts in enumerate(counts):
            print colorId, colorCounts, start, start+colorCounts, nums
            nums[start:start+colorCounts] = [colorId]*colorCounts
            start += colorCounts    

			
			        counts = {0:0, 1:0, 2:0}
        for num in nums:
            counts[num] +=1            
        print counts
		
		
	def sortColors2(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        end = 0
        #for color:colorNums in enumerate(counts):
        for colorId in xrange(3):
            print nums, colorId, end, end+counts[colorId]
            nums[end:end+counts[colorId]] = [colorId]*(counts[colorId])
            end += counts[colorId]
            print nums
			
	def sortColors3(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        lo = 0
        i = 1
        hi = len(nums)-1

        while i <= hi:
            
            if nums[hi] == 2:
                hi -= 1

            elif nums[lo] == 0:
                i +=1
                lo +=1

            elif nums[lo] == 2:
                nums[lo], nums[hi] = nums[hi], nums[lo]
                hi -= 1
                
            elif nums[i] == 2:
                nums[i], nums[hi] = nums[hi], nums[i]
                hi -= 1
                
            elif nums[i] < nums[lo]:
                nums[i], nums[lo] = nums[lo], nums[i]
                i +=1
                lo +=1

            else:
                i +=1
				
	def sortColors4(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        lo = i = 0
        hi = len(nums)-1
        
        while i <= hi:            
            if nums[i] == 0:
                if i > lo:
                    nums[i], nums[lo] = nums[lo], nums[i]
                lo += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[hi] = nums[hi], nums[i]
                hi -= 1
            else:
                i += 1
				
	def sortColors5(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        med = 1        
        lo = i =  0        
        hi = len(nums)-1
        
        while i <= hi:            
            if nums[i] < med:
                if i > lo:
                    nums[lo], nums[i] = nums[i], nums[lo]
                i += 1
                lo += 1
            elif nums[i] > med:
                nums[i], nums[hi] = nums[hi], nums[i]
                hi -= 1
            else:
                i += 1
				
				
	#Runtime: 20 ms, faster than 100.00% of Python online submissions for Sort Colors.
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        r = w = b = 0
        
        for i in xrange(len(nums)):
            
            if nums[i] == 0:
                nums[r] = 2
                nums[w] = 1
                nums[b] = 0
                r += 1
                w += 1
                b += 1
                
            elif nums[i] == 1:
                nums[r] = 2
                nums[w] = 1                
                r += 1
                w += 1
                
            else:
                nums[r] = 2                
                r += 1       
				
				
	
			
	
