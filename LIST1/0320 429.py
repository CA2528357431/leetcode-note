"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        res = []
        cur = [root]
        while cur:
            res.append([x.val for x in cur])
            neo = []
            for p in cur:
                neo.extend(p.children)
            cur = neo
        return res
