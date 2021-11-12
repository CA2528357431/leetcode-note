# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None

        # 如果有环，则 “fast slow初次交点” 与 “head” 到 ”入环点“ 等距离

        slow = head.next
        fast = head.next.next
        while fast and fast.next and slow != fast:
            fast = fast.next.next
            slow = slow.next

        if not fast or not fast.next:
            return None

        a = head
        b = fast

        while a != b:
            a = a.next
            b = b.next

        return a