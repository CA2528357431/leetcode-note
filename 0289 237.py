# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        while node.next:
            node.val = node.next.val
            if node.next.next is None:
                node.next = None
                return
            node = node.next

        # 逐个改值，使得node之后的值依次迁移，再删除尾节点