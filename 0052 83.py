# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        cur = head
        col = {head.val}
        while cur.next:
            if cur.next.val not in col:
                col.add(cur.next.val)
                cur = cur.next
            else:
                cur.next = cur.next.next
        return head
