# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def do(cur):
            nonlocal res
            if not cur:
                return 0,0
            ls,ln = do(cur.left)
            rs,rn = do(cur.right)
            s = ls+rs+cur.val
            n = ln+rn+1
            if s//n==cur.val:
                res+=1
            return s,n
        do(root)
        return res