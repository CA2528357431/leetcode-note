# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        l = 0

        cur = head
        while cur:
            l += 1
            cur = cur.next

        if l == 0:
            return None

        k = k % l
        if k == 0:
            return head

        f = head
        for _ in range(k):
            f = f.next
        s = head
        while f.next:
            f = f.next
            s = s.next
        neohead = s.next
        s.next = None
        f.next = head

        return neohead