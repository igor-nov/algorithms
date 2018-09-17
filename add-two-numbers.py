"""
https://leetcode.com/problems/add-two-numbers/description/
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assum_rese the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        l1_head = l1
        l2_head = l2
        accumulator = 0
        new_node_header = ListNode(0)
        new_node = new_node_header

        while True:

            if l1_head and l1_head.val:
                num1 = l1_head.val
            else:
                num1 = 0

            if l2_head and l2_head.val:
                num2 = l2_head.val
            else:
                num2 = 0

            print('val1 %s + val2 %s + acc %s' % (num1, num2, accumulator))
            [accumulator, new_node.val] = divmod(num1 + num2 + accumulator, 10)
            print(new_node.val)

            if l1_head and l1_head.next:
                l1_head = l1_head.next
            else:
                l1_head = None

            if l2_head and l2_head.next:
                l2_head = l2_head.next
            else:
                l2_head = None

            if not l1_head and not l2_head:
                if accumulator:
                    last_node = ListNode(accumulator)
                    new_node.next = last_node
                break
            else:
                new_node.next = ListNode(0)
                new_node = new_node.next

        return new_node_header

    def addTwoNumbers2(self, l1, l2):

        offset = 0
        new_node = ListNode(offset)
        current = new_node
        item1 = l1
        item2 = l2

        while True:
            try:
                if item1.val:
                    value1 = item1.val
                else:
                    value1 = 0

                if item2.val:
                    value2 = item2.val
                else:
                    value2 = 0

                sum_res = value1 + value2 + current.val
                offset = sum_res / 10
                current.val = sum_res % 10

                if item1.next is not None or item2.next is not None or offset:
                    current.next = ListNode(offset)
                    current = current.next

                    if item1.next is not None:
                        item1 = item1.next
                    else:
                        item1 = ListNode(0)

                    if item2.next is not None:
                        item2 = item2.next
                    else:
                        item2 = ListNode(0)

                else:
                    break

            except Exception as e:
                print 'exeption : %s' % e
                break

        return new_node


l1_1 = ListNode(2)
l1_2 = ListNode(4)
l1_3 = ListNode(3)
l1_1.next = l1_2
l1_2.next = l1_3

l2_1 = ListNode(5)
l2_2 = ListNode(6)
l2_3 = ListNode(4)
l2_1.next = l2_2
l2_2.next = l2_3

solution = Solution()
res = solution.addTwoNumbers(l1_1, l2_1)

print(res)
