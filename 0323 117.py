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
        if not root: 
            return 
        cur=root
        while cur:
            pre = Node(-1)
            needle = pre

            # 思路是串联同层的节点
            while cur:
                if cur.left:
                    needle.next=cur.left
                    needle=needle.next
                if cur.right:
                    needle.next=cur.right
                    needle=needle.next
                # 链接本层cur的子节点

                cur=cur.next
                # 切换到本层下一个节点
            cur=pre.next



        return root