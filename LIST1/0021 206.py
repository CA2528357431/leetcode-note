# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        la = None
        cur = head
        while cur:
            ne = cur.next
            cur.next = la
            la = cur
            cur = ne
        return la

# 全体向后转
# 对于head，向后转没有目标
# 同时需要记录cur的父节点
# 设置初始为none的pre记录父节点
