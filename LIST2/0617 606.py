# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def do(cur):
            if not cur:
                return ""

            mid = str(cur.val)
            l = ""
            r = ""
            if cur.left and cur.right:
                l = "(" + do(cur.left) + ")"
                r = "(" + do(cur.right) + ")"
            elif cur.left and not cur.right:
                l = "(" + do(cur.left) + ")"
            elif not cur.left and cur.right:
                l = "()"
                r = "(" + do(cur.right) + ")"

            return mid + l + r

        return do(root)