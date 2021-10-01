# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        fast = head
        slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow
        neohead = fast
        neotail = slow
        if neohead.next:
            neohead = neohead.next
            neotail = neotail.next
        cur = neotail.next
        la = neotail
        while cur:
            ne = cur.next
            cur.next = la
            cur,la = ne,cur

        l = head
        r = neohead
        while l!=mid:
            if l.val!=r.val:
                return False
            else:
                l = l.next
                r = r.next
        return l.val==r.val

