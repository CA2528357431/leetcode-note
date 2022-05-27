# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        num=root.val
        def do(cur):
            if not cur:
                return True
            if cur.val!=num:
                return False
            l=do(cur.left)
            r=do(cur.right)
            return l and r
        return do(root)