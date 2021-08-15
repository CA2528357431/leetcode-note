# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur1 = l1
        cur2 = l2
        la = 0
        pre = ListNode()
        cur = pre
        while cur1 or cur2 or la:
            num = la
            if cur1:
                num += cur1.val
                cur1 = cur1.next
            if cur2:
                num += cur2.val
                cur2 = cur2.next
            if num >= 10:
                la = 1
                num -= 10
            else:
                la = 0

            neo = ListNode(num)
            cur.next = neo

            cur = cur.next

        return pre.next