# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        pre = ListNode(-99999, head)
        cur = pre
        while cur and cur.next:

            if cur.val <= cur.next.val:
                cur = cur.next

            else:

                neo = pre
                while neo.next.val <= cur.next.val:
                    if neo == cur.next:
                        break
                    else:
                        neo = neo.next
                if neo == cur.next:
                    cur = cur.next
                else:
                    ne = cur.next.next

                    cur.next.next = neo.next
                    neo.next = cur.next

                    cur.next = ne

        return pre.next