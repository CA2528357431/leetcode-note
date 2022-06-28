"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        def do(cur):
            if not cur:
                return
            res.append(cur.val)
            for s in cur.children:
                do(s)
        do(root)
        return res