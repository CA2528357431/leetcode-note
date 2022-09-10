# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def do(x):
            if not x:
                return None
            if x.val<low:
                return do(x.right)
            elif x.val>high:
                return do(x.left)
            else:
                x.left = do(x.left)
                x.right = do(x.right)
                return x
        return do(root)