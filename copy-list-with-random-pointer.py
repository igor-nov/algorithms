"""
138. Copy List with Random Pointer

A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
Return a deep copy of the list.


Solution:
+++ Clone A Linked List (With Random Pointers) - Linear Space Solution & Tricky Constant Space Solution - https://www.youtube.com/watch?v=OvpKeraoxW0&feature=youtu.be&t=1016
My accepted Java code. O(n) but need to iterate the list 3 times - https://leetcode.com/problems/copy-list-with-random-pointer/discuss/43515/My-accepted-Java-code.-O(n)-but-need-to-iterate-the-list-3-times

"""

"""
Runtime: 68 ms, faster than 97.02% of Python online submissions for Copy List with Random Pointer.
Memory Usage: 19.8 MB, less than 71.50% of Python online submissions for Copy List with Random Pointer.

time O(n)
space O(n)
"""
class Solution(object):
    
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        
        if not head:
            return None
        
        originHead = head
        dictCopy = {}        
        while head:            
            dictCopy[head] = RandomListNode(head.label)
            head = head.next
            
        head = originHead        
        
        while head:
            
            if head.next:
                dictCopy[head].next = dictCopy[head.next]
            
            if head.random:
                dictCopy[head].random = dictCopy[head.random]
            
            head = head.next
        
        copiedListHead = dictCopy[originHead]
        
        return copiedListHead 
		
"""
Runtime: 68 ms, faster than 97.02% of Python online submissions for Copy List with Random Pointer.
Memory Usage: 19.9 MB, less than 36.09% of Python online submissions for Copy List with Random Pointer.

time O(n)
space O(1)
"""
class Solution(object):
    
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        
        if not head:
            return None
        
        originHead = head        
        while head:
            clonedNode = RandomListNode(head.label)            
            clonedNode.next = head.next
            head.next = clonedNode
            
            head = clonedNode.next
        
        head = originHead
        
        while head:
            if head.random:
                head.next.random = head.random.next
            head = head.next.next
                
        head = originHead
        headCloned = clonedCurrent = head.next
        while head:            
            head.next = head.next.next            
            
            if clonedCurrent.next:
                clonedCurrent.next = clonedCurrent.next.next            
                
            clonedCurrent = clonedCurrent.next            
            head = head.next
            
        
        #head = originHead
        
        return headCloned
