# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        result = 0

        def do(cur):

            if not cur:
                return 0
            res = 1
            height = 1
            l = do(cur.left)
            r = do(cur.right)
            if (cur.left and cur.left.val == cur.val) and (cur.right and cur.right.val == cur.val):
                res += l + r
                height += max(l, r)
            elif cur.left and cur.left.val == cur.val:
                res += l
                height += l
            elif cur.right and cur.right.val == cur.val:
                res += r
                height += r
            nonlocal result
            result = max(res - 1, result)

            return height

        do(root)
        return result