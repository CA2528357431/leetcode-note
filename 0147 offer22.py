# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        pr = head
        ne = head
        for x in range(k-1):
            ne = ne.next
        while ne.next:
            ne = ne.next
            pr = pr.next
        return pr