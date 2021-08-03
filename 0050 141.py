# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        f = head
        s = head
        while f and f.next and s:
            f = f.next.next
            s = s.next
            if f==s:
                return True
        return False

    # 快慢针
    # 如果快针在慢针之后，则有环
    # 如果最终跳出循环，说明有none，不是循环