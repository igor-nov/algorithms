"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.



Runtime: 24 ms, faster than 100.00% of Python online submissions for Jump Game.

Solutions:
https://leetcode.com/problems/jump-game/solution/
https://leetcode.com/problems/jump-game/discuss/20907/1-6-lines-O(n)-time-O(1)-space
https://leetcode.com/problems/jump-game/discuss/20944/Java-98-Percentile-Solution
"""


class Solution(object):    
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """        
        targetIdx = len(nums) - 1
        for idx in xrange(len(nums)-2, -1, -1):            
            if idx + nums[idx] >= targetIdx:
                targetIdx = idx
        
        return True if targetIdx == 0 else False