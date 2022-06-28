"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None

        def get(root):
            if not root:
                return None
            head = root
            if root.left:
                l = get(root.left)
                head = l

                while l.right:
                    l = l.right
                l.right = root
                root.left = l
            if root.right:
                r = get(root.right)
                r.left = root
                root.right = r

            return head

        root = get(root)
        cur = root
        while cur.right:
            cur = cur.right
        cur.right = root
        root.left = cur
        return root