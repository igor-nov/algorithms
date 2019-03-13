"""
160. Intersection of Two Linked Lists

Write a program to find the node at which the intersection of two singly linked lists begins.

Solutions:

My concise python solution, run in O(n) time and O(1) memory - https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/50010/My-concise-python-solution-run-in-O(n)-time-and-O(1)-memory
Concise python code with comments - https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/49798/Concise-python-code-with-comments
Python AC solution with clear explanation - https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/49924/Python-AC-solution-with-clear-explanation
Python Solution: O(n) time and O(1) space - https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/49938/Python-Solution%3A-O(n)-time-and-O(1)-space

"""


#Solutuon 1 - O(n) time,  O(n) space

"""
Runtime: 196 ms, faster than 92.28% of Python online submissions for Intersection of Two Linked Lists.
Memory Usage: 41.4 MB, less than 5.17% of Python online submissions for Intersection of Two Linked Lists.
"""
class Solution(object):
    
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        if not headA or not headB:
            return None
        
        vals = {}
        
        while headA:
            vals[headA] = headA
            headA = headA.next
            
        while headB:
            if  headB in vals:
                return headB
            headB = headB.next
        
            
        return None
		
# Solution 2 - O(n) time, O(1) space

"""
Runtime: 204 ms, faster than 77.27% of Python online submissions for Intersection of Two Linked Lists.
Memory Usage: 40.8 MB, less than 88.33% of Python online submissions for Intersection of Two Linked Lists.
"""
class Solution(object):
    
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        if not headA or not headB:
            return None
        
        pHdA = headA
        pHdB = headB
        
        while pHdA != pHdB:
            
            if pHdA is None:
                pHdA = headB
            else:
                pHdA = pHdA.next
                
                
            if pHdB is None:
                pHdB = headA
            else:
                pHdB = pHdB.next
                
            
        return pHdB
		
#Solution 3 - same as above
class Solution(object):
    
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
		
		if not headA or not headB:
			return None
		
		curHeadA, curHeadB = headA, headB
		
		while headA or headB:
			
			if curHeadA == curHeadB:
				return curHeadA
			
			if not curHeadA:
				curHeadA = headB
			else:
				curHeadA = curHeadA.next
				
			if not curHeadB:
				curHeadB = headA
			else:
				curHeadB = curHeadB.next
		
	
		return None
