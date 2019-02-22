"""
141. Linked List Cycle

Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.


Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.


Solutions:
+++ Except-ionally fast Python -https://leetcode.com/problems/linked-list-cycle/discuss/44494/Except-ionally-fast-Python
walker and runner. https://leetcode.com/problems/linked-list-cycle/discuss/44489/O(1)-Space-Solution
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
Runtime: 44 ms, faster than 93.67% of Python online submissions for Linked List Cycle.
Memory Usage: 17.1 MB, less than 44.01% of Python online submissions for Linked List Cycle.
"""
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if not head:
            return False
        
        normalPointer = head
        nextPointer = head.next
        
        while normalPointer != nextPointer:
            
            if not nextPointer or not nextPointer.next:
                return False
            
            normalPointer = normalPointer.next
            nextPointer = nextPointer.next.next
            
            
        return True


"""
Runtime: 36 ms, faster than 100.00% of Python online submissions for Linked List Cycle.
Memory Usage: 17.1 MB, less than 48.49% of Python online submissions for Linked List Cycle.
"""
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        try:
            normalPointer = head
            nextPointer = head.next

            while normalPointer != nextPointer:
                normalPointer = normalPointer.next
                nextPointer = nextPointer.next.next

            return True
            
        except:
            return False
        
            
            
            
        
        

		
        