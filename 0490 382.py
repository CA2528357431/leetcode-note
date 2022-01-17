# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head


    def getRandom(self) -> int:
        res = -1311
        i = 1
        cur = self.head
        while cur:
            x = random.randint(0,i-1)
            if x==0:
                res = cur.val
            i+=1
            cur = cur.next
        return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()