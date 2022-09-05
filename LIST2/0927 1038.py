# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        carry = 0

        def do(cur):
            if not cur:
                return 0
            nonlocal carry
            r = do(cur.right)
            carry += cur.val
            cur.val = carry
            do(cur.left)

        do(root)
        return root