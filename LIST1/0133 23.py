# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        pre = ListNode()
        cur = pre
        heap = []
        for x in lists:
            while x:
                heapq.heappush(heap,x.val)
                x = x.next
        while heap:
            neo = ListNode(heapq.heappop(heap))
            cur.next = neo
            cur = cur.next
        return pre.next

        '''
        n = len(lists)
        if n > 2:
            return self.mergeKLists([self.mergeKLists(lists[:n // 2]), self.mergeKLists(lists[n // 2:])])
        elif n == 1:
            return lists[0]
        elif n == 0:
            return None
        else:
    
            l = lists[0]
            r = lists[1]
            pre = ListNode()
            cur = pre
            while l and r:
                if l.val < r.val:
                    cur.next = l
                    cur = cur.next
                    l = l.next
                else:
                    cur.next = r
                    cur = cur.next
                    r = r.next
            if not l:
                cur.next = r
            else:
                cur.next = l
            return pre.next
            '''