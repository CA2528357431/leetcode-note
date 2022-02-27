# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        la=None
        cur=head
        while cur:
            ne=cur.next
            cur.next=la
            la=cur
            cur=ne
        return la