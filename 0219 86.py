# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        small = None
        scur = small
        big = None
        bcur = big

        cur = head

        while cur:
            if cur.val < x:
                if not small:
                    small = cur
                    scur = cur
                else:
                    scur.next = cur
                    scur = scur.next
            else:
                if not big:
                    big = cur
                    bcur = cur
                else:
                    bcur.next = cur
                    bcur = bcur.next
            cur = cur.next
        if not small or not big:
            return head

        scur.next = big
        bcur.next = None
        return small