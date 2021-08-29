# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1:
            return head

        c = head
        n = 1
        while c.next:
            c = c.next
            n += 1

        def reverse(node):
            cur = node.next.next
            la = node.next
            for i in range(k - 1):
                ne = cur.next
                cur.next = la
                la = cur
                cur = ne

            res = node.next
            res.next = cur
            node.next = la
            return res

        pre = ListNode()
        pre.next = head
        cur = pre

        for time in range(n // k):
            cur = reverse(cur)
        return pre.next