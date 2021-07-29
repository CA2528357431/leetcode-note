# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        add = ListNode(0,head)

        f = add
        for _ in range(0, n):
            f = f.next


        s = add
        while f.next is not None:
            f = f.next
            s = s.next
        s.next = s.next.next

        return add.next

# 还是快慢针问题，让f比s先走n，当f到最后一个的时候，s为倒数n+1个，操作即可
# 两大问题
# 1：如果n等于链长，则f直接成为none，无法推进
# 解决————有好的思路被特例打断？修正原数据
# 本题中就在原head之前附加了一个add，使链长到达n+1，可以使用原方法
# 2：如果n等于链长，则head改变
# 此处应该是一个提示，告诉我们需要以新方式获取head
# 添加add解决此问题