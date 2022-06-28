# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        pre = ListNode()

        used = set()

        cur = head
        rescur = pre

        while cur:
            if cur.val not in used and (not cur.next or cur.next.val != cur.val):
                rescur.next = cur
                rescur = rescur.next
            used.add(cur.val)
            cur = cur.next
        rescur.next = None

        return pre.next