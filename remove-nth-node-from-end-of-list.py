# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    
    #faster solution - faster than 98.91% of Python online submissions for Remove Nth Node From End of List.
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        current = head        
        nthPrev = None
        nodeToDelete = None        
        step = 1
        
        while current.next:
            current = current.next
            
            if step + 1 == n:
                nodeToDelete = head
            elif nodeToDelete:                
                nodeToDelete = nodeToDelete.next
            
            if step == n:
                nthPrev = head
            elif nthPrev:        
                nthPrev = nthPrev.next
            
            step += 1
        
        if not nthPrev and nodeToDelete:
            head = nodeToDelete.next            
        elif not nthPrev:
            head = None        
        elif not nthPrev.next and not nthPrev.next.next:
            nthPrev.next = None
        else:                
            nthPrev.next = nthPrev.next.next
        
        return head
    
	
    #solution with explanation
    def removeNthFromEndTmp(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        current = head        
        nodeToDeletePrev = None
        nodeToDelete = None        
        step = 1
        
        while current.next:
            current = current.next
            
            if step + 1 == n:
                nodeToDelete = head
            elif nodeToDelete:                
                nodeToDelete = nodeToDelete.next
            
            if step == n:
                nodeToDeletePrev = head
            elif nodeToDeletePrev:        
                nodeToDeletePrev = nodeToDeletePrev.next
            
            step += 1
        
        #if new list starts from deleting element
        if not nodeToDeletePrev and nodeToDelete:
            head = nodeToDelete.next
            
        #if we just delete element from list constitng only from 1 element
        elif not nodeToDeletePrev:
            head = None
            
        #if we delete last element from list
        elif not nodeToDeletePrev.next and not nodeToDeletePrev.next.next:
            nodeToDeletePrev.next = None
        
        #if we delete element from middle of the list
        else:                
            nodeToDeletePrev.next = nodeToDeletePrev.next.next
        
        return head