"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if not head:
            node = Node(insertVal)
            node.next = node
            return node

        cur = head
        big = head

        while True:

            if cur.val <= insertVal <= cur.next.val:
                node = Node(insertVal)
                node.next = cur.next
                cur.next = node

                return head
            else:
                cur = cur.next
                if cur.val >= big.val:
                    big = cur
                if cur == head:
                    break
        node = Node(insertVal)
        node.next = big.next
        big.next = node
        return head