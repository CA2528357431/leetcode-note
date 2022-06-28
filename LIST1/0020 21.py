# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        # 递归

        '''
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        else:
            if l1.val<l2.val:
                l1.next = self.mergeTwoLists(l1.next,l2)
                return l1
            else:
                l2.next = self.mergeTwoLists(l1,l2.next)
                return l2
        '''

        # 多指针

        # 用于记录新的头部
        pre = ListNode()

        # 创建l1 l2 res 的指针
        cur = pre
        cur1 = l1
        cur2 = l2

        while cur1 and cur2:
            if cur1.val<cur2.val:
                cur.next = cur1
                cur = cur.next
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur = cur.next
                cur2 = cur2.next

        # 把多余的加入res
        if cur1:
            cur.next = cur1
        else:
            cur.next = cur2
        return pre.next