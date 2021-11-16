# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        pre = ListNode()
        pre.next = head

        hinder = []
        count = 1
        i = 0

        start = head
        end = None

        cur = head

        while cur:
            i += 1
            if i == count:
                hinder.append(start)
                i = 0
                count += 1
                start = cur.next

                ne = cur.next
                cur.next = None
                cur = ne
            else:
                cur = cur.next

        def reverse(first):
            if not first.next:
                return first

            la = first
            cur = first.next
            first.next = None
            while cur:
                ne = cur.next
                cur.next = la
                la = cur
                cur = ne
            return la

        ii = 0
        cur = pre
        for node in hinder:
            ii += 1
            if ii % 2 == 0:
                neolast = node
                neofirst = reverse(node)
                cur.next = neofirst
                cur = neolast
            else:
                cur.next = node
                while cur.next:
                    cur = cur.next

        if start:
            if i % 2 == 0:
                neolast = start
                neofirst = reverse(start)
                cur.next = neofirst
                cur = neolast
            else:
                cur.next = start

        return pre.next