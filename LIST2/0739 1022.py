# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def do(cur,pre):
            pp = pre*2+cur.val
            if not cur.left and not cur.right:
                return pp
            l = 0
            r = 0
            if cur.left:
                l = do(cur.left,pp)
            if cur.right:
                r = do(cur.right,pp)
            return l+r
        return do(root,0)