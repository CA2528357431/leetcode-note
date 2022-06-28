# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        def find(li):
            re = li[0].val
            for x in li:
                re = max(re, x.val)
            return re

        res = []
        cur = [root]
        while cur:
            nxt = []
            for x in cur:
                if x.left:
                    nxt.append(x.left)
                if x.right:
                    nxt.append(x.right)
            res.append(find(cur))
            cur = nxt
        return res
