# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        def sort(first, last):
            if first.next == last:
                first.next = None
                # 断开节点
                # merge的链表必须有一个出口
                return first

            slow = fast = first
            while fast != last and fast.next != last:
                slow = slow.next
                fast = fast.next.next
            # 找中点

            mid = slow
            a = sort(mid, last)
            b = sort(first, mid)
            m = merge(a, b)
            return m

        def merge(a, b):
            h = ListNode()
            cur = h
            while a and b:
                if a.val <= b.val:
                    cur.next = a
                    a = a.next
                else:
                    cur.next = b
                    b = b.next
                cur = cur.next
            if a:
                cur.next = a
            else:
                cur.next = b
            return h.next

        return sort(head, None)