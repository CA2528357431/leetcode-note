# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:

        i = 0
        cur = head
        while cur:
            i += 1
            cur = cur.next
        n = i // k
        num = i % k
        res = []

        cur = head
        for j in range(k):
            if j < num:
                res.append(cur)
                for jj in range(n):
                    cur = cur.next
                ne = cur.next
                cur.next = None
                cur = ne
            else:
                if n == 0:
                    res.append(None)
                    continue
                res.append(cur)
                for jj in range(n - 1):
                    cur = cur.next
                ne = cur.next
                cur.next = None
                cur = ne
        return res