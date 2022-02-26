# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = ListNode()
        w = pre
        cur = head.next
        num = 0
        while cur:
            if cur.val!=0:
                num+=cur.val
            else:
                neo = ListNode(num)
                num = 0
                w.next = neo
                w = neo
            cur = cur.next
        return pre.next