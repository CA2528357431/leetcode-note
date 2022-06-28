# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next:
            return

        pre = ListNode()
        pre.next = head
        slow = pre
        fast = pre
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        right = slow.next
        slow.next = None

        pr = right
        ne = pr.next
        while ne:
            neo = ne.next
            ne.next = pr
            pr, ne = ne, neo

        right.next = None
        right = pr

        left = head

        cur = pre
        while left or right:
            if left and right:
                nl = left.next
                nr = right.next

                cur.next = left
                left.next = right
                cur = right

                left = nl
                right = nr
            elif not right:
                cur.next = left
                break

        # 找到中点，分为left和right
        # 将二者混杂