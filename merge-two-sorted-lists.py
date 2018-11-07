"""

Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4


Other variants:
https://leetcode.com/problems/merge-two-sorted-lists/discuss/9916/Clean-recursive-python-solution
https://leetcode.com/problems/merge-two-sorted-lists/discuss/9735/Python-solutions-(iteratively-recursively-iteratively-in-place).
"""



# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    
    def setNode(self, l1, l2):
        
        if l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                newVal = l1.val
                l1 = l1.next
            else:
                newVal = l2.val
                l2 = l2.next
                
        elif l1 is not None:
            newVal = l1.val
            l1 = l1.next   
            
        else:
            newVal = l2.val
            l2 = l2.next
            
        newNode = ListNode(newVal)
        
        return newNode, l1, l2
        
    
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 and l2:
            
            newNode, currentL1, currentL2 = self.setNode(l1, l2)
            mergedList = newNode            
            tail = mergedList
                        
            while currentL1 is not None or currentL2 is not None:                
                newNode, currentL1, currentL2 = self.setNode(currentL1, currentL2)
                tail.next = newNode
                tail = tail.next
                     
            return mergedList
            
        elif l1:
            return l1
        
        else:
            return l2
        
        
#     def mergeTwoLists2(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
        
#         if not l1:
#             return l2
#         if not l2:
#             print 'l1 %s ' %l1
#             return l1
        
#         start = None    
#         if l1.val <= l2.val:
#             start = l1;
#             start.next = self.mergeTwoLists2(l1.next, l2)
#         else:
#             start = l2;
#             start.next = self.mergeTwoLists2(l1, l2.next)
        
#         return start

        
l11 = ListNode(1)
l12 = ListNode(2)
l11.next = l12
l13 = ListNode(4)
l12.next = l13

#l11 = None

l21 = ListNode(0)
l22 = ListNode(3)
l21.next = l22
l23 = ListNode(4)
l22.next = l23
l24 = ListNode(4)
l23.next = l24

# print l11.val
# print l11.next.val
# print l11.next.next.val

# print l21.val
# print l21.next.val
# print l21.next.next.val

res = Solution().mergeTwoLists(l11, l21)

print '----'

print res.val
print res.next.val
print res.next.next.val
print res.next.next.next.val
print res.next.next.next.next.val
print res.next.next.next.next.next.val
#print res.next.next.next.next.next.next.val

#Input: 1->2->4, 1->3->4
#Output: 1->1->2->3->4->4
        

        