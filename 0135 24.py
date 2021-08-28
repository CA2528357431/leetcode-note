# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        pre = ListNode()
        pre.next = head
        la = pre
        while la.next and la.next.next:
            cur = la.next
            a = cur.next
            b = cur.next.next
            la.next = a
            a.next = cur
            cur.next = b

            la = la.next.next
        return pre.next