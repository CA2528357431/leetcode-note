# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        pre = ListNode()
        pre.next = head
        slow = pre
        fast = pre
        while fast and fast.next:

            slow = slow.next
            fast = fast.next.next

        right = slow.next

        pr = right
        ne = pr.next
        while ne:
            neo = ne.next
            ne.next = pr
            pr, ne = ne, neo
        right.next = None
        right = pr

        slow.next = None
        left = head

        print(head.val,head.next.val)


        cur = pre
        while left and right:
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
a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
a.next = b
b.next = c
c.next = d

sol = Solution()
sol.reorderList(a)
print(a.val,a.next.val,a.next.next.val,a.next.next.val)
