# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        res=[]
        cur=head
        while cur:
            res.append(cur.val)
            cur=cur.next
        return res[::-1]