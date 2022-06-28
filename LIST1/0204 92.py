# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right:
            return head
        pre = ListNode()
        pre.next = head
        cur = pre
        count = 0
        for _ in range(left - 1):
            cur = cur.next
        rhead = cur

        la = cur.next
        cur = cur.next.next
        for _ in range(right - left):
            ne = cur.next
            cur.next = la
            la = cur
            cur = ne
        rhead.next.next = cur
        rhead.next = la
        return pre.next