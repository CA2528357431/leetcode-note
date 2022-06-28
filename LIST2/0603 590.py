"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        def do(cur):
            if not cur:
                return
            for x in cur.children:
                do(x)
            res.append(cur.val)
        do(root)
        return res