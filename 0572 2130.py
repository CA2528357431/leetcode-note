# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        pre = ListNode()
        pre.next = head
        f = s = pre
        while f and f.next:
            f = f.next.next
            s = s.next
        hh = s.next
        s.next = None

        pre.next = hh
        la = pre
        cur = hh
        while cur:
            ne = cur.next
            cur.next = la
            la = cur
            cur = ne

        neohead = la

        res = 0
        while head:
            res = max(res, head.val + neohead.val)
            head = head.next
            neohead = neohead.next
        return res




