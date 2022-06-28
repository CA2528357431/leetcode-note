# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        li = []
        loc = 1
        cur = head.next
        pre = head.val
        while cur.next:
            if pre < cur.val > cur.next.val or pre > cur.val < cur.next.val:
                li.append(loc)
            pre = cur.val
            cur = cur.next
            loc += 1
        print(li)
        if len(li) <= 1:
            return [-1, -1]

        big = li[-1] - li[0]
        small = 99999
        for i in range(1, len(li)):
            small = min(small, li[i] - li[i - 1])
        return [small, big]
