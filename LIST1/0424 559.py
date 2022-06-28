"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def judge(cur):
            if not cur:
                return 0
            res = 1
            for x in cur.children:
                res = max(res,judge(x)+1)
            return res
        return judge(root)