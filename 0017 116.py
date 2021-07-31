"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return None
        if root.left is None:
            return root

        cur = root
        while cur:
            cur.left.next = cur.right
            if cur.next:
                cur.right.next = cur.next.left
            cur = cur.next
        self.connect(root.left)
        return root

    # next指针使得每一行形成链表
    # 利用上一层来指引下一层链接