class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        f = head
        s = head
        while f is not None and f.next is not None:
            f = f.next.next
            s = s.next
        return s
    # 快慢针